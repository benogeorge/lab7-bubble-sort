from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Literal

StepKind = Literal["compare", "swap", "done"]


@dataclass(frozen=True, slots=True)
class SortStep:
    kind: StepKind
    values: tuple[int, ...]
    i: int | None = None
    j: int | None = None


def bubble_sort(values: Iterable[int]) -> list[int]:
    arr = list(values)
    for _ in bubble_sort_steps(arr):
        pass
    return arr


def bubble_sort_steps(values: list[int]) -> Iterable[SortStep]:
    """
    Yield bubble-sort steps for visualization.

    - Mutates the provided list *in place* (UI owns the list).
    - Yields:
      - compare(i, j) before each comparison
      - swap(i, j) after a swap
      - done at the end
    """

    n = len(values)
    if n <= 1:
        yield SortStep(kind="done", values=tuple(values))
        return

    # Standard bubble sort: after each outer pass, the largest element is at the end.
    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            j = i + 1
            yield SortStep(kind="compare", values=tuple(values), i=i, j=j)
            if values[i] > values[j]:
                values[i], values[j] = values[j], values[i]
                swapped = True
                yield SortStep(kind="swap", values=tuple(values), i=i, j=j)
        if not swapped:
            break

    yield SortStep(kind="done", values=tuple(values))

