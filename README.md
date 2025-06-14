![KeyScope](/logo.png)

**KeyScope** is a cross-platform, self-installing keystroke logger with active window tracking, developed as part of a Cybersecurity Internship project. It is designed exclusively for use in authorized lab environments to study user behavior, test keylogging detection systems, and simulate adversarial techniques for defense and detection research.



## DISCLAIMER

**This project is for EDUCATIONAL and RESEARCH PURPOSES ONLY.**

Unauthorized use of this tool on systems or networks without explicit written permission is strictly prohibited and may violate local, national, or international laws.



## Features

- Self-installs required Python packages on first run
- Cross-platform compatibility (Windows, macOS, Linux)
- Captures and logs keystrokes with timestamps
- Tracks and logs the active application/window title
- Saves logs in a platform-aware location (user home directory)
- Designed for cybersecurity labs and red team simulation environments



## Requirements

While the script auto-installs its dependencies, the following are used:

- `keyboard` — for capturing keystrokes
- `psutil` — for process-related metadata
- `pygetwindow` — to retrieve active window titles (Windows only)
- `pyobjc-framework-Quartz` — macOS active application support
- Python 3.6 or higher
- Internet access for first-time dependency installation (if packages not present)



## Usage

To execute the script:

```bash
python keyscope.py
```

Log file will be created at:

- **Windows**: `C:\Users\<Username>\keylog.txt`
- **macOS/Linux**: `~/keylog.txt`

No console output will be shown during execution.



## File Structure

```
KeyScope/
├── keyscope.py         # Main keylogger script
├── README.md           # Project documentation
├── LICENSE.md         # Legal and ethical use terms
├── requirements.txt    # Dependencies (reference only)
├── sample_keylog.txt    # Sample Keylog File
└── logo.png          # Logo
```



## Customization Ideas

- Add log rotation (by size or date)
- Encrypt or compress log files for secure handling
- Create a startup script for testing persistence in lab
- Integrate email alerting or exfiltration simulation (lab only)
- Bundle with PyInstaller for portable binary execution



## Note

This script was developed by an intern as part of a structured cybersecurity internship program focused on ethical red team tooling and behavioral simulation in safe, sandboxed environments.

Use of this software must align with applicable laws, institutional policies, and ethical guidelines.


## License

See `LICENSE.md` for permitted and restricted uses.