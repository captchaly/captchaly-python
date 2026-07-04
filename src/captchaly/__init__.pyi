import src.captchaly.model
import typing
import typing_extensions

class CaptchalyClient:

    def __init__(self, apikey: str | None = None):
        """Args:
                apikey (Optional[str]): The API key for Captchaly. If not provided, it will be retrieved from the environment variable `CAPTCHALY_APIKEY`.
        """
        ...

    @property
    def apikey(self) -> str:
        ...

    def __enter__(self) -> typing.Self:
        ...

    async def __aenter__(self) -> typing.Self:
        ...

    def __exit__(self, exc_type, exc_value, traceback):
        ...

    async def __aexit__(self, exc_type, exc_value, traceback):
        ...

    class ___request_spec(typing_extensions.Protocol):
        def __call__(self, /, method: str, url: str, tries: int, **kwargs):
            ...

        async def aio(self, /, method: str, url: str, tries: int, **kwargs):
            ...

    _request: ___request_spec

    class __account_spec(typing_extensions.Protocol):
        def __call__(self, /) -> src.captchaly.model.Account:
            """Get account information."""
            ...

        async def aio(self, /) -> src.captchaly.model.Account:
            """Get account information."""
            ...

    account: __account_spec

    class __hcaptcha_spec(typing_extensions.Protocol):
        def __call__(self, /, url: str, sitekey: str, proxy: str | None = None, *, tries: int = 3) -> src.captchaly.model.Hcaptcha:
            """Solve hCaptcha and return the captcha token (`h-captcha-response`) that to be submitted to the target website.
            Args:
                    url (str): The URL where the captcha is located on, or you can only just use the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example.com`

                    sitekey (str): The value of the data-sitekey property of the captcha `div` element, or the value of the `sitekey` parameter of the requests from the webpage to the hCaptcha server. For example: `a5f74b19-9e45-40e0-b45d-47ff91b7a6c2`

                    proxy (Optional[str]): The proxy used to solve the captcha. Must match the format `scheme://host:port`, or `scheme://username:password@host:port` if authentication is required. Examples: `http://john:my_password@myproxy.com:8080`, `http://123.123.123.123:8080`

                    tries (int): How many attempts until not receiving a 503 status code from Captchaly.
            """
            ...

        async def aio(self, /, url: str, sitekey: str, proxy: str | None = None, *, tries: int = 3) -> src.captchaly.model.Hcaptcha:
            """Solve hCaptcha and return the captcha token (`h-captcha-response`) that to be submitted to the target website.
            Args:
                    url (str): The URL where the captcha is located on, or you can only just use the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example.com`

                    sitekey (str): The value of the data-sitekey property of the captcha `div` element, or the value of the `sitekey` parameter of the requests from the webpage to the hCaptcha server. For example: `a5f74b19-9e45-40e0-b45d-47ff91b7a6c2`

                    proxy (Optional[str]): The proxy used to solve the captcha. Must match the format `scheme://host:port`, or `scheme://username:password@host:port` if authentication is required. Examples: `http://john:my_password@myproxy.com:8080`, `http://123.123.123.123:8080`

                    tries (int): How many attempts until not receiving a 503 status code from Captchaly.
            """
            ...

    hcaptcha: __hcaptcha_spec

    class __hcaptcha_enterprise_spec(typing_extensions.Protocol):
        def __call__(self, /, url: str, sitekey: str, proxy: str | None = None, rqdata: str | None = None, *, tries: int = 3) -> src.captchaly.model.Hcaptcha:
            """Solve hCaptcha Enterprise and return the captcha token (`h-captcha-response`) that to be submitted to the target website.
            Args:
                    url (str): The URL where the captcha is located on, or you can only just use the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example.com`

                    sitekey (str): The value of the data-sitekey property of the captcha `div` element, or the value of the `sitekey` parameter of the requests from the webpage to the hCaptcha server. For example: `a5f74b19-9e45-40e0-b45d-47ff91b7a6c2`

                    proxy (Optional[str]): The proxy used to solve the captcha. Must match the format `scheme://host:port`, or `scheme://username:password@host:port` if authentication is required. Examples: `http://john:my_password@myproxy.com:8080`, `http://123.123.123.123:8080`

                    rqdata (Optional[str]): The `rqdata` value required by some sites. Recommendation: Also providing the proxy argument when targeting these websites.

                    tries (int): How many attempts until not receiving a 503 status code from Captchaly.
            """
            ...

        async def aio(self, /, url: str, sitekey: str, proxy: str | None = None, rqdata: str | None = None, *, tries: int = 3) -> src.captchaly.model.Hcaptcha:
            """Solve hCaptcha Enterprise and return the captcha token (`h-captcha-response`) that to be submitted to the target website.
            Args:
                    url (str): The URL where the captcha is located on, or you can only just use the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example.com`

                    sitekey (str): The value of the data-sitekey property of the captcha `div` element, or the value of the `sitekey` parameter of the requests from the webpage to the hCaptcha server. For example: `a5f74b19-9e45-40e0-b45d-47ff91b7a6c2`

                    proxy (Optional[str]): The proxy used to solve the captcha. Must match the format `scheme://host:port`, or `scheme://username:password@host:port` if authentication is required. Examples: `http://john:my_password@myproxy.com:8080`, `http://123.123.123.123:8080`

                    rqdata (Optional[str]): The `rqdata` value required by some sites. Recommendation: Also providing the proxy argument when targeting these websites.

                    tries (int): How many attempts until not receiving a 503 status code from Captchaly.
            """
            ...

    hcaptcha_enterprise: __hcaptcha_enterprise_spec

    class __turnstile_spec(typing_extensions.Protocol):
        def __call__(self, /, url: str, sitekey: str, action: str | None = None, cdata: str | None = None, *, tries: int = 3) -> src.captchaly.model.Turnstile:
            """Solve Cloudflare Turnstile and return the captcha token (`cf-turnstile-response`) that to be submitted to the target website.
            Args:
                    url (str): The URL where the captcha is located on, or you can use only the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example.com`

                    sitekey (str): The value of the `data-sitekey` property of the captcha `div` element, or the value of the `sitekey` argument of call to `turnstile.render()` or `turnstile.execute()`, typically prefixed with 0x, for example: `0x4AAAAAAAA-1LUipBaoBpsG`

                    action (Optional[str]): The value of the `data-action` property of the captcha element, or the value of the `action` argument in the call to `turnstile.render()` or `turnstile.execute()`

                    cdata (Optional[str]): The value of the `data-cdata` property of the captcha element, or the value of the `cData` argument in the call to `turnstile.render()` or `turnstile.execute()`

                    tries (int): How many attempts until not receiving a 503 status code from Captchaly.
            """
            ...

        async def aio(self, /, url: str, sitekey: str, action: str | None = None, cdata: str | None = None, *, tries: int = 3) -> src.captchaly.model.Turnstile:
            """Solve Cloudflare Turnstile and return the captcha token (`cf-turnstile-response`) that to be submitted to the target website.
            Args:
                    url (str): The URL where the captcha is located on, or you can use only the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example.com`

                    sitekey (str): The value of the `data-sitekey` property of the captcha `div` element, or the value of the `sitekey` argument of call to `turnstile.render()` or `turnstile.execute()`, typically prefixed with 0x, for example: `0x4AAAAAAAA-1LUipBaoBpsG`

                    action (Optional[str]): The value of the `data-action` property of the captcha element, or the value of the `action` argument in the call to `turnstile.render()` or `turnstile.execute()`

                    cdata (Optional[str]): The value of the `data-cdata` property of the captcha element, or the value of the `cData` argument in the call to `turnstile.render()` or `turnstile.execute()`

                    tries (int): How many attempts until not receiving a 503 status code from Captchaly.
            """
            ...

    turnstile: __turnstile_spec

    class __recaptcha_v2_spec(typing_extensions.Protocol):
        def __call__(self, /, url: str, sitekey: str, *, tries: int = 3) -> src.captchaly.model.Recaptcha:
            """Solve reCAPTCHA v2 and return the captcha token (`g-recaptcha-response`) that to be submitted to the target website.
            Args:
                    url (str): The URL where the captcha is located on, or you can only just use the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example`

                    sitekey (str): The value of the `data-sitekey` property of the captcha div element, or the value of the k parameter of the requests from the webpage to the reCaptcha server. For example: `6LdKlZEpAAAAAAOQjzC2v_d36tWxCl6dWsozdSy9`

                    tries (int): How many attempts until not receiving a 503 status code from Captchaly.
            """
            ...

        async def aio(self, /, url: str, sitekey: str, *, tries: int = 3) -> src.captchaly.model.Recaptcha:
            """Solve reCAPTCHA v2 and return the captcha token (`g-recaptcha-response`) that to be submitted to the target website.
            Args:
                    url (str): The URL where the captcha is located on, or you can only just use the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example`

                    sitekey (str): The value of the `data-sitekey` property of the captcha div element, or the value of the k parameter of the requests from the webpage to the reCaptcha server. For example: `6LdKlZEpAAAAAAOQjzC2v_d36tWxCl6dWsozdSy9`

                    tries (int): How many attempts until not receiving a 503 status code from Captchaly.
            """
            ...

    recaptcha_v2: __recaptcha_v2_spec

    class __recaptcha_v3_spec(typing_extensions.Protocol):
        def __call__(self, /, url: str, sitekey: str, action: str, fast: bool | None = None, *, tries: int = 3) -> src.captchaly.model.Recaptcha:
            """Solve reCAPTCHA v3 and return the captcha token (`g-recaptcha-response`) that to be submitted to the target website.
            Args:
                    url (str): The URL where the captcha is located on, or you can only just use the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example`

                    sitekey (str): The value of the `data-sitekey` property of the captcha `div` element, or the value of the `k` parameter of the requests from the webpage to the reCaptcha server. For example: `6LdKlZEpAAAAAAOQjzC2v_d36tWxCl6dWsozdSy9`

                    action (str): The value of the `data-action` property of the captcha `div` element, for example: `submit`

                    fast (Optional[bool]): Prioritize speed over quality. Recaptcha V3 works by determining how human-like a client is, when set to `True`, tokens are returned faster but with a lower human score (0.3 or lower). The default value is false (better score).

                    tries (int): How many attempts until not receiving a 503 status code from Captchaly.
            """
            ...

        async def aio(self, /, url: str, sitekey: str, action: str, fast: bool | None = None, *, tries: int = 3) -> src.captchaly.model.Recaptcha:
            """Solve reCAPTCHA v3 and return the captcha token (`g-recaptcha-response`) that to be submitted to the target website.
            Args:
                    url (str): The URL where the captcha is located on, or you can only just use the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example`

                    sitekey (str): The value of the `data-sitekey` property of the captcha `div` element, or the value of the `k` parameter of the requests from the webpage to the reCaptcha server. For example: `6LdKlZEpAAAAAAOQjzC2v_d36tWxCl6dWsozdSy9`

                    action (str): The value of the `data-action` property of the captcha `div` element, for example: `submit`

                    fast (Optional[bool]): Prioritize speed over quality. Recaptcha V3 works by determining how human-like a client is, when set to `True`, tokens are returned faster but with a lower human score (0.3 or lower). The default value is false (better score).

                    tries (int): How many attempts until not receiving a 503 status code from Captchaly.
            """
            ...

    recaptcha_v3: __recaptcha_v3_spec

    class __geetest_spec(typing_extensions.Protocol):
        def __call__(self, /, url: str, captchaId: str, *, tries: int = 3) -> src.captchaly.model.Geetest:
            """Solve GeeTest and return the captcha token that to be submitted to the target website.
            Args:
                    url (str): The URL where the captcha is located on, or you can only just use the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example`

                    captchaId (str): The value of the `captcha_id` (or `captchaID`) parameter of the requests from the webpage to the Geetest server. For example: `e392e1d7fd421dc63325744d5a2b9c73`

                    tries (int): How many attempts until not receiving a 503 status code from Captchaly.
            """
            ...

        async def aio(self, /, url: str, captchaId: str, *, tries: int = 3) -> src.captchaly.model.Geetest:
            """Solve GeeTest and return the captcha token that to be submitted to the target website.
            Args:
                    url (str): The URL where the captcha is located on, or you can only just use the full domain name of the website (must include any subdomain). Captchaly will not try to access this URL therefore it will not be a problem if the captcha is behind some authentications. Examples: `https://www.example.com/examplepath`, `example.com`, `subdomain.example`

                    captchaId (str): The value of the `captcha_id` (or `captchaID`) parameter of the requests from the webpage to the Geetest server. For example: `e392e1d7fd421dc63325744d5a2b9c73`

                    tries (int): How many attempts until not receiving a 503 status code from Captchaly.
            """
            ...

    geetest: __geetest_spec
