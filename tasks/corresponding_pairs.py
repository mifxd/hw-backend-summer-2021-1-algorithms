from typing import TypeVar

__all__ = ("corresponding_pairs",)

T1 = TypeVar("T1")
T2 = TypeVar("T2")

def corresponding_pairs(arr1: list[T1], arr2: list[T2]) -> list[tuple[T1, T2]]:
    l = []
    if not arr1 or not arr2:
        return []

    min_len = min([len(arr1), len(arr2)])
    for n in range(min_len):
        l.append((arr1[n], arr2[n]))

    return l
