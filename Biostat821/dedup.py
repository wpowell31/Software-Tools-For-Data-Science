"""Deduplication."""
from typing import TypeVar

T = TypeVar("T")


def is_in(things: list[T], target: T) -> bool:
    """Determine whether target is in things.

    O(N) total
    """
    for thing in things:  # N times
        if thing == target:  # O(1)
            return True  # O(1)
    return False  # O(1)


def dedup(things: list[T]) -> list[T]:
    """De-duplicate things.

    O(N**2) total
    """
    unique_things: list[T] = []  # O(1)
    for thing in things:  # N times
        if not is_in(unique_things, thing):  # O(N)
            unique_things.append(thing)  # O(1)
    return unique_things  # O(1)
