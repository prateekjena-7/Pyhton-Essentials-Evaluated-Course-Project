from constants import EXERCISE_LEVELS


def calculate_bmr(age, sex, height, weight):
    """Calculate Basal Metabolic Rate."""

    if sex.lower() == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5

    return 10 * weight + 6.25 * height - 5 * age - 161


def calculate_calories(age, sex, height, weight, exercise):
    """Calculate daily calorie estimates."""

    bmr = calculate_bmr(age, sex, height, weight)

    multiplier = EXERCISE_LEVELS[exercise]
    maintenance = bmr * multiplier

    gain = maintenance + 300
    loss = maintenance - 500

    return {
        "bmr": bmr,
        "maintenance": maintenance,
        "gain": gain,
        "loss": loss
    }