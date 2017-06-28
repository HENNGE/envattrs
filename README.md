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


## Built in converter factories


* `envattrs.converters.boolean(truthy_values={'on', '1', 'true'})`
* `envattrs.converters.sequence(delimiter=' ')`
* `envattrs.converters.mapping(item_delimiter=' ', value_delimiter='=')`
