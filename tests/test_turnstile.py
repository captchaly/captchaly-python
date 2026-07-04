import pytest

from captchaly import CaptchalyClient, model
from tests.helpers import validate_dataclass

URL = "demo.captchaly.com"
SITEKEY = "0x4AAAAAAA4nzhwwpeesSPI2"


@pytest.mark.asyncio
async def test_turnstile():
	async with CaptchalyClient() as client:
		turnstile = await client.turnstile.aio(URL, SITEKEY)
		assert isinstance(turnstile, model.Turnstile)
		assert turnstile.token
		validate_dataclass(turnstile)


@pytest.mark.asyncio
async def test_turnstile_action():
	action = "my-very-own-action"
	async with CaptchalyClient() as client:
		turnstile = await client.turnstile.aio(URL, SITEKEY, action=action)
		assert isinstance(turnstile, model.Turnstile)
		assert turnstile.token
		validate_dataclass(turnstile)


@pytest.mark.asyncio
async def test_browser_token_cdata():
	cdata = "my-very-own-customer-data"
	async with CaptchalyClient() as client:
		turnstile = await client.turnstile.aio(URL, SITEKEY, cdata=cdata)
		assert isinstance(turnstile, model.Turnstile)
		assert turnstile.token
		validate_dataclass(turnstile)
