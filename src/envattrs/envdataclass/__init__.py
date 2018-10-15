import os
from typing import TypeVar, Type
import dataclasses

T = TypeVar("T")
SubAttrs = object()


def _iter(cls, prefix, source):
    value = None
    for field in dataclasses.fields(cls):
        sub = field.metadata.get(SubAttrs, None)
        key = f"{prefix.upper()}_{field.name.upper()}"
        if sub is None:
            try:
                value = source[key]
            except KeyError as e:
                continue
        else:
            value = load(sub, key, source)
        yield field.name, value


def load(cls: Type[T], prefix: str, source=os.environ) -> T:
    return cls(**dict(_iter(cls, prefix, source)))
