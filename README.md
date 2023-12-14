# Window Activity Tracker

This Python script tracks the active window's title, counts keypresses, and mouse clicks.

## Instructions

### Prerequisites
- Python 3.x installed
- Required libraries installed:
  - `pygetwindow`
  - `pynput`

### Installation
1. Clone this repository.
2. Install the required Python libraries:



### Usage
1. Import the `track_active_window` function from `tracker.py`.
2. Execute `track_active_window()` to start monitoring.
3. The function continuously displays the active window's title and counts keypresses and mouse clicks.
4. Stop the monitoring by pressing `Ctrl + C`.

### Example
```python
from tracker import track_active_window

if __name__ == "__main__":
 track_active_window()
