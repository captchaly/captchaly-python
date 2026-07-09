import logging
import os
import warnings
from typing import Optional, Self

from httpx import AsyncClient
from httpx import __version__ as _httpx_version
from synchronicity import Synchronizer as _Synchronizer

from . import model
from .__version__ import __version__
from .exception import CaptchalyError
from .warning import CaptchalyWarning

_APIKEY_ENV_NAME = "CAPTCHALY_APIKEY"
_BASE_URL = "https://v1.captchaly.com"
_USER_AGENT = f"captchaly-py/{__version__} httpx/{_httpx_version}"
_REQUEST_TIMEOUT = 180
_WARNING_HEADER = "X-Captchaly-Warning"

_logger = logging.getLogger("captchaly")

_synchronizer = _Synchronizer()


@_synchronizer.wrap
class CaptchalyClient:
	def __init__(self, apikey: Optional[str] = None):
		"""
		Args:
			apikey (Optional[str]): The API key for Captchaly. If not provided, it will be retrieved from the environment variable `CAPTCHALY_APIKEY`.
		"""
		apikey = os.environ.get(_APIKEY_ENV_NAME, apikey)
		if not apikey:
			raise ValueError(
				f"API key must be provided either as an argument or through the environment variable '{_APIKEY_ENV_NAME}'!"
			)

		self._apikey = apikey

	@property
	def apikey(self) -> str:
		return self._apikey

	async def __aenter__(self) -> Self:
		self._http_client = await AsyncClient(
			base_url=_BASE_URL,
			timeout=_REQUEST_TIMEOUT,
			http2=True,
			headers={
				"Authorization": f"Bearer {self.apikey}",
				"User-Agent": _USER_AGENT,
			},
		).__aenter__()
		return self

	async def __aexit__(self, exc_type, exc_value, traceback):
		await self._http_client.__aexit__(exc_type, exc_value, traceback)

	async def _request(self, method: str, url: str, tries: int, **kwargs):
		for attempt in range(1, tries + 1):
			response = await self._http_client.request(method, url, **kwargs)
			if response.status_code != 503:
				break
			_logger.info("Captchaly unable to solve, retrying... (%d/%d)", attempt, tries)
		else:
			raise CaptchalyError(
				f"Failed to get successful response after {tries} attempts. "
				"Check your parameter or try again later. If the issue persists, please contact support."
			)

		# TODO: only warn once per session
		if _WARNING_HEADER in response.headers:
			message = response.headers[_WARNING_HEADER]
			warnings.warn(message, CaptchalyWarning)
			_logger.warning(message)

		if response.status_code != 200:
			raise CaptchalyError(
				f"Request failed with status code {response.status_code}: {response.text}"
			)

		return response.json()

	async def account(self) -> model.Account:
		"""
		Get account information.
		"""
		data = await self._request("GET", "/account", tries=1)
		return model.Account(**data)  # pyright: ignore[reportCallIssue]

	async def hcaptcha(
		self, url: str, sitekey: str, proxy: Optional[str] = None, *, tries: int = 3
	) -> model.Hcaptcha:
		"""
		Solve hCaptcha and return the captcha token (`h-captcha-response`) that to be submitted to the target website.
		Args:
			url (str): The URL where the captcha is located on, or you can only just use the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example.com`

			sitekey (str): The value of the `data-sitekey` property of the captcha `div` element, or the value of the `sitekey` parameter of the requests from the webpage to the hCaptcha server. For example: `a5f74b19-9e45-40e0-b45d-47ff91b7a6c2`

			proxy (Optional[str]): The proxy used to solve the captcha. Must match the format `scheme://host:port`, or `scheme://username:password@host:port` if authentication is required. Examples: `http://john:my_password@myproxy.com:8080`, `http://123.123.123.123:8080`

			tries (int): How many attempts until not receiving a 503 status code from Captchaly.
		"""
		params = {
			"url": url,
			"sitekey": sitekey,
		}
		if isinstance(proxy, str):
			params["proxy"] = proxy
		data = await self._request("GET", "/hcaptcha", tries=tries, params=params)
		return model.Hcaptcha(**data)  # pyright: ignore[reportCallIssue]

	async def hcaptcha_enterprise(
		self,
		url: str,
		sitekey: str,
		proxy: Optional[str] = None,
		rqdata: Optional[str] = None,
		*,
		tries: int = 3,
	) -> model.Hcaptcha:
		"""
		Solve hCaptcha Enterprise and return the captcha token (`h-captcha-response`) that to be submitted to the target website.
		Args:
			url (str): The URL where the captcha is located on, or you can only just use the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example.com`

			sitekey (str): The value of the `data-sitekey` property of the captcha `div` element, or the value of the `sitekey` parameter of the requests from the webpage to the hCaptcha server. For example: `a5f74b19-9e45-40e0-b45d-47ff91b7a6c2`

			proxy (Optional[str]): The proxy used to solve the captcha. Must match the format `scheme://host:port`, or `scheme://username:password@host:port` if authentication is required. Examples: `http://john:my_password@myproxy.com:8080`, `http://123.123.123.123:8080`

			rqdata (Optional[str]): The `rqdata` value required by some sites. Recommendation: Also providing the proxy argument when targeting these websites.

			tries (int): How many attempts until not receiving a 503 status code from Captchaly.
		"""
		params = {
			"url": url,
			"sitekey": sitekey,
		}
		if isinstance(proxy, str):
			params["proxy"] = proxy
		if isinstance(rqdata, str):
			params["rqdata"] = rqdata
		data = await self._request("GET", "/hcaptcha-enterprise", tries=tries, params=params)
		return model.Hcaptcha(**data)  # pyright: ignore[reportCallIssue]

	async def turnstile(
		self,
		url: str,
		sitekey: str,
		action: Optional[str] = None,
		cdata: Optional[str] = None,
		*,
		tries: int = 3,
	) -> model.Turnstile:
		"""
		Solve Cloudflare Turnstile and return the captcha token (`cf-turnstile-response`) that to be submitted to the target website.
		Args:
			url (str): The URL where the captcha is located on, or you can use only the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example.com`

			sitekey (str): The value of the `data-sitekey` property of the captcha `div` element, or the value of the `sitekey` argument of call to `turnstile.render()` or `turnstile.execute()`, typically prefixed with 0x, for example: `0x4AAAAAAAA-1LUipBaoBpsG`

			action (Optional[str]): The value of the `data-action` property of the captcha element, or the value of the `action` argument in the call to `turnstile.render()` or `turnstile.execute()`

			cdata (Optional[str]): The value of the `data-cdata` property of the captcha element, or the value of the `cData` argument in the call to `turnstile.render()` or `turnstile.execute()`

			tries (int): How many attempts until not receiving a 503 status code from Captchaly.
		"""
		params = {"url": url, "sitekey": sitekey}
		if isinstance(action, str):
			params["action"] = action
		if isinstance(cdata, str):
			params["cdata"] = cdata
		data = await self._request("GET", "/turnstile", tries=tries, params=params)
		return model.Turnstile(**data)  # pyright: ignore[reportCallIssue]

	async def recaptcha_v2(self, url: str, sitekey: str, *, tries: int = 3) -> model.Recaptcha:
		"""
		Solve reCAPTCHA v2 and return the captcha token (`g-recaptcha-response`) that to be submitted to the target website.
		Args:
			url (str): The URL where the captcha is located on, or you can only just use the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example`

			sitekey (str): The value of the `data-sitekey` property of the captcha div element, or the value of the k parameter of the requests from the webpage to the reCaptcha server. For example: `6LdKlZEpAAAAAAOQjzC2v_d36tWxCl6dWsozdSy9`

			tries (int): How many attempts until not receiving a 503 status code from Captchaly.
		"""
		params = {"url": url, "sitekey": sitekey}
		data = await self._request("GET", "/recaptchav2", tries=tries, params=params)
		return model.Recaptcha(**data)  # pyright: ignore[reportCallIssue]

	async def recaptcha_v3(
		self,
		url: str,
		sitekey: str,
		action: str,
		fast: Optional[bool] = None,
		*,
		tries: int = 3,
	) -> model.Recaptcha:
		"""
		Solve reCAPTCHA v3 and return the captcha token (`g-recaptcha-response`) that to be submitted to the target website.
		Args:
			url (str): The URL where the captcha is located on, or you can only just use the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example`

			sitekey (str): The value of the `data-sitekey` property of the captcha `div` element, or the value of the `k` parameter of the requests from the webpage to the reCaptcha server. For example: `6LdKlZEpAAAAAAOQjzC2v_d36tWxCl6dWsozdSy9`

			action (str): The value of the `data-action` property of the captcha `div` element, for example: `submit`

			fast (Optional[bool]): Prioritize speed over quality. Recaptcha V3 works by determining how human-like a client is, when set to `True`, tokens are returned faster but with a lower human score (0.3 or lower). The default value is false (better score).

			tries (int): How many attempts until not receiving a 503 status code from Captchaly.
		"""
		params = {"url": url, "sitekey": sitekey, "action": action}
		if isinstance(fast, bool):
			params["fast"] = str(fast).lower()
		data = await self._request("GET", "/recaptchav3", tries=tries, params=params)
		return model.Recaptcha(**data)  # pyright: ignore[reportCallIssue]

	async def geetest(self, url: str, captchaId: str, *, tries: int = 3) -> model.Geetest:
		"""
		Solve GeeTest and return the captcha token that to be submitted to the target website.
		Args:
			url (str): The URL where the captcha is located on, or you can only just use the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example`

			captchaId (str): The value of the `captcha_id` (or `captchaID`) parameter of the requests from the webpage to the Geetest server. For example: `e392e1d7fd421dc63325744d5a2b9c73`

			tries (int): How many attempts until not receiving a 503 status code from Captchaly.
		"""
		params = {"url": url, "captchaId": captchaId}
		data = await self._request("GET", "/geetest", tries=tries, params=params)
		return model.Geetest(**data)  # pyright: ignore[reportCallIssue]
