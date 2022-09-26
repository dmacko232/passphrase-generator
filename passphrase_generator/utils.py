import re

RE_D = re.compile("\d")

def contains_number(string: str) -> bool:

    return RE_D.search(string)