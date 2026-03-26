from __future__ import annotations

import os
import sys
import time

from .sort_logic import SortStep, bubble_sort_steps


def run_terminal_visualization(values: list[int], *, delay_ms: int = 40) -> None:
    """Terminal visualization using in-place redraw.

    This is intentionally lightweight (no extra deps). Quit with Ctrl+C.
    """

    if delay_ms < 0:
        raise ValueError("delay_ms must be >= 0")
    if not values:
        raise ValueError("values must be non-empty")

    steps = iter(bubble_sort_steps(values))

    try:
        while True:
            try:
                step = next(steps)
            except StopIteration:
                step = None

            _clear_screen()
            print(_format_bars(values, step))

            if step is None or step.kind == "done":
                print("\nDone. (Ctrl+C to exit)")
                time.sleep(999999)

            if delay_ms:
                time.sleep(delay_ms / 1000.0)
    except KeyboardInterrupt:
        return


def _clear_screen() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        sys.stdout.write("\x1b[2J\x1b[H")
        sys.stdout.flush()


def _format_bars(values: list[int], step: SortStep | None) -> str:
    max_val = max(values) if values else 1
    max_val = max(1, max_val)

    hi_a = step.i if step is not None else None
    hi_b = step.j if step is not None else None

    header = "TERMINAL (done)" if step is None else f"TERMINAL ({step.kind})  highlight: A={hi_a} B={hi_b}"

    lines: list[str] = [header, ""]
    for idx, v in enumerate(values):
        bar_len = int((v / max_val) * 50)
        bar = "#" * max(1, bar_len)

        prefix = "  "
        if idx == hi_a:
            prefix = "A "
        elif idx == hi_b:
            prefix = "B "

        lines.append(f"{prefix}{idx:02d} {bar} ({v})")

    return "\n".join(lines)
