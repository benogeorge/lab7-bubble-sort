"""Bubble sort learning scaffold.

This file is intentionally incomplete. It gives you the structure for a
simple bubble sort program and leaves the important steps as TODOs so you
can fill them in while learning.
"""


def bubble_sort(numbers: list[int]) -> list[int]:
    """Sort a list of integers using bubble sort.

    TODO:
    - Loop over the list multiple times.
    - Compare neighboring values.
    - Swap them when the left value is larger than the right value.
    - Stop early if a full pass makes no swaps.
    """
    # Make a copy so the original list is not modified.
    sorted_numbers = numbers[:]

    # TODO: Write the outer loop for repeated passes.
    # TODO: Write the inner loop that compares neighbors.
    # TODO: Swap out-of-order values.
    # TODO: Track whether a pass made any swaps.

    return sorted_numbers


def main() -> None:
    """Run a small demo of the bubble sort scaffold."""
    sample_numbers = [5, 1, 4, 2, 8]

    print("Before sorting:", sample_numbers)
    # TODO: Replace the scaffold with a real bubble sort implementation.
    result = bubble_sort(sample_numbers)
    print("After sorting: ", result)


if __name__ == "__main__":
    main()
