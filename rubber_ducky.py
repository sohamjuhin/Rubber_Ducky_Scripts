import time
import keyboard

# Delay between keystrokes (in seconds)
DELAY = 0.1

# Function to emulate Rubber Ducky keystrokes
def type_keystrokes(keystrokes):
    time.sleep(2)  # Delay before starting

    for keystroke in keystrokes:
        if keystroke.startswith("DELAY"):
            delay = float(keystroke.split(" ")[1])
            time.sleep(delay)
        else:
            keyboard.write(keystroke)
            time.sleep(DELAY)

# Usage example
keystrokes = [
    "Hello, world!",
    "DELAY 1",
    "This is a test",
    "ENTER"
]

type_keystrokes(keystrokes)
