import pytest

from captchaly import CaptchalyClient, model
from tests.helpers import validate_dataclass


@pytest.mark.asyncio
async def test_recaptcha_v2():
	url = "demo.captchaly.com"
	sitekey = "6Le0FEMtAAAAAK9IgmSqaJfPb3E-9fI9xMp1nDfk"
	async with CaptchalyClient() as client:
		recaptcha = await client.recaptcha_v2.aio(url, sitekey)
		assert isinstance(recaptcha, model.Recaptcha)
		assert recaptcha.token
		validate_dataclass(recaptcha)


@pytest.mark.parametrize("fast", [True, False], ids=["fast=True", "fast=False"])
@pytest.mark.asyncio
async def test_recaptcha_v3(fast):
	url = "demo.captchaly.com"
	sitekey = "6LfPykItAAAAAD21EZu_BSQUUUVxnXrYEl3z8CwS"
	action = "submit"
	async with CaptchalyClient() as client:
		recaptcha = await client.recaptcha_v3.aio(url, sitekey, action, fast=fast)
		assert isinstance(recaptcha, model.Recaptcha)
		assert recaptcha.token
		validate_dataclass(recaptcha)
