def validate_input(age, height, weight, sex, exercise):
    """Check whether the user's input is valid."""

    if age <= 0:
        return False, "Age must be greater than 0."

    if height <= 0:
        return False, "Height must be greater than 0."

    if weight <= 0:
        return False, "Weight must be greater than 0."

    if sex.lower() not in ["male", "female"]:
        return False, "Sex must be Male or Female."

    if exercise not in [
        "1 - No exercise",
        "2 - Light exercise",
        "3 - Normal exercise",
        "4 - Intense exercise",
        "5 - Very intense exercise"
    ]:
        return False, "Invalid exercise level."

    return True, "Valid input."