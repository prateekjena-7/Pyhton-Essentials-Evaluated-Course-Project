import unittest

from calculations import calculate_calories


class TestCalculations(unittest.TestCase):

    def test_calculate_calories(self):
        result = calculate_calories(
            20,
            "Male",
            175,
            70,
            "1 - No exercise"
        )

        self.assertIn("bmr", result)
        self.assertIn("maintenance", result)
        self.assertIn("gain", result)
        self.assertIn("loss", result)


if __name__ == "__main__":
    unittest.main()