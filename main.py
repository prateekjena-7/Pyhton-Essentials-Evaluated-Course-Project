from terminal_calculator import terminal_calculator
from gui_calculator import start_gui


def main():
    print("\n===== DAILY CALORIE CALCULATOR =====")
    print("1. Terminal")
    print("2. GUI")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        terminal_calculator()

    elif choice == "2":
        start_gui()

    else:
        print("Invalid choice. Please choose 1 or 2.")


if __name__ == "__main__":
    main()