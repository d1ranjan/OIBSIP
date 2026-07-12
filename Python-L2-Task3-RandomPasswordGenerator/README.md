3. Random Password Generator
A Python application that generates secure and customizable random passwords.

Features

Generate strong random passwords
Select password length
Include uppercase, lowercase, digits, and special characters
Simple graphical user interface
Copy password directly to the clipboard
Technologies Used

Python
Tkinter
secrets
string
pyperclip








TASK 3 · Random Password Generator
Objective: Build a Python tool that generates strong, random passwords based on user-defined criteria. Beginners build a command-line version; advanced builds a GUI with complexity controls and clipboard integration.
Tech Stack — Beginner: Python, random, string Tech Stack — Advanced: Python, secrets (cryptographically secure), tkinter or PyQt5, pyperclip
Feature Checklist — Beginner Tier:
[ ] Prompt user to specify desired password length (minimum 8 characters enforced)
[ ] Prompt user to choose which character types to include: uppercase letters, lowercase letters, numbers, symbols (at least 2 types must be selected)
[ ] Generate and display a password matching all specified criteria
[ ] Input validation: reject invalid lengths or no character types selected
[ ] Option to generate another password without restarting the program
[ ] GUI window with sliders or spinboxes for length control and checkboxes for character type selection
[ ] Use secrets module (not random) for cryptographically secure generation
[ ] Password strength indicator: display a visual bar or label showing strength (Weak / Medium / Strong) based on length and character diversity
[ ] Security rules enforced: generated password guaranteed to contain at least one character from each selected type
[ ] "Copy to Clipboard" button using pyperclip — password copies automatically on generation
[ ] Option to exclude ambiguous characters (e.g., 0, O, l, 1) via a checkbox
[ ] Generation history: display the last 5 generated passwords in the session (do not persist to file for security)
This project is easy and efficient to use and is made in such a simple way so that it becomes common and easy for everyone to use.
