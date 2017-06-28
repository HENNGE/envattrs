def boolean(truthy_values={'1', 'on', 'true'}):
    def converter(value):
        return value.lower() in truthy_values
    return converter


def sequence(delimiter=' '):
    def converter(value):
        return value.split(' ')
    return converter


def mapping(item_delimiter=' ', value_delimiter='='):
    sequencer = sequence(item_delimiter)

    def converter(value):
        return dict(item.split(value_delimiter, 1) for item in sequencer(value))

    return converter
