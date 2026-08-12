## Password Checker

A simple desktop password security checker built with **Python and PyQt6**.

## Description

Password Checker is a PyQt6 desktop application that helps users check whether a password meets several basic security requirements.

The application provides immediate visual feedback while the user enters a password. Requirements change from red to green when they are satisfied.

## Features

* Checks for a minimum of 10 characters
* Checks for at least one uppercase letter
* Checks for at least one lowercase letter
* Checks for at least one number
* Checks for a special character
* Shows which requirements are satisfied
* Allows the user to show or hide the password
* Simple PyQt6 graphical user interface

## Technologies

* Python
* PyQt6
* Regular Expressions (`re`)

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Tade2020/Password-Checker.git
```

### 2. Open the project folder

```bash
cd Password-Checker
```

### 3. Install PyQt6

```bash
pip install PyQt6
```

### 4. Run the application

```bash
python "Password Checker.py"
```

## Project Structure

```text
Password-Checker/
│
├── Password Checker.py
├── Resources/
│   └── check.png
└── README.md
```

## What I Learned

This project helped me practice:

* Building a desktop application with PyQt6
* Working with PyQt6 signals and widgets
* Using regular expressions to validate text
* Organizing a Python project
* Using Git for version control
* Creating and managing a GitHub repository
* Uploading and maintaining a project using Git

## Future Improvements

Possible future improvements include:

* Password strength scoring
* Common password detection
* Password generation
* More advanced password security analysis
* Improved user interface

## Disclaimer

This application is intended for educational purposes and provides basic password requirement checking. Meeting these requirements does not guarantee that a password is completely secure.
