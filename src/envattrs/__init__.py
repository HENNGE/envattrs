import os
from typing import TypeVar, Type

import attr

T = TypeVar('T')

SubAttrs = object()


def _iter(cls, prefix, source):
    for field in attr.fields(cls):
        sub = field.metadata.get(SubAttrs, None)
        key = f'{prefix.upper()}_{field.name.upper()}'
        if sub is None:
            try:
                value = source[key]
            except KeyError:
                continue
        else:
            value = load(sub, key, source)
        yield field.name, value


def load(cls: Type[T], prefix: str, source=os.environ) -> T:
    return cls(**dict(_iter(cls, prefix, source)))
