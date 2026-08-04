# CPE106L-4 - Laboratory Activity 1

An interactive Python command-line program demonstrating fundamental programming concepts, input validation, error handling, modular function design, and Git version control workflows.

---

## Project Overview

This repository contains the source code, directory layout, and execution instructions for **Laboratory Activity 1**. The program allows a user to input an integer and choose from a menu of multiplication options (multiply by 2, multiply by 3, or multiply by a custom integer), incorporating robust error handling for non-integer inputs.

---

## Repository Structure

```text
.
├── README.md           # Project documentation and execution guide
├── src/
│   └── main.py         # Main interactive Python script
├── tests/              # Test files and test cases
└── screenshots/        # Execution output and Git log screenshots
```

---

## Program Features & Functions

- **Modular Logic (`multiply()`):** Encapsulates multiplication functionality inside a reusable helper function accepting input value, choice, and optional custom multiplier parameters.
- **Interactive Menu Options:**
  - Option 1: Multiply input by 2
  - Option 2: Multiply input by 3
  - Option 3: Multiply input by a custom user-provided integer
- **Input Validation & Error Handling:** Utilizes `try-except` blocks (`ValueError`) to catch invalid non-integer inputs and prevent runtime crashes.

---

## Requirements & Environment Setup

### Prerequisites
- Python 3.10+
- Git & GitHub CLI (`gh`)
- Linux / WSL (Ubuntu)

### Virtual Environment Setup

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate
```

---

## How to Run

Execute the main Python script from the root directory of the project:

```bash
python3 src/main.py
```

### Sample Interactive Usage

```text
Enter an integer: 5

Choose an option:
1. Multiply by 2
2. Multiply by 3
3. Multiply by custom number
Enter your choice (1, 2, or 3): 3
Enter the custom integer multiplier: 4

Result: 20
```
