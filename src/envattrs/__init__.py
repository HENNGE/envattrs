import os
from typing import TypeVar, Type

try:
    import attr
except ImportError:
    try:
        import dataclasses
    except ImportError:
        print("Neither dataclasses not attr libraries available")
        print("Make sure you are using either one and install that module")


T = TypeVar("T")

SubAttrs = object()


def _iter(cls, prefix, source):
    # Check if it is an attr class or dataclass
    # and use the corresponding fields function
    if attr.has(cls):
        fields = attr.fields
    elif dataclasses.is_dataclass(cls):
        fields = dataclasses.fields
    else:
        print("Object is neither dataclass nor attr class")
        return

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
