# Bubble Sort Visualization (Lab 7)

This project visualizes Bubble Sort in two ways:

- Terminal animation (in-place redraw)
- Pygame 2D bars animation (swap highlights in two colors)

## Setup

Create and activate a virtual environment, then install dependencies:

```powershell
# Use Python 3.12 (pygame wheels are available). If `py` defaults to 3.14 on your machine,
# forcing 3.12 avoids a source build.
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run

Recommended:

```powershell
python .\main.py --renderer pygame --size 40 --delay-ms 40 --seed 123
```

Terminal renderer:

```powershell
python .\main.py --renderer terminal --size 40 --delay-ms 40 --seed 123
```

## Controls (Pygame)

- `Space`: pause / resume
- `q` or `Esc`: quit

## Notes

- Separation of concerns:
  - `lab7_bubble_sort/sort_logic.py`: bubble sort logic (yields steps)
  - `lab7_bubble_sort/terminal_ui.py`: terminal in-place redraw visualization
  - `lab7_bubble_sort/pygame_ui.py`: Pygame visualization
