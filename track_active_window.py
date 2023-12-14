
# pip install pygetwindow pynput

import time
import pygetwindow as gw
from pynput import keyboard, mouse

def on_key_press(key):
    track_active_window.keypress_count += 1

def on_click(x, y, button, pressed):
    track_active_window.mouse_click_count += 1

def track_active_window():
    prev_window_title = None

    track_active_window.keypress_count = 0
    track_active_window.mouse_click_count = 0

    # Keyboard listener
    keyboard_listener = keyboard.Listener(on_press=on_key_press)
    keyboard_listener.start()

    # Mouse listener
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()

    try:
        while True:
            active_window = gw.getActiveWindow()

            if active_window and active_window.title != prev_window_title:
                print(f"Active Window Title: {active_window.title}")
                print(f"Keypress Count: {track_active_window.keypress_count}")
                print(f"Mouse Click Count: {track_active_window.mouse_click_count}")
                prev_window_title = active_window.title
                track_active_window.keypress_count = 0
                track_active_window.mouse_click_count = 0
            
            time.sleep(1)  

    except KeyboardInterrupt:  
        pass

    finally:
        keyboard_listener.stop()
        mouse_listener.stop()

if __name__ == "__main__":
    track_active_window()
