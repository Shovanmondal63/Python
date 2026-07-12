# 🎯 Guess The Number — CLI Python Game

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Shovanmondal63/Python/tree/main/py-guess-the-number)

An interactive, retro-styled Command Line Interface (CLI) number guessing game written in Python. Players can define their own mathematical playground by configuring the custom minimum and maximum ranges. The game tracks performance and awards custom gamer ranks based on how efficiently the secret number is cracked!

---

## ✨ Features

* **Retro ASCII Art Banner:** A stylized welcome screen that gives the game an arcade-like vibe.
* **Dynamic Range Setup:** Total freedom to set your own boundaries (e.g., 1 to 10, or 1 to 10,000).
* **Crash-Proof Input Validation:** Built-in error handling ensures that accidental letters, symbols, or invalid ranges won't crash the executable.
* **Intelligent Hints:** Real-time visual tracking (`📈 TOO HIGH!` / `📉 TOO LOW!`) to guide your next move.
* **Gamified Ranking System:** Earn distinct titles based on your performance:
    * 🥇 **GODLIKE GUESSER!** (1-3 attempts)
    * 🥈 **SHARPSHOOTER!** (4-7 attempts)
    * 🐢 **SLOW & STEADY!** (8+ attempts)

---

## 🛠️ Installation & Prerequisites

To run this project locally, you need to have **Python** installed on your system. 

### 1. Installing Python

#### 🪟 Windows:
1. Download the latest installer from the official [Python Downloads page](https://www.python.org/downloads/).
2. Run the installer executable.
3. **CRITICAL:** Check the box that says **"Add Python.exe to PATH"** at the bottom of the installation wizard before proceeding.
4. Click **Install Now**.

#### 🍏 macOS:
Python usually comes pre-installed on macOS, but to ensure you have the latest version:
1. Open your Terminal and install Homebrew (if you don't have it) by pasting:
   ```bash
   /bin/bash -c "$(curl -fsSL [https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh](https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh))"
