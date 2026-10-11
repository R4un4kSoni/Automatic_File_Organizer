# Automatic_File_Organizer

A simple yet efficient Python script designed to automatically organize unorganized files within a directory by grouping them into dedicated folders based on their file extensions.

## Features

* **Automated Categorization:** Scans a target directory and sorts files into subdirectories named after their respective file extensions (e.g., `PNG`, `JPG`, `TXT`).
* **Extension Normalization:** Converts extensions to uppercase and handles files without extensions gracefully by placing them into a `NO_EXTENSION` folder.
* **Safe Directory Creation:** Automatically creates destination folders only if they do not already exist, preventing redundant operations.
* **Built-in Modules Only:** Relies solely on Python's standard library (`pathlib` and `shutil`), meaning no external dependencies or installations are required.

---

## Prerequisites

* Python 3.6 or higher installed on your system.

---

## Project Structure

### Before Running the Script
```text
Assets/
│
├── image1.png
├── document.pdf
├── notes.txt
├── graphic.jpg
└── unknown_file
