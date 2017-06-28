import os
from typing import TypeVar, Type

import attr

T = TypeVar('T')


def _iter(cls, prefix, source):
    for field in attr.fields(cls):
        key = f'{prefix.upper()}_{field.name.upper()}'
        try:
            yield field.name, source[key]
        except KeyError:
            pass


def load(cls: Type[T], prefix: str, source=os.environ)  -> T:
    return cls(**dict(_iter(cls, prefix, source)))
