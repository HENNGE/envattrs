import os
from typing import TypeVar, Type

try:
    import attr
except ImportError:
    attr = None
try:
    import dataclasses
except ImportError:
    dataclasses = None

T = TypeVar("T")

SubAttrs = object()


def _iter(cls, prefix, source):
    # Check if it is an attr class or dataclass
    # and use the corresponding fields function
    if attr is not None and attr.has(cls):
        fields = attr.fields
    elif dataclasses is not None and dataclasses.is_dataclass(cls):
        fields = dataclasses.fields
    else:
        raise TypeError("Object is neither dataclass nor attr class")

    for field in fields(cls):
        sub = field.metadata.get(SubAttrs, None)
        key = f"{prefix.upper()}_{field.name.upper()}"
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
