import tkinter as tk
from tkinter import messagebox

from calculations import calculate_calories
from validation import validate_input
from constants import EXERCISE_LEVELS


def start_gui():
    root = tk.Tk()
    root.title("Daily Calorie Calculator")
    root.geometry("420x570")
    root.resizable(False, False)
    root.configure(bg="#f2f2f2")

    # Variables
    age_var = tk.StringVar()
    height_var = tk.StringVar()
    weight_var = tk.StringVar()
    sex_var = tk.StringVar(value="Male")
    exercise_var = tk.StringVar(
        value="1 - No exercise"
    )

    # Title
    tk.Label(
        root,
        text="DAILY CALORIE CALCULATOR",
        font=("Arial", 16, "bold"),
        bg="#f2f2f2"
    ).pack(pady=15)

    # Input section
    input_frame = tk.Frame(
        root,
        bg="white",
        padx=15,
        pady=10
    )
    input_frame.pack(padx=20, fill="x")

    tk.Label(
        input_frame,
        text="Age:",
        bg="white"
    ).grid(row=0, column=0, sticky="w", pady=7)

    tk.Entry(
        input_frame,
        textvariable=age_var
    ).grid(row=0, column=1, pady=7)

    tk.Label(
        input_frame,
        text="Sex:",
        bg="white"
    ).grid(row=1, column=0, sticky="w", pady=7)

    tk.OptionMenu(
        input_frame,
        sex_var,
        "Male",
        "Female"
    ).grid(row=1, column=1, pady=7)

    tk.Label(
        input_frame,
        text="Height (cm):",
        bg="white"
    ).grid(row=2, column=0, sticky="w", pady=7)

    tk.Entry(
        input_frame,
        textvariable=height_var
    ).grid(row=2, column=1, pady=7)

    tk.Label(
        input_frame,
        text="Weight (kg):",
        bg="white"
    ).grid(row=3, column=0, sticky="w", pady=7)

    tk.Entry(
        input_frame,
        textvariable=weight_var
    ).grid(row=3, column=1, pady=7)

    tk.Label(
        input_frame,
        text="Exercise:",
        bg="white"
    ).grid(row=4, column=0, sticky="w", pady=7)

    tk.OptionMenu(
        input_frame,
        exercise_var,
        *EXERCISE_LEVELS.keys()
    ).grid(row=4, column=1, pady=7)

    # Results
    results_frame = tk.Frame(
        root,
        bg="white",
        padx=15,
        pady=12
    )
    results_frame.pack(
        padx=20,
        pady=15,
        fill="x"
    )

    tk.Label(
        results_frame,
        text="RESULTS",
        font=("Arial", 13, "bold"),
        bg="white"
    ).grid(
        row=0,
        column=0,
        columnspan=2,
        pady=5
    )

    result_labels = {}

    for row, name in enumerate(
        ["BMR", "Maintenance", "Weight Gain", "Weight Loss"],
        start=1
    ):
        tk.Label(
            results_frame,
            text=f"{name}:",
            bg="white"
        ).grid(
            row=row,
            column=0,
            sticky="w",
            pady=5
        )

        result_labels[name] = tk.Label(
            results_frame,
            text="--",
            bg="white"
        )
        result_labels[name].grid(
            row=row,
            column=1,
            sticky="e"
        )

    def calculate():
        try:
            age = int(age_var.get())
            height = float(height_var.get())
            weight = float(weight_var.get())

            valid, message = validate_input(
                age,
                height,
                weight,
                sex_var.get(),
                exercise_var.get()
            )

            if not valid:
                messagebox.showerror("Error", message)
                return

            results = calculate_calories(
                age,
                sex_var.get(),
                height,
                weight,
                exercise_var.get()
            )

            result_labels["BMR"].config(
                text=f"{results['bmr']:.0f} kcal/day"
            )

            result_labels["Maintenance"].config(
                text=f"{results['maintenance']:.0f} kcal/day"
            )

            result_labels["Weight Gain"].config(
                text=f"{results['gain']:.0f} kcal/day"
            )

            result_labels["Weight Loss"].config(
                text=f"{results['loss']:.0f} kcal/day"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter valid numbers."
            )

    def clear():
        age_var.set("")
        height_var.set("")
        weight_var.set("")
        sex_var.set("Male")
        exercise_var.set("1 - No exercise")

        for label in result_labels.values():
            label.config(text="--")

    # Buttons
    button_frame = tk.Frame(
        root,
        bg="#f2f2f2"
    )
    button_frame.pack(pady=5)

    tk.Button(
        button_frame,
        text="Calculate",
        width=12,
        command=calculate
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        button_frame,
        text="Clear",
        width=12,
        command=clear
    ).grid(row=0, column=1, padx=5)

    tk.Label(
        root,
        text="Estimates only. Not medical advice.",
        font=("Arial", 9),
        bg="#f2f2f2",
        fg="gray"
    ).pack(pady=12)

    root.mainloop()