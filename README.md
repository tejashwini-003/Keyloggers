This Python script captures keyboard input and logs it to a file named log.txt. It uses the pynput library to listen to keyboard events and processes the input according to specific rules.

Features:
Key Logging: Captures and logs all key presses.
Special Key Handling: Ignores specific keys such as shift, control, alt, and others to avoid cluttering the log file.
Space and Enter Keys: Properly logs spaces and newlines.
Backspace Key: Represents the backspace key as an empty string to indicate deletion.
Caps Lock Tracking: Keeps track of the Caps Lock state to correctly log the case of letters.

Code Overview:
Listener Setup: The script sets up a listener for keyboard events using pynput.keyboard.Listener.
Key Handling: Special keys (e.g., shift, control, alt) are ignored, and space and enter keys are logged as their respective characters.
Caps Lock Handling: The script tracks the state of the Caps Lock key and adjusts the case of the letters accordingly.

There is also a list keycodes that can be used.
