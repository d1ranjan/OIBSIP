import tkinter as tk
from tkinter import ttk, messagebox
import secrets
import string
import pyperclip


root = tk.Tk()
root.title("Random Password Generator")
root.geometry("550x620")
root.resizable(False, False)

history = []



length_var = tk.IntVar(value=8)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

exclude_var = tk.BooleanVar()

password_var = tk.StringVar()



UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase
NUMBERS = string.digits
SYMBOLS = "!@#$%^&*()_-+=[]{}|;:,.<>?/"

AMBIGUOUS = "0O1lI"




def password_strength(length, types):

    if  types == 2:
        return "Weak", 33

    elif length < 14 or types == 3:
        return "Medium", 66

    else:
        return "Strong", 100




def generate_password():

    length = length_var.get()

    if length < 8:
        messagebox.showerror("Error", "Password length must be at least 8.")
        return

    selected = []

    if upper_var.get():
        chars = UPPER
        if exclude_var.get():
            chars = "".join(c for c in chars if c not in AMBIGUOUS)
        selected.append(chars)

    if lower_var.get():
        chars = LOWER
        if exclude_var.get():
            chars = "".join(c for c in chars if c not in AMBIGUOUS)
        selected.append(chars)

    if number_var.get():
        chars = NUMBERS
        if exclude_var.get():
            chars = "".join(c for c in chars if c not in AMBIGUOUS)
        selected.append(chars)

    if symbol_var.get():
        selected.append(SYMBOLS)

    if len(selected) < 2:
        messagebox.showerror(
            "Error",
            "Select at least two character types."
        )
        return

    password = []

    # One guaranteed character from each selected type
    for group in selected:
        password.append(secrets.choice(group))

    all_chars = "".join(selected)

    while len(password) < length:
        password.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password)

    final_password = "".join(password)

    password_var.set(final_password)

    pyperclip.copy(final_password)

    # History
    history.insert(0, final_password)
    if len(history) > 5:
        history.pop()

    history_box.delete(0, tk.END)
    for item in history:
        history_box.insert(tk.END, item)

    strength, value = password_strength(length, len(selected))
    strength_label.config(text="Strength : " + strength)
    progress["value"] = value



def copy_password():

    if password_var.get():
        pyperclip.copy(password_var.get())
        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard."
        )




title = tk.Label(
    root,
    text="Random Password Generator",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Password Length").grid(row=0, column=0, padx=5)

spin = tk.Spinbox(
    frame,
    from_=8,
    to=64,
    textvariable=length_var,
    width=5
)
spin.grid(row=0, column=1)

options = tk.LabelFrame(root, text="Character Types")
options.pack(padx=10, pady=10, fill="x")

tk.Checkbutton(
    options,
    text="Uppercase",
    variable=upper_var
).pack(anchor="w")

tk.Checkbutton(
    options,
    text="Lowercase",
    variable=lower_var
).pack(anchor="w")

tk.Checkbutton(
    options,
    text="Numbers",
    variable=number_var
).pack(anchor="w")

tk.Checkbutton(
    options,
    text="Symbols",
    variable=symbol_var
).pack(anchor="w")

tk.Checkbutton(
    options,
    text="Exclude Ambiguous Characters (0 O 1 l I)",
    variable=exclude_var
).pack(anchor="w", pady=5)

tk.Button(
    root,
    text="Generate Password",
    width=22,
    command=generate_password
).pack(pady=10)

entry = tk.Entry(
    root,
    textvariable=password_var,
    font=("Consolas", 14),
    justify="center",
    width=35
)
entry.pack(pady=5)

tk.Button(
    root,
    text="Copy to Clipboard",
    command=copy_password
).pack()

strength_label = tk.Label(
    root,
    text="Strength : "
)
strength_label.pack(pady=10)

progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=300,
    mode="determinate"
)
progress.pack()

history_frame = tk.LabelFrame(root, text="Last 5 Passwords")
history_frame.pack(fill="both", padx=10, pady=15)

history_box = tk.Listbox(
    history_frame,
    height=5,
    width=45
)
history_box.pack(padx=5, pady=5)

credit = tk.Label(
    root,
    text="Made by D(Task-3)",
    font=("Aladin", 8),
    fg="gray"
)
credit.pack(side="bottom", pady=7)
credit.place(relx=0.97, rely=1.0, anchor="se",x=5, y=-5)

root.mainloop()