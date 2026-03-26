# Bubble Sort Visualization (Lab 7)

This project visualizes Bubble Sort with a simple Pygame animation.

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

```powershell
python -m lab7_bubble_sort.main
```

Optional flags:

```powershell
python -m lab7_bubble_sort.main --size 40 --delay-ms 40 --seed 123
```

## Controls

- `Space`: pause / resume
- `q` or `Esc`: quit

## Notes

- The sorting algorithm and the visualization UI are separated:
  - `lab7_bubble_sort/sort_logic.py`: pure bubble sort logic (yields steps)
  - `lab7_bubble_sort/pygame_ui.py`: rendering + input handling
