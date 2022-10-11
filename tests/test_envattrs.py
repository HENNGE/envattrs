import attr
import pytest

import envattrs
from envattrs import converters


def test_load():
    @attr.s
    class Foo:
        bar = attr.ib()

    instance = envattrs.load(Foo, "FOO", {"FOO_BAR": "baz"})
    assert instance.bar == "baz"


def test_load_fail():
    @attr.s
    class Foo:
        bar = attr.ib()

    with pytest.raises(TypeError):
        envattrs.load(Foo, "BAR", {"FOO_BAR": "baz"})


def test_load_with_leading_underscore():
    @attr.s
    class Foo:
        _bar = attr.ib()

    instance = envattrs.load(Foo, "FOO", {"FOO_BAR": "baz"})
    assert instance._bar == "baz"


def test_load_with_non_leading_underscore():
    @attr.s
    class Foo:
        bar_check = attr.ib()

    instance = envattrs.load(Foo, "FOO", {"FOO_BAR_CHECK": "baz"})
    assert instance.bar_check == "baz"


def test_converters():
    @attr.s
    class Foo:
        flag = attr.ib(converter=converters.boolean())
        sequence = attr.ib(converter=converters.sequence())
        mapping = attr.ib(converter=converters.mapping())

    instance = envattrs.load(
        Foo,
        "FOO",
        {
            "FOO_FLAG": "true",
            "FOO_SEQUENCE": "first second",
            "FOO_MAPPING": "key1=value1 key2=value2",
        },
    )
    assert instance.flag
    assert instance.sequence == ["first", "second"]
    assert instance.mapping == {"key1": "value1", "key2": "value2"}


def test_nested():
    @attr.s
    class Sub:
        value = attr.ib()

    @attr.s
    class Main:
        sub = attr.ib(metadata={envattrs.SubAttrs: Sub})

    instance = envattrs.load(Main, "TEST", {"TEST_SUB_VALUE": "foo"})
    assert instance.sub.value == "foo"
