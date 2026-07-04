import pytest

from captchaly import CaptchalyClient, model
from tests.helpers import validate_dataclass


@pytest.mark.asyncio
async def test_init_client_from_env(monkeypatch):
	monkeypatch.setenv("CAPTCHALY_APIKEY", "test-api-key")
	async with CaptchalyClient():
		pass


@pytest.mark.asyncio
async def test_init_client_from_param(monkeypatch):
	monkeypatch.delenv("CAPTCHALY_APIKEY", raising=False)
	async with CaptchalyClient(apikey="test-api-key"):
		pass


@pytest.mark.asyncio
@pytest.mark.parametrize("apikey", [None, ""])
async def test_falsy_apikey(monkeypatch, apikey):
	monkeypatch.delenv("CAPTCHALY_APIKEY", raising=False)
	with pytest.raises(ValueError):
		async with CaptchalyClient(apikey):
			pass


@pytest.mark.asyncio
async def test_get_account():
	async with CaptchalyClient() as client:
		account = await client.account.aio()
		assert isinstance(account, model.Account)
		validate_dataclass(account)
