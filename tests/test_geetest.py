import pytest

from captchaly import CaptchalyClient, model


@pytest.mark.asyncio
async def test_geetest():
	url = "2captcha.com"
	captchaId = "e392e1d7fd421dc63325744d5a2b9c73"
	async with CaptchalyClient() as client:
		geetest = await client.geetest.aio(url, captchaId)
		assert isinstance(geetest, model.Geetest)
		assert geetest.token
