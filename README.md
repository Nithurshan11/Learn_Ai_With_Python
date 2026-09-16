# Learn AI With Python

First step in this AI-with-Python path: **Python functions**, plus menus, `match`/`case`, and simple programs.

You do not need extra packages. Use **Python 3.10 or newer** (`match` / `case` was added in 3.10).

```bash
python --version
```

---

## How to run the exercises

From the project folder:

```bash
python Function/Ex1.py
python Function/Ex2.py
python Function/Ex3.py
python Function/Ex4.py
```

On some Windows setups the command is `py` instead of `python`.

---

## What each file does

### `Function/Ex1.py` — menu with functions

- Three functions (`mnu1`, `mnu2`, `mnu3`)
- Infinite `while True` loop until the user chooses Exit
- `match` / `case` to call the right function

This is a good pattern: **the loop handles the menu, functions do the work**.

### `Function/Ex2.py` — calculator

- Two integers and an operator: `+`, `-`, `*`, `/`, `//`, `%`
- `match` / `case` picks the operation
- Unknown operators print `invalied operaction`

This file is still written as a script (no functions yet). A next step is to wrap the math in functions, for example `add(a, b)`.

### `Function/Ex3.py` — total and average

Menu:

1. Input three numbers
2. Calculate total and average
3. Display the results
4. Exit

Uses `global` so the input, calculate, and display functions share the same values.

### `Function/Ex4.py` — employee gross salary

Menu:

1. Input employee name and basic salary
2. Calculate gross salary (bonus 25% if basic salary is above 100000, otherwise 10%)
3. Display name, salary, and gross salary
4. Exit

---

## Code review (what is working, what to improve)

These programs already use the right beginner ideas: functions, a menu loop, and `match` / `case`. The notes below are for the next round of practice, not a rewrite of your work.

### What you did well

- **Ex1, Ex3, Ex4** split work into named functions instead of one long script.
- The infinite loop plus **Exit** option is the right way to keep a menu running.
- **Ex3 and Ex4** handle a wrong menu number with `case _:`.
- **Ex4** bonus rule matches the requirement: 25% above 100000, 10% otherwise.

### Bugs and crash cases to fix next

1. **Non-number input crashes**  
   `int(input(...))` and `float(input(...))` raise `ValueError` if the user types text. Wrap input in `try` / `except`, or check the text before converting.

2. **Calculate or display before input**  
   In Ex3 and Ex4, if you choose option 2 or 3 first, Python raises `NameError` because `num1` / `salary` do not exist yet. Set starting values at the top (Ex4 already does this for salary) or show a message like `"Please input values first"`.

3. **Division by zero in Ex2**  
   `/`, `//`, and `%` crash if the second number is `0`. Check `num2 == 0` before dividing.

4. **Ex1 has no default case**  
   Typing `5` (or any number other than 1–4) does nothing. Add `case _:` like Ex3 and Ex4.

### Python style (small cleanups)

- Semicolons (`;`) are not needed in Python.
- Prefer full names: `menu1` instead of `mnu1`, `operation` instead of `oper`.
- `global` works, but later you will pass values in and `return` results. That is how real programs (and AI code) share data without hidden state.
- Ex2 is a good candidate to rewrite with functions, since the rest of this folder is about functions.

Example of moving away from `global`:

```python
def calculate(num1, num2, num3):
    total = num1 + num2 + num3
    average = total / 3
    return total, average
```

---

## Suggested next steps toward AI with Python

1. Practice functions with **parameters** and **return values** (less `global`).
2. Learn **lists** and **dictionaries** (datasets are collections of values).
3. Learn **files** (`open`, `read`, `write`) so programs can load data.
4. Then libraries used in AI: **NumPy**, **pandas**, **matplotlib**.
5. After that: simple machine learning with **scikit-learn**.

---

## Project layout

```
Learn_Ai_With_Python/
├── Function/
│   ├── Ex1.py    # menu functions
│   ├── Ex2.py    # calculator
│   ├── Ex3.py    # total and average
│   └── Ex4.py    # employee salary
├── README.md
└── .gitignore
```
