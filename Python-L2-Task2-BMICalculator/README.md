2. BMI Calculator
A graphical Body Mass Index (BMI) calculator developed using Tkinter.

Features

Calculate BMI using height and weight
Supports height input in feet and weight in kilograms
Displays BMI category (Underweight, Normal, Overweight, Obese)
Stores records in an SQLite database
Displays BMI history and graphical analysis
Technologies Used

Python
Tkinter
SQLite3
Matplotlib


Objective: Build a Python program that calculates a user's Body Mass Index (BMI) and classifies it into health categories. Beginners build a command-line tool; advanced builds a full GUI application with data persistence and trend visualisation.
Tech Stack — Beginner: Python, input(), basic arithmetic Tech Stack — Advanced: Python, tkinter or PyQt5, matplotlib, sqlite3 or CSV file storage
Feature Checklist — Beginner Tier:



[ ] Prompt user for weight (kg) and height (m) via command line
[ ] Calculate BMI using the formula: BMI = weight / (height²)
[ ] Classify result into standard categories: Underweight (< 18.5), Normal (18.5–24.9), Overweight (25–29.9), Obese (≥ 30)
[ ] Display the BMI value rounded to 2 decimal places and the category
[ ] Input validation: reject non-numeric input and negative values with a helpful error message.
[ ] GUI window built with tkinter or PyQt5 — no command line
[ ] Input fields with labels for weight and height; a "Calculate" button
[ ] Result displayed in the GUI with colour-coded feedback (e.g., green = normal, red = obese)
[ ] Multi-user support: allow saving BMI records for different named users
[ ] Historical records stored in an SQLite database or CSV file
[ ] Graph view: display a line chart of a user's BMI trend over time using matplotlib
[ ] Error handling for database read/write failures
The project uses another metric as feet and inches instead of metres so that even local and common people can easily use this.
