# Spin-Bot

**SpinBot** is an automated script designed to perform repetitive spinning actions in a video game. It uses image recognition to detect specific in-game elements and can be customized to stop spinning based on user-defined criteria.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automated spinning based on image recognition.
- Customizable stop conditions based on in-game rarities.
- Easy setup and configuration via a guided setup script.
- Cross-platform support with Python.

## Prerequisites

Before you can use SpinBot, you'll need to install the following:

1. **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
   - Ensure that Python is added to your system's PATH during installation.
   
2. **Tesseract-OCR**: An open-source OCR (Optical Character Recognition) engine.
   - [Download Tesseract-OCR](https://github.com/tesseract-ocr/tesseract)
   - **Windows**: Install the latest version and note the installation path. It’s typically `C:\Program Files\Tesseract-OCR\tesseract.exe`.
   - **macOS**: Install using Homebrew with `brew install tesseract`.
   - **Linux**: Install using your package manager, e.g., `sudo apt-get install tesseract-ocr`.

## Installation

### 1. Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/Sino1507/Spin-Bot.git
cd Spin-Bot
```

### 2. Install Required Python Packages

For convenience, an `install.bat` file is provided to install all necessary Python packages. Simply double-click the `install.bat` file, or run the following command in your terminal:

```bash
install.bat
```

Alternatively, you can manually install the packages using:

```bash
pip install -r requirements.txt
```

### 3. Install Tesseract-OCR

If you haven't already, install Tesseract-OCR by following the [instructions here](#prerequisites).

## Setup

### 1. Run the Setup Script

To configure SpinBot, run the `setup.py` script:

```bash
python setup.py
```

The script will guide you through:

- Setting the path to the Tesseract-OCR executable.
- Selecting the region of the screen where the in-game spinning occurs.
- Providing paths to images for the "Spin" and "ReSpin" buttons.
- Specifying the rarities at which SpinBot should stop spinning.

### 2. Capture Images

Ensure that you've captured images of the "Spin" and "ReSpin" buttons in your game. Save these images on your computer and provide their paths during the setup process.

## Usage

Once you’ve completed the setup:

1. **Run SpinBot**:
   - Simply run `main.py` to start the automated spinning process:
     ```bash
     python main.py
     ```
   - SpinBot will perform actions based on the settings configured during setup.

2. **Stop SpinBot**:
   - To stop the bot, press `CTRL + C` in the terminal window.

## Customization

### Environment Variables

You can customize SpinBot’s behavior by editing the `.env` file generated during setup:

- **TESSERACT_PATH**: Path to the Tesseract-OCR executable.
- **REGION**: Screen region where the spinning occurs.
- **STOP_RARITIES**: List of rarities that trigger stopping the bot.
- **SPIN_IMAGE_PATH**: Path to the image of the "Spin" button.
- **RESPIN_IMAGE_PATH**: Path to the image of the "ReSpin" button.

### Changing Stop Conditions

If you wish to change the rarities at which the bot should stop, simply modify the `STOP_RARITIES` value in the `.env` file.

## Troubleshooting

- **Tesseract Not Found**:
  - Ensure Tesseract-OCR is installed and that the path in `.env` is correct.
  - For Windows, verify that the path includes `tesseract.exe`.
  
- **Images Not Found**:
  - Double-check the paths provided to the images of the "Spin" and "ReSpin" buttons.
  - Ensure the images are clear and correctly captured.

- **Bot Not Stopping**:
  - Review the `STOP_RARITIES` list in the `.env` file to ensure it contains the correct rarities.

## Contributing

We welcome contributions! If you’d like to improve SpinBot:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Sino1507/Spin-Bot/blob/main/LICENSE) file for more details.

---

**Enjoy using SpinBot!** If you encounter any issues or have suggestions, feel free to open an issue on the [GitHub repository](https://github.com/Sino1507/Spin-Bot/issues).

---
