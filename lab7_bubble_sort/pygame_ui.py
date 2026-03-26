from __future__ import annotations

from dataclasses import dataclass

import pygame

from .sort_logic import SortStep, bubble_sort_steps


@dataclass(frozen=True, slots=True)
class VisualConfig:
    width: int = 1000
    height: int = 600
    padding: int = 40
    background: tuple[int, int, int] = (18, 18, 18)
    bar_color: tuple[int, int, int] = (94, 186, 255)
    compare_color: tuple[int, int, int] = (255, 132, 74)
    swap_color: tuple[int, int, int] = (84, 241, 162)
    text_color: tuple[int, int, int] = (230, 230, 230)


def run_pygame_visualization(
    values: list[int],
    *,
    delay_ms: int = 40,
    config: VisualConfig | None = None,
) -> None:
    """
    Visualize bubble sort with Pygame.

    Controls:
    - Space: pause/resume
    - q or Esc: quit
    """

    if delay_ms < 0:
        raise ValueError("delay_ms must be >= 0")
    if not values:
        raise ValueError("values must be non-empty")

    cfg = VisualConfig() if config is None else config

    pygame.init()
    try:
        screen = pygame.display.set_mode((cfg.width, cfg.height))
        pygame.display.set_caption("Bubble Sort Visualization")
        clock = pygame.time.Clock()
        font = pygame.font.SysFont(None, 20)

        paused = False
        current_step: SortStep | None = None
        steps_iter = iter(bubble_sort_steps(values))

        running = True
        done = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_ESCAPE, pygame.K_q):
                        running = False
                    elif event.key == pygame.K_SPACE:
                        paused = not paused

            if not paused:
                if not done:
                    try:
                        current_step = next(steps_iter)
                    except StopIteration:
                        current_step = None
                        done = True

            _draw_frame(screen, font, values, current_step, paused, delay_ms, cfg, done)
            pygame.display.flip()

            # Slow down; still keep the window responsive.
            if delay_ms > 0:
                pygame.time.delay(delay_ms)
            clock.tick(60)
    finally:
        pygame.quit()


def _draw_frame(
    screen: pygame.Surface,
    font: pygame.font.Font,
    values: list[int],
    step: SortStep | None,
    paused: bool,
    delay_ms: int,
    cfg: VisualConfig,
    done: bool,
) -> None:
    screen.fill(cfg.background)

    n = len(values)
    if n == 0:
        return

    max_val = max(values)
    if max_val <= 0:
        max_val = 1

    left = cfg.padding
    top = cfg.padding
    usable_w = cfg.width - 2 * cfg.padding
    usable_h = cfg.height - 2 * cfg.padding

    bar_w = max(1, usable_w // n)
    gap = 1

    hi_a = step.i if step is not None else None
    hi_b = step.j if step is not None else None
    hi_color = None
    if step is not None:
        if step.kind == "compare":
            hi_color = cfg.compare_color
        elif step.kind == "swap":
            # Two different colors for the two values being swapped.
            # We draw one as compare_color, the other as swap_color.
            hi_color = None

    for idx, v in enumerate(values):
        x = left + idx * bar_w
        h = int((v / max_val) * usable_h)
        y = top + (usable_h - h)

        color = cfg.bar_color
        if step is not None and idx in (hi_a, hi_b):
            if step.kind == "swap":
                color = cfg.compare_color if idx == hi_a else cfg.swap_color
            else:
                color = cfg.compare_color

        rect = pygame.Rect(x, y, bar_w - gap, h)
        pygame.draw.rect(screen, color, rect)

    if paused:
        status = "PAUSED"
    elif done:
        status = "DONE"
    else:
        status = step.kind.upper() if step is not None else "RUNNING"

    msg = f"{status}  (Space: pause, q/Esc: quit)  delay={delay_ms}ms"
    text = font.render(msg, True, cfg.text_color)
    screen.blit(text, (10, 10))
