import re

RE_D = re.compile("\d")

def contains_number(string: str) -> bool:
    """Decides if string contains any number."""

    return RE_D.search(string)