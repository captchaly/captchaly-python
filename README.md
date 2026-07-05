[![Test](https://github.com/captchaly/captchaly-python/actions/workflows/test.yaml/badge.svg)](https://github.com/captchaly/captchaly-python/actions/workflows/test.yaml)

# Captchaly Python SDK

Official Python SDK for [Captchaly.com](https://captchaly.com).

Captchaly is the most advanced captcha solving service for enterprises. Providing large-scale automation and data scraping. Allow AI agents to bypass captchas and access the web without human intervention. Try for free at [https://captchaly.com](https://captchaly.com).

## Features

- Support both sync and async usage.
- Fully typed.
- Automatic retry.

## Requirements

This SDK is tested with Python 3.14. It may work with earlier versions, but it is not guaranteed.

## Installation

```bash
pip install captchaly
```

## Authentication

Provide your API key in either of these ways:

1. Pass it to the client constructor
```python
from captchaly import CaptchalyClient

CaptchalyClient("your_api_key")
```
2. Set the environment variable `CAPTCHALY_APIKEY` and the client will read it automatically.


## Quick Start

### Synchronous usage

```python
from captchaly import CaptchalyClient

url = "demo.captchaly.com"
sitekey = "6Le0FEMtAAAAAK9IgmSqaJfPb3E-9fI9xMp1nDfk"

with CaptchalyClient("your_api_key") as client:
	account = client.account()
	print(account.email, account.balance)

	recaptcha = client.recaptcha_v2(url, sitekey)
	print(recaptcha.token)
```

### Asynchronous usage

In async code, use async keywords (`await`, `async with`, `async for`, ...) and call the `.aio(...)` variant of each method.

```python
import asyncio
from captchaly import CaptchalyClient

url = "demo.captchaly.com"
sitekey = "0x4AAAAAAA4nzhwwpeesSPI2"

async def main():
	async with CaptchalyClient("your_api_key") as client:
		account = await client.account.aio()
		print(account.email, account.balance)

		turnstile = await client.turnstile.aio(url, sitekey)
		print(turnstile.token)
```

## TODO / Roadmap

- [ ] Playwright integration
- [ ] Puppeteer integration

## Contributing
This repository does not normally accept merge requests. You are welcome to open issues and requests for new features.


## License
MIT License. See [LICENSE](LICENSE) for details.
