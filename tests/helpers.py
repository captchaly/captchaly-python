from dataclasses import fields
from typing import get_type_hints


def validate_dataclass(obj: object) -> None:
	hints = get_type_hints(type(obj))

	for field in fields(obj):  # type: ignore
		expected = hints[field.name]
		value = getattr(obj, field.name)
		assert isinstance(value, expected)
