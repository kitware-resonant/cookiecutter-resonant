from collections.abc import Generator
from contextlib import contextmanager
from typing import Any


# From https://stackoverflow.com/a/38532086
@contextmanager
def temporarily_change_attributes(something: object, **kwargs: Any) -> Generator[None]:
    previous_values = {k: getattr(something, k) for k in kwargs}
    for k, v in kwargs.items():
        setattr(something, k, v)
    try:
        yield
    finally:
        for k, v in previous_values.items():
            setattr(something, k, v)
