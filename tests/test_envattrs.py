import attr
import pytest

import envattrs
from envattrs import converters


def test_load():
    @attr.s
    class Foo:
        bar = attr.ib()

    instance = envattrs.load(Foo, 'FOO', {'FOO_BAR': 'baz'})
    assert instance.bar == 'baz'


def test_load_fail():
    @attr.s
    class Foo:
        bar = attr.ib()

    with pytest.raises(TypeError):
        envattrs.load(Foo, 'BAR', {'FOO_BAR': 'baz'})


def test_converters():
    @attr.s
    class Foo:
        flag = attr.ib(convert=converters.boolean())
        sequence = attr.ib(convert=converters.sequence())
        mapping = attr.ib(convert=converters.mapping())

    instance = envattrs.load(Foo, 'FOO', {
        'FOO_FLAG': 'true',
        'FOO_SEQUENCE': 'first second',
        'FOO_MAPPING': 'key1=value1 key2=value2',
    })
    assert instance.flag
    assert instance.sequence == ['first', 'second']
    assert instance.mapping == {
        'key1': 'value1',
        'key2': 'value2',
    }
