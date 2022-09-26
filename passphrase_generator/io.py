from typing import List

def read_phrases(input_message: str, min_phrases: int=3, min_phrase_len: int=2) -> List[str]:

    loop = True
    while loop:
        read_line = input(f"{input_message}\n")
        phrases = read_line.split()
        loop = False
        if len(phrases) < min_phrases:
            print(f"Atleast {min_phrases} phrases (words) need to be specified.")
            loop = True
        if len(list(filter(lambda p: len(p) < min_phrase_len, phrases))):
            print(f"Each phrase (word) must be atleast {min_phrase_len} long.")
            loop = True
    return phrases




