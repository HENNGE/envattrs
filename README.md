# envattrs

Populate an `attr.s` class from environment variables.

## Usage


```python

import attr
import envattrs


@attr.s
class Options:
    port = attr.ib(convert=int)


options = envattrs.load(Options, 'PREFIX')  # Sets port to PREFIX_PORT env variable
```

## Sub objects

New in 1.1.0

```python

import attr
import envattrs


@attr.s
class ServerOptions:
    port = attr.ib(convert=int)


@attr.s
class AppOptions:
    name = attr.ib()


@attr.s
class Options:
    server = attr.ib(metadata={envattrs.SubAttrs: ServerOptions})
    app = attr.ib(metadata={envattrs.SubAttrs: AppOptions})


# ServerOptions.port is loaded from PREFIX_SERVER_PORT
# AppOptions.name is loaded from PREFIX_APP_NAME
options = envattrs.load(Options, 'PREFIX')
```


## Built in converter factories


* `envattrs.converters.boolean(truthy_values={'on', '1', 'true'})`
* `envattrs.converters.sequence(delimiter=' ')`
* `envattrs.converters.mapping(item_delimiter=' ', value_delimiter='=')`


## Changelog

### 1.1.0

Released: 2018-01-10

* Added support for nested objects.

### 1.0.0

Relased: 2017-06-28

* Initial release
