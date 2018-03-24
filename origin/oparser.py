class ParserError(Exception):
    pass


def parse(command, obj):
    try:
        return getattr(obj, command)
    except AttributeError:
        return "err"
