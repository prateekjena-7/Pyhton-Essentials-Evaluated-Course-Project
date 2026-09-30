from calculations import calculate_calories
from validation import validate_input
from constants import EXERCISE_LEVELS


def terminal_calculator():
    print("\n===== DAILY CALORIE CALCULATOR =====")

    try:
        age = int(input("Enter your age: "))
        sex = input("Enter your sex (Male/Female): ").strip()
        height = float(input("Enter your height in cm: "))
        weight = float(input("Enter your weight in kg: "))

        print("\nExercise Level:")
        for level in EXERCISE_LEVELS:
            print(level)

        exercise = input("Choose 1-5: ").strip()

        exercise_options = {
            "1": "1 - No exercise",
            "2": "2 - Light exercise",
            "3": "3 - Normal exercise",
            "4": "4 - Intense exercise",
            "5": "5 - Very intense exercise"
        }

        if exercise not in exercise_options:
            print("Invalid exercise choice.")
            return

        exercise = exercise_options[exercise]

        valid, message = validate_input(
            age,
            height,
            weight,
            sex,
            exercise
        )

        if not valid:
            print(message)
            return

        results = calculate_calories(
            age,
            sex,
            height,
            weight,
            exercise
        )

        print("\n===== RESULTS =====")
        print(f"BMR: {results['bmr']:.0f} kcal/day")
        print(
            f"Maintenance: "
            f"{results['maintenance']:.0f} kcal/day"
        )
        print(
            f"Weight Gain Estimate: "
            f"{results['gain']:.0f} kcal/day"
        )
        print(
            f"Weight Loss Estimate: "
            f"{results['loss']:.0f} kcal/day"
        )

    except ValueError:
        print("Please enter valid numbers.")