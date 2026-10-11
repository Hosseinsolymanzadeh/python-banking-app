# Bank-001

A simple Python banking project used for practicing Python fundamentals, project structure, testing, and Git workflows.

## Warning

This project is for educational purposes only. It is not suitable for real financial transactions or production use.

## Requirements

* Python 3.10 or later
* Git

## Setup

Clone the repository and navigate to the project directory.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in Git Bash on Windows:

```bash
source .venv/Scripts/activate
```

Install development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

## Run

Run the package from the project root:

```bash
python -m bank
```

Expected output:

```text
Banking app skeleton - no features yet.
```

## Tests

Run the tests from the project root:

```bash
python -m pytest
```

Using `python -m pytest` runs pytest with the selected Python interpreter and normally includes the current directory in Python's module search path.

Running `pytest` directly may use a different Python environment if the command points to another installation.

Running `python -m pytest` without activating `.venv` may fail if pytest is installed only inside `.venv` and the system Python does not have pytest installed.

## Project Structure

```text
Bank-001/
├── bank/
│   ├── __init__.py
│   └── __main__.py
├── legacy/
│   ├── v1.0.0.py
│   ├── v1.1.0.py
│   └── v1.2.0_wip.py
├── tests/
│   └── test_smoke.py
├── .gitignore
├── README.md
└── requirements-dev.txt
```

The `legacy/` directory contains earlier versions and work-in-progress files kept for reference.
The v1.2.0_wip.py file is an unfinished prototype and may contain undefined dependencies or incomplete functionality. It is kept for reference and is not part of the runnable bank package.