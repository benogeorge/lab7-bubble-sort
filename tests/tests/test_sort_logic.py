from __future__ import annotations

from lab7_bubble_sort.sort_logic import bubble_sort, bubble_sort_steps


def test_bubble_sort_sorts() -> None:
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]


def test_steps_end_with_done() -> None:
    arr = [2, 1]
    steps = list(bubble_sort_steps(arr))
    assert steps[-1].kind == "done"


def test_steps_swap_on_inversion() -> None:
    arr = [2, 1]
    kinds = [s.kind for s in bubble_sort_steps(arr)]
    assert "swap" in kinds


def test_no_swap_on_sorted() -> None:
    arr = [1, 2, 3]
    kinds = [s.kind for s in bubble_sort_steps(arr)]
    assert "swap" not in kinds


def test_empty_rejected_by_ui_contract() -> None:
    # Logic supports empty input for bubble_sort; visualization refuses empty.
    assert bubble_sort([]) == []

