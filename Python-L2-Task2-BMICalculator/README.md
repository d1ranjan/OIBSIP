# BMI Calculator

A Python GUI application that calculates Body Mass Index (BMI), classifies the result, stores user records in a database, and provides graphical analysis.

## Features

* 📏 Height input in feet
* ⚖️ Weight input in kilograms
* 📊 BMI calculation and classification
* 💾 Store records using SQLite
* 📈 Display BMI history and graphs
* 🖥️ User-friendly Tkinter interface

## Technologies Used

* Python
* Tkinter
* SQLite3
* Matplotlib

## Installation

Install the required dependency:

```bash
pip install matplotlib
```

> Tkinter and SQLite3 are included with most standard Python installations.

## Usage

Run the application:

```bash
python task2.py
```

Enter your height and weight, then click the calculate button to view your BMI and save the record.

## BMI Categories

| BMI            | Category      |
| -------------- | ------------- |
| Below 18.5     | Underweight   |
| 18.5 – 24.9    | Normal Weight |
| 25.0 – 29.9    | Overweight    |
| 30.0 and above | Obese         |

## Future Improvements

* Export records to CSV or Excel
* Dark mode
* User authentication
* BMI trend analysis

## License

This project is intended for educational and learning purposes.
