# CPE106L - Laboratory Activity 1

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

## Features & Capabilities

- **Interactive Operations:** Choose to multiply an input integer by 2, multiply by 3, or provide a custom integer multiplier.
- **Input Validation & Error Handling:** Prevents program crashes when non-integer values or out-of-range choices are entered.
- **Modular Code Design:** Encapsulates multiplication logic inside a dedicated, reusable `multiply()` function.

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

---

## Testing & Test Cases

Run multiple test cases to verify functionality across different scenarios:

1. **Option 1 (Multiply by 2):** Input `4` -> Choice `1` -> Result: `8`
2. **Option 2 (Multiply by 3):** Input `7` -> Choice `2` -> Result: `21`
3. **Option 3 (Custom Multiplier):** Input `5` -> Choice `3` -> Multiplier `4` -> Result: `20`
4. **Error Handling Test:** Input non-integer text string (e.g., `abc`) -> Output: `Error: Invalid input! Please enter valid integers only.`

---

## Author

- **Name:** Daniel Yuan C. Velasco
- **Course:** CPE106L
- **GitHub:** [@eps-man01](https://github.com/eps-man01)
