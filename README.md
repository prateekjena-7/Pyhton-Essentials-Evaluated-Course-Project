# 🥗 Daily Calorie Calculator

A modular Python-based **Daily Calorie Calculator** that estimates a user's Basal Metabolic Rate (BMR), daily maintenance calories, and calorie targets for weight gain and weight loss.

The project provides both a **Terminal-based interface** and a **Graphical User Interface (GUI)** built with Tkinter. Both interfaces use the same calculation and validation modules, making the application easier to maintain, test, and extend.

> **Note:** This application provides general calorie estimates for educational and project purposes. It is not medical advice.

---

## 📌 Project Overview

The Daily Calorie Calculator is designed to demonstrate how Python programming concepts can be applied to a practical real-world problem.

The application collects basic user information such as:

* Age
* Sex
* Height
* Weight
* Exercise level

It then processes the information using a BMR calculation and an activity multiplier to estimate daily calorie requirements.

The project has been designed using a **modular architecture**, separating calculations, validation, constants, terminal interaction, GUI interaction, and testing.

---

## ✨ Features

### Core Features

* Calculate **BMR (Basal Metabolic Rate)**
* Calculate estimated **maintenance calories**
* Calculate estimated **weight-gain calories**
* Calculate estimated **weight-loss calories**
* Support for male and female users
* Five different exercise/activity levels
* Input validation
* Error handling
* Clear/reset functionality in the GUI
* Terminal-based calculator
* Graphical calculator using Tkinter
* Automated unit testing
* Shared calculation logic between Terminal and GUI

### Application Interfaces

#### 💻 Terminal Mode

The terminal version allows users to enter their information directly through the command line.

#### 🖥️ GUI Mode

The graphical version provides input fields, dropdown menus, result displays, and buttons using Python's Tkinter library.

---

## 🏗️ Project Architecture

The application follows a modular structure:

```text
                         ┌───────────────┐
                         │    main.py    │
                         └───────┬───────┘
                                 │
                    ┌────────────┴────────────┐
                    │                         │
                    ▼                         ▼
          ┌──────────────────┐     ┌──────────────────┐
          │ terminal_         │     │ gui_calculator.py│
          │ calculator.py     │     └────────┬─────────┘
          └────────┬─────────┘              │
                   │                        │
                   └──────────┬─────────────┘
                              ▼
                    ┌──────────────────┐
                    │ calculations.py  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  constants.py    │
                    └──────────────────┘

                    ┌──────────────────┐
                    │  validation.py   │
                    └──────────────────┘

                    ┌──────────────────┐
                    │      tests/      │
                    │ test_calculations│
                    └──────────────────┘
```

### Design Approach

The project separates responsibilities into different modules:

| Module                       | Responsibility                                                  |
| ---------------------------- | --------------------------------------------------------------- |
| `main.py`                    | Starts the application and lets the user choose Terminal or GUI |
| `terminal_calculator.py`     | Handles terminal-based interaction                              |
| `gui_calculator.py`          | Handles the Tkinter graphical interface                         |
| `calculations.py`            | Contains the calorie calculation logic                          |
| `validation.py`              | Validates user input                                            |
| `constants.py`               | Stores activity/exercise level constants                        |
| `tests/test_calculations.py` | Tests the calculation functionality                             |
| `requirements.txt`           | Documents project dependencies                                  |

This structure prevents the calculation formula from being duplicated between the Terminal and GUI versions.

---

## 🧮 Calculation Logic

The application first estimates **Basal Metabolic Rate (BMR)** using the **Mifflin-St Jeor equation**.

### Male

```text
BMR = (10 × weight) + (6.25 × height) − (5 × age) + 5
```

### Female

```text
BMR = (10 × weight) + (6.25 × height) − (5 × age) − 161
```

The estimated BMR is then multiplied by an activity factor to estimate maintenance calories.

The application also provides general calorie estimates for:

* Weight gain
* Maintenance
* Weight loss

These values are estimates and should not be treated as personalized medical or nutritional advice.

---

## 🏃 Exercise Levels

The application supports five activity levels:

| Level | Activity                           |
| ----- | ---------------------------------- |
| 1     | No exercise                        |
| 2     | Walking/running a few times a week |
| 3     | Normal exercise                    |
| 4     | Intense exercise 2–4 days/week     |
| 5     | Intense exercise 5–6 days/week     |

The activity level is selected by the user through the Terminal or GUI interface.

---

## 🛠️ Technologies Used

### Programming Language

* **Python 3**

### Libraries

* `tkinter` — Graphical User Interface
* `unittest` — Automated testing

The project uses Python's standard library and does not require external pip packages.

---

## 📁 Folder Structure

```text
Daily-Calorie-Calculator/
│
├── main.py
├── terminal_calculator.py
├── gui_calculator.py
├── calculations.py
├── validation.py
├── constants.py
├── requirements.txt
├── README.md
├── statement.md
│
└── tests/
    └── test_calculations.py
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/prateekjena-7/Pyhton-Essentials-Evaluated-Course-Project.git
```

### 2. Open the project folder

```bash
cd cd Pyhton-Essentials-Evaluated-Course-Project
```

### 3. Check Python installation

```bash
python --version
```

Python 3.x is required.

### 4. Install dependencies

This project uses only Python's standard library, so no external packages are required.

If desired, the dependency documentation can be checked with:

```bash
pip install -r requirements.txt
```

No additional packages should be necessary.

---

## ▶️ How to Run

Start the application with:

```bash
python main.py
```

You will see:

```text
===== DAILY CALORIE CALCULATOR =====
1. Terminal
2. GUI
Choose 1 or 2:
```

### Terminal

Enter:

```text
1
```

The Terminal calculator will start and ask for the required information.

### GUI

Enter:

```text
2
```

The Tkinter graphical interface will open.

---

## 🧪 Testing

The project includes automated tests using Python's built-in `unittest` framework.

Run:

```bash
python -m unittest discover -s tests -v
```

A successful test run should end with:

```text
OK
```

The test suite helps verify that the core calculation module is functioning correctly.

---

## ✅ Validation & Error Handling

The application validates user input before performing calculations.

Examples of handled problems include:

* Invalid numeric input
* Invalid age
* Invalid height
* Invalid weight
* Invalid sex selection
* Invalid exercise level

The GUI displays errors using Tkinter message boxes, while the Terminal version provides appropriate console messages.

---

## 🔄 Application Workflow

```text
Start
  │
  ▼
Choose Interface
  │
  ├───────────────┐
  ▼               ▼
Terminal          GUI
  │               │
  └───────┬───────┘
          ▼
     Enter Details
          │
          ▼
     Validate Input
          │
      ┌───┴───┐
      │       │
    Invalid  Valid
      │       │
      ▼       ▼
    Error   Calculate
              │
              ▼
       Display Results
              │
              ▼
             End
```

---

## 📸 Screenshots

Screenshots can be added here after the final application is tested.

Recommended screenshots:

1. Terminal menu
2. Terminal calculation result
3. GUI input screen
4. GUI result screen
5. Successful unit-test output

Example:

```text
### GUI

![GUI Screenshot](screenshots/gui.png)

### Terminal

![Terminal Screenshot](screenshots/terminal.png)
```

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Build a practical Python application.
2. Apply modular programming principles.
3. Separate business logic from user-interface code.
4. Implement input validation and error handling.
5. Provide both Terminal and GUI interfaces.
6. Demonstrate automated testing.
7. Use Git and GitHub for version control.
8. Create clear technical documentation.

---

## 🔐 Limitations

This application is an educational calorie-estimation tool.

It does not account for every individual factor that can affect energy requirements, such as:

* Body composition
* Medical conditions
* Medications
* Pregnancy
* Athletic training demands
* Individual metabolic differences

Therefore, the results should be treated as general estimates rather than medical or clinical recommendations.

---

## 🚀 Future Enhancements

Possible future improvements include:

* BMI calculation
* Macro/nutrient recommendations
* More detailed activity categories
* Saving user profiles
* Calculation history
* Exporting results
* Charts and visualizations
* Dark mode
* Improved GUI styling
* Database integration
* More extensive automated tests
* Web or mobile version

---

## 📚 Learning Outcomes

Through this project, the following Python and software-development concepts are demonstrated:

* Functions
* Variables and data types
* Conditional statements
* Dictionaries
* Modules
* Modular programming
* Exception handling
* Input validation
* Tkinter GUI development
* Unit testing
* File/folder organization
* Git and GitHub
* Technical documentation

---

## 👨‍💻 Author

**Prateek Jena**

Daily Calorie Calculator — Python Project

---

## 📄 License

This project was created for educational and academic purposes.
