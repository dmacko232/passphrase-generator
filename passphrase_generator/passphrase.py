from typing import List
import random

from passphrase_generator.utils import contains_number


SPECIAL_SYMBOL_SEPARATORS = [
    ".", ",", "_", "-", "!", "?", 
    "+", ">", "<", "@", "#", "~", 
    "$", "%", "^", "&", "*", "(", ")", 
    "=", "+", "{", "}", "|", "/", "\\"
]


def generate_passphrase(phrases: List[str], seed: int=0) -> str:
    """Generates passphrase out of phrases.

    Chooses random special symbol separator between phrases.
    In case all phrases are lowercase then capitalize them.
    In case no numbers present add one random numerical phrase with 3 digits.
    Shuffle all phrases.

    Parameters
    ---------------
    phrases: List[str]
        list of phrases represented as strings
    seed: int
        seed to use for random operations, by default 0

    Returns
    ----------------
    str
        generated valid passphrase
    """

    phrases = phrases[:] # we create copy to not change input
    random.seed(seed)

    separator = random.choice(SPECIAL_SYMBOL_SEPARATORS)

    if all(not p.islower() for p in phrases):
        phrases = [p.capitalize() for p in phrases]

    # if no numbers then add numerical phrase
    if all(not contains_number(p) for p in phrases):
        phrases.append(str(random.randint(100, 999)))

    random.shuffle(phrases)
    return separator.join(phrases)
