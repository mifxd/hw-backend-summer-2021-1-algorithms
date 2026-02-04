import re
__all__ = ("find_shortest_longest_word",)


def find_shortest_longest_word(text: str) -> tuple[str, str] | tuple[None, None]:
    words = re.findall(r'\S+', text)
    if not words:
        return None, None

    shortest = min(words, key=len)
    longest = max(words, key=len)

    return shortest, longest
