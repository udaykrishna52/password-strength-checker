import tkinter as tk
from tkinter import messagebox
from evaluator import evaluate_password_strength

def run_gui():
    def check_password():
        password = entry.get()
        strength, remarks = evaluate_password_strength(password)
        result_label.config(text=f"Strength: {strength}\n" + "\n".join(remarks))

    root = tk.Tk()
    root.title("Password Strength Checker")

    tk.Label(root, text="Enter Password:").pack(pady=5)
    entry = tk.Entry(root, show="*", width=30)
    entry.pack(pady=5)

    tk.Button(root, text="Check Strength", command=check_password).pack(pady=5)
    result_label = tk.Label(root, text="", justify="left")
    result_label.pack(pady=10)

    root.mainloop()
