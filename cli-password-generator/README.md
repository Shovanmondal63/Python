# 🔐 CLI Password Generator

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Terminal](https://img.shields.io/badge/Interface-CLI-lightgrey.svg?logo=gnometerminal)

A simple, interactive, and secure Command-Line Interface (CLI) password generator written in Python. Quickly generate strong, customizable passwords right from your terminal!

---

## ✨ Features

- **Customizable Length:** Choose exactly how long you want your password to be (enforces a minimum of 8 characters for security).
- **Flexible Character Sets:** Mix and match your requirements:
  - `[a-z, A-Z]` Letters
  - `[0-9]` Numbers
  - `[!@#$...]` Symbols
- **Interactive Prompts:** Simple `y/n` questions to guide you through creating your perfect password.
- **Input Validation:** Prevents crashes and ensures you select at least one character type.
- **Retro ASCII Art:** Starts up with a clean, classic hacker-style banner.

---

## 🚀 Getting Started

### Prerequisites

All you need is **Python 3.x** installed on your system. No external libraries or dependencies are required!

### Installation

1. Clone this repository to your local machine:
   ```bash
   https://github.com/Shovanmondal63/Python/blob/main/cli-password-generator/password_generator.py
   ```
2. Navigate into the project directory:
   ```bash
   cd cli-password-generator
   ```

---

## 💻 Usage

Run the script directly from your terminal:

```bash
python main.py
```
*(Note: Depending on your system, you might need to use `python3 main.py`)*

### 🎮 Example Interaction

```text
==================================================================
  _____            _____  _____ __          __ ____  _____  _____  
 |  __ \   /\     / ____|/ ____|\ \        / // __ \|  __ \|  __ \ 
 | |__) | /  \   | (___ | (___   \ \  /\  / /| |  | | |__) | |  | |
 |  ___/ / /\ \   \___ \ \___ \   \ \/  \/ / | |  | |  _  /| |  | |
 | |    / ____ \ ____) |____) |    \  /\  /  | |__| | | \ \| |__| |
 |_|   /_/    \_\_____/|_____/      \/  \/    \____/|_|  \_\_____/ 
==================================================================

[?] Enter your password length (min 8): 16

--- Character Selection ---
[?] Input letters? (y/n): y
[?] Input numbers? (y/n): y
[?] Input symbols? (y/n): y

************************************************
  GENERATED PASSWORD :  v7#K9p@Lm2!qR8z$
************************************************
```

---

## 🛠️ Potential Future Improvements

If you're looking to fork and expand this project, here are some ideas:
- [ ] Upgrade `random` to `secrets` module for cryptographic strength.
- [ ] Add an option to copy the generated password straight to the clipboard.
- [ ] Add command-line arguments (e.g., `python main.py -l 16 -n -s`) to bypass the interactive prompts.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 
Feel free to check out the [issues page](https://github.com/Shovanmondal63/cli-password-generator/issues) if you want to contribute.


