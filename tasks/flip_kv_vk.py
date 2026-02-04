from typing import TypeVar

__all__ = (
    "flip_kv_vk",
    "flip_kv_vk_safe",
)

KT = TypeVar("KT")
KV = TypeVar("KV")

def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    reserved = {v: k for k, v in d.items()}
    return reserved

def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    reserved = {}
    for k, v in d.items():
        if v not in reserved:
            reserved[v] = []
        reserved[v].append(k)
    return reserved
