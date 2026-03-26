from __future__ import annotations

import argparse

from .data import make_random_list
from .pygame_ui import run_pygame_visualization
from .terminal_ui import run_terminal_visualization


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Bubble Sort Visualization (Lab 7).")
    p.add_argument("--renderer", choices=["pygame", "terminal"], default="pygame")
    p.add_argument("--size", type=int, default=50, help="Number of values to sort.")
    p.add_argument("--delay-ms", type=int, default=40, help="Delay between steps/frames in milliseconds.")
    p.add_argument("--seed", type=int, default=None, help="Random seed (for reproducible runs).")
    return p.parse_args()


def main() -> None:
    args = _parse_args()
    values = make_random_list(size=args.size, seed=args.seed)

    if args.renderer == "terminal":
        run_terminal_visualization(values, delay_ms=args.delay_ms)
    else:
        run_pygame_visualization(values, delay_ms=args.delay_ms)


if __name__ == "__main__":
    main()
