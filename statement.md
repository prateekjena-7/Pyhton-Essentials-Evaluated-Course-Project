# Project Statement — Daily Calorie Calculator

## 1. Problem Statement

Many people want to understand approximately how many calories they need each day based on their age, sex, height, weight, and level of physical activity. However, calculating estimated calorie requirements manually can be confusing, especially when different activity levels and goals are involved.

The **Daily Calorie Calculator** addresses this problem by providing a simple Python application that accepts basic user information and calculates estimated daily calorie requirements.

The application provides both a **Terminal interface** and a **Graphical User Interface (GUI)** so that users can interact with the calculator in different ways.

The project also demonstrates important software-development concepts such as modular programming, input validation, error handling, automated testing, and version control.

---

## 2. Project Objectives

The main objectives of the project are:

* Develop a practical Python-based calorie calculator.
* Calculate estimated Basal Metabolic Rate (BMR).
* Estimate daily maintenance calories using physical activity.
* Provide general calorie targets for weight gain and weight loss.
* Create both Terminal and GUI interfaces.
* Separate calculation logic from interface code.
* Implement input validation and error handling.
* Apply automated testing to the calculation module.
* Maintain a clean and modular project structure.
* Document the project using GitHub-compatible documentation.

---

## 3. Scope of the Project

The project focuses on providing general calorie estimates based on user-provided information.

### Included in Scope

The application accepts:

* Age
* Sex
* Height
* Weight
* Exercise/activity level

It provides:

* BMR estimation
* Maintenance calorie estimation
* Weight-gain calorie estimation
* Weight-loss calorie estimation
* Input validation
* Error handling
* Terminal interaction
* Graphical interaction
* Automated calculation testing

### Outside the Current Scope

The current version does not provide:

* Medical or clinical nutritional advice
* Diagnosis of health conditions
* Personalized medical diet plans
* Database-based user accounts
* Cloud storage
* Professional nutritionist consultation

The calculated values are intended as general estimates for educational purposes.

---

## 4. Target Users

The intended users include:

### Students

Students can use the application as a simple example of how Python programming concepts can be applied to a practical problem.

### General Users

People interested in obtaining a basic estimate of their daily calorie requirements can use the calculator.

### Beginner Python Developers

The modular source code can demonstrate:

* Functions
* Modules
* Dictionaries
* Input validation
* Exception handling
* Tkinter GUI development
* Unit testing
* Project organization

### Academic Evaluators

The project demonstrates the implementation of a real-world problem using modular Python programming, testing, documentation, and version control.

---

## 5. High-Level Features

### 5.1 BMR Calculation

The application estimates Basal Metabolic Rate using the Mifflin-St Jeor equation.

### 5.2 Maintenance Calories

The estimated BMR is combined with the selected activity level to estimate daily maintenance calories.

### 5.3 Weight Gain Estimate

The application provides a general calorie estimate intended for gradual weight gain.

### 5.4 Weight Loss Estimate

The application provides a general calorie estimate intended for gradual weight loss.

### 5.5 Activity Selection

Users can select from five activity levels ranging from no exercise to intense exercise.

### 5.6 Input Validation

The application checks user inputs before performing calculations.

### 5.7 Error Handling

Invalid input is handled without crashing the application.

### 5.8 Terminal Interface

Users can perform calculations directly through the command line.

### 5.9 Graphical User Interface

A Tkinter-based GUI provides a more visual way to enter information and view results.

### 5.10 Modular Architecture

Calculation, validation, constants, Terminal interaction, GUI interaction, and testing are separated into different files.

### 5.11 Automated Testing

The project includes unit tests for the core calculation functionality.

---

## 6. Expected Outcome

The expected outcome is a working, modular Python application that can:

1. Accept user information.
2. Validate the provided information.
3. Calculate estimated calorie requirements.
4. Display the results through either Terminal or GUI.
5. Handle invalid inputs appropriately.
6. Be tested using automated unit tests.
7. Be maintained and extended through its modular structure.

---

## 7. Project Structure

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

## 8. Conclusion

The Daily Calorie Calculator is a practical Python project that combines calculation logic with user-friendly interfaces.

Its modular design allows the Terminal and GUI applications to share the same calculation and validation logic. This reduces code duplication and makes the project easier to test, maintain, and expand.

The project demonstrates the application of Python programming, modular design, validation, error handling, testing, documentation, and version control in a real-world context.
