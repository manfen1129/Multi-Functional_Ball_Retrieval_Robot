from pynput import keyboard
import time
import serial.tools.list_ports
import str_processing as sp

portNames = ["/dev/ttyACM0", "/dev/ttyUSB0"]
baudRate = 9600
timeOut = 100
# Arduino = serial.Serial(portName, baudRate, timeout=timeOut)
Arduino1 = serial.Serial(portNames[0], baudRate, timeout=timeOut)
Arduino2 = serial.Serial(portNames[1], baudRate, timeout=timeOut)
pressed_keys = set()


def on_press(key):
    try:
        if key.char:
            pressed_keys.add(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            pressed_keys.add("space")
        elif key == keyboard.Key.backspace:
            pressed_keys.add("backspace")
        elif key == keyboard.Key.enter:
            pressed_keys.add("enter")
        elif key == keyboard.Key.esc:
            pressed_keys.add("esc")

def on_release(key):
    try:
        if key.char and key.char in pressed_keys:
            pressed_keys.remove(key.char)
    except AttributeError:
        if key == keyboard.Key.space and "space" in pressed_keys:
            pressed_keys.remove("space")
        elif key == keyboard.Key.backspace and "backspace" in pressed_keys:
            pressed_keys.remove("backspace")
        elif key == keyboard.Key.enter and "enter" in pressed_keys:
            pressed_keys.remove("enter")
        elif key == keyboard.Key.esc and "esc" in pressed_keys:
            pressed_keys.remove("esc")


def main():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    while True:
        # Make a copy of the pressed_keys to avoid modification during iteration
        current_keys = pressed_keys.copy()
        print("Pressed keys:", current_keys)
        DC_keys_str, serve_keys_str = sp.set2str(current_keys)
        Arduino1.write(DC_keys_str.encode("ascii"))
        Arduino2.write(serve_keys_str.encode("ascii"))
        print("DC keys string:", DC_keys_str)
        print("Serve keys string:", serve_keys_str)
        # Arduino.write(DC_keys_str.encode("ascii"))
        time.sleep(0.0001)


if __name__ == "__main__":
    main()
