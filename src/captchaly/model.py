from dataclasses import dataclass
from decimal import Decimal
from typing import TypedDict


@dataclass
class Account:
	"""User account information.

	Attributes:
		id (str): Unique account identifier.
		email (str): Account email address.
		balance (float): Current account balance.
		join_at (int): Unix timestamp of account creation.
	"""

	id: str
	email: str
	balance: float
	join_at: int


@dataclass
class Hcaptcha:
	"""
	HCaptcha token solution.

	Attributes:
		duration (float): How long until the token expires in seconds.
		time (float): Timestamp of when the token was generated.
		token (str): The captcha token to be submitted to the target website, commonly for `h-captcha-response` but not always.
		deducted (Decimal): Amount deducted from account balance.
	"""

	duration: float
	time: float
	token: str
	deducted: Decimal

	def __post_init__(self) -> None:
		self.deducted = Decimal(self.deducted)


@dataclass
class Turnstile:
	"""
	Cloudflare Turnstile token solution.

	Attributes:
		duration (float): How long until the token expires in seconds.
		time (float): Timestamp of when the token was generated.
		token (str): The captcha token to be submitted to the target website, commonly for `cf-turnstile-response` but not always.
		deducted (Decimal): Amount deducted from account balance.
	"""

	duration: float
	time: float
	token: str
	deducted: Decimal

	def __post_init__(self) -> None:
		self.deducted = Decimal(self.deducted)


@dataclass
class Recaptcha:
	"""
	Google reCAPTCHA token solution.

	Attributes:
		duration (float): How long until the token expires in seconds.
		time (float): Timestamp of when the token was generated.
		token (str): The captcha token to be submitted to the target website, commonly for `g-recaptcha-response` but not always.
		deducted (Decimal): Amount deducted from account balance.
	"""

	duration: float
	time: float
	token: str
	deducted: Decimal

	def __post_init__(self) -> None:
		self.deducted = Decimal(self.deducted)


class _GeetestToken(TypedDict):
	captcha_id: str
	lot_number: str
	pass_token: str
	gen_time: str
	captcha_output: str


@dataclass
class Geetest:
	"""
	Geetest CAPTCHA token solution.

	Attributes:
		duration (float): How long until the token expires in seconds.
		time (float): Timestamp of when the token was generated.
		token (_GeetestToken): The captcha object to be submitted to the target website.
		deducted (Decimal): Amount deducted from account balance.
	"""

	duration: float
	time: float
	token: _GeetestToken
	deducted: Decimal

	def __post_init__(self) -> None:
		self.deducted = Decimal(self.deducted)
