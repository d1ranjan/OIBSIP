import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt


try:
    conn = sqlite3.connect("bmi_records.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bmi(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight REAL,
        height REAL,
        bmi REAL,
        category TEXT,
        date TEXT
    )
    """)

    conn.commit()

except Exception as e:
    messagebox.showerror("Database Error", str(e))



def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "blue"

    elif bmi < 25:
        return "Normal", "green"

    elif bmi < 30:
        return "Overweight", "orange"

    else:
        return "Obese", "red"


def calculate():

    name = entry_name.get().strip()

    if name == "":
        messagebox.showerror("Error", "Enter your name.")
        return

    try:
        weight = float(entry_weight.get())
        feet   = float(entry_feet.get())
        inches = float(entry_inches.get())
        total_inches = feet *12 + inches
        height = total_inches * 0.0254

        if weight <= 0 or height <= 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Weight and Height must be positive numbers."
        )
        return

    bmi = weight / (height ** 2)

    category, color = bmi_category(bmi)

    result.config(
        text=f"BMI = {bmi:.2f}\nCategory : {category}",
        fg=color
    )

    try:
        cursor.execute(
            "INSERT INTO bmi(name,weight,height,bmi,category, date) VALUES(?,?,?,?,?,?)",
            (
                name,
                weight,
                height,
                bmi,
                category,
                datetime.now().strftime("%Y-%m-%d")
            )
        )

        conn.commit()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))


def history():

    name = entry_name.get().strip()

    if name == "":
        messagebox.showerror("Error", "Enter user name.")
        return

    try:

        cursor.execute(
            "SELECT date,bmi FROM bmi WHERE name=?",
            (name,)
        )

        rows = cursor.fetchall()

        if not rows:
            messagebox.showinfo(
                "History",
                "No records found."
            )
            return

        text = ""

        for row in rows:
            text += f"{row[0]}   BMI : {row[1]:.2f}\n"

        messagebox.showinfo("History", text)

    except Exception as e:
        messagebox.showerror("Database Error", str(e))



def graph():

    name = entry_name.get().strip()

    if name == "":
        messagebox.showerror("Error", "Enter user name.")
        return

    try:

        cursor.execute(
            "SELECT date,bmi FROM bmi WHERE name=?",
            (name,)
        )

        rows = cursor.fetchall()

        if len(rows) == 0:
            messagebox.showinfo("Graph", "No data available.")
            return

        dates = [r[0] for r in rows]
        values = [r[1] for r in rows]

        plt.figure(figsize=(8,5))
        plt.plot(dates, values, marker= 'o')
        plt.tight_layout()
        plt.title(f"{name}'s BMI Trend")
        plt.xlabel("Date")
        plt.ylabel("BMI")
        plt.grid(True)
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))



root = tk.Tk()

root.title("BMI Calculator")
root.geometry("420x420")

title = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial",18,"bold")
)
title.pack(pady=10)
footer = tk.Label(
    root,
    text="Made by D(Task-2)",
    font=("Aladin", 7),
    fg="black"
)
footer.place(relx=0.97, rely=1.0, anchor="se",x=5, y=-5)
tk.Label(root,text="Name").pack()

entry_name = tk.Entry(root,width=30)
entry_name.pack()

tk.Label(root,text="Weight (kg)").pack(pady=5)

entry_weight = tk.Entry(root,width=30)
entry_weight.pack()

tk.Label(root,text="Height (Feet)").pack(pady=5)

entry_feet = tk.Entry(root)
entry_feet.pack()

tk.Label(root,text="Height (Inches)").pack(pady=5)

entry_inches = tk.Entry(root)
entry_inches.pack()


tk.Button(
    root,
    text="Calculate BMI",
    command=calculate,
    width=20
).pack()

tk.Button(
    root,
    text="View History",
    command=history,
    width=20
).pack()

tk.Button(
    root,
    text="Show Graph",
    command=graph,
    width=20
).pack(pady=5)

result = tk.Label(
    root,
    text="",
    font=("Aladin",15,"italic")
)
result.pack(pady=10)

root.mainloop()

conn.close()