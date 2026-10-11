# Automatic_File_Organizer


A Python script designed to automatically organize unorganized files inside an `Assets` subdirectory by grouping them into dedicated folders based on their file extensions.

## Features

* **Automated Categorization:** Scans the `Assets` folder and sorts files into subdirectories named after their respective file extensions (e.g., `PNG`, `PDF`, `TXT`).
* **Extension Normalization:** Converts extensions to uppercase and handles files without extensions by placing them into a `NO_EXTENSION` folder.
* **Safe Directory Creation:** Automatically creates destination folders only if they do not already exist.
* **Standard Library Only:** Uses only Python's built-in `pathlib` and `shutil` modules—no external installations required.

---

## Prerequisites

* Python 3.6 or higher installed on your system.

---

## Project Directory Structure

Your project folder should be set up as follows before running the script:

```text
MyFileOrganizer/
│
├── main.py
└── Assets/
    ├── image1.png
    ├── document.pdf
    ├── notes.txt
    └── unknown_file
