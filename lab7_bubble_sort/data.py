from __future__ import annotations

import random


def make_random_list(
    size: int = 50,
    *,
    min_value: int = 5,
    max_value: int = 100,
    seed: int | None = None,
) -> list[int]:
    if size <= 0:
        raise ValueError("size must be > 0")
    if min_value >= max_value:
        raise ValueError("min_value must be < max_value")

    rng = random.Random(seed)
    return [rng.randint(min_value, max_value) for _ in range(size)]

