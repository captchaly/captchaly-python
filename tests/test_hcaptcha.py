import pytest

from captchaly import CaptchalyClient, model
from tests.helpers import validate_dataclass


@pytest.mark.asyncio
async def test_hcaptcha():
	url = "hcaptcha.pythonanywhere.com"
	sitekey = "87bd4111-b2d5-4f31-86c0-4a944f0d3b24"
	async with CaptchalyClient() as client:
		hcaptcha = await client.hcaptcha.aio(url, sitekey)
		assert isinstance(hcaptcha, model.Hcaptcha)
		assert hcaptcha.token
		validate_dataclass(hcaptcha)


@pytest.mark.asyncio
async def test_hcaptcha_enterprise():
	url = "sso.acesso.gov.br"
	sitekey = "93b08d40-d46c-400a-ba07-6f91cda815b9"
	async with CaptchalyClient() as client:
		hcaptcha = await client.hcaptcha_enterprise.aio(url, sitekey)
		assert isinstance(hcaptcha, model.Hcaptcha)
		assert hcaptcha.token
		validate_dataclass(hcaptcha)


# TODO: test hcaptcha enterprise rqdata
