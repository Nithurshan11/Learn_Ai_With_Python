# Learn AI With Python

Practice Python functions, file handling, and classes as the first step toward AI.

Coded in **IDLE (Python 3.14.7)**. No extra packages.

## How to run

1. Open IDLE.
2. File → Open the `.py` file.
3. Run → Run Module (`F5`).

Text files (`.txt`) are created in IDLE’s current folder.

## Functions

| File | What it does |
|------|----------------|
| `Function/Ex1.py` | Menu with 3 functions and `match`/`case` |
| `Function/Ex2.py` | Calculator (`+ - * / // %`) |
| `Function/Ex3.py` | Input 3 numbers, then total and average |
| `Function/Ex4.py` | Employee name, salary, and gross salary (25% or 10% bonus) |

## File handling

| File | What it does |
|------|----------------|
| `file-handling/File_Write_Ex1.py` | 3 students → total, average → `Stud1.txt` |
| `file-handling/File_Write_Ex2.py` | 5 students → pass (`>= 75`) → `pass.txt`, fail → `fail.txt` |
| `file-handling/File_Write_Ex3.py` | 5 employees → Manager (`salary > 1000000`) or Staff |
| `file-handling/File_Write_Ex4.py` | Employees until ID `000` → allowance, bonus, gross → `emp.txt` |
| `file-handling/File_Write_Read_Ex5.py` | One product: write `prod.txt`, then read and print it |
| `file-handling/File_Write_Read_Ex6.py` | Employees until ID `0000` → 10% or 5% bonus → write and read `Emp2.txt` |
| `file-handling/File_Write_Read_Ex7.py` | Students until `0000` → total, average, Pass/Fail → `Stud2.txt` |
| `file-handling/File_Write_Read_Ex8.py` | Same as Ex7, but calculate is a separate function |
| `file-handling/File_Write_Read_Ex9.py` | Same idea, but pass (`>= 75`) and fail go to two files |

## Accessors and mutators

| File | What it does |
|------|----------------|
| `Accessor_and_mutator/Accessor_and_mutator_Ex1.py` | `student` class: set and get id and name |
| `Accessor_and_mutator/Accessor_and_mutator_Ex2.py` | Empty |
| `Accessor_and_mutator/Accessor_and_mutator_Ex3.py` | `Employee`: salary, 25% bonus, and gross salary |
| `Accessor_and_mutator/Accessor_and_mutator_Ex4.py` | `Student`: name, 3 marks, total, and average |
| `Accessor_and_mutator/Accessor_and_mutator_Ex5.py` | `Customer` bank: register, deposit, withdraw (fixed data) |
| `Accessor_and_mutator/Accessor_and_mutator_Ex6.py` | Same bank, but name, account, deposit, and withdraw come from input |
| `Accessor_and_mutator/Accessor_and_mutator_Ex7.py` | Same bank with input, using a setter and getter for each field |

## Constructors

| File | What it does |
|------|----------------|
| `Constructor_Declaration/Constructor_Declaration_Ex1.py` | `Employee`: `__init__` sets number, name, and salary |
| `Constructor_Declaration/Constructor_Declaration_Ex2.py` | `Parts`: name, code, manufacturing date, and cost |
| `Constructor_Declaration/Constructor_Declaration_Ex3.py` | Empty |
| `Constructor_Declaration/Constructor_Declaration_Ex4.py` | `Employee`: constructor sets number, name, and salary; setters add 50% allowance and gross salary |
| `Constructor_Declaration/Constructor_Declaration_Ex5.py` | Customers until `000` → commercial (`C`) or domestic (`D`) slab bill → `Customer.txt` |
| `Constructor_Declaration/Constructor_Declaration_Ex6.py` | Same bill rules as Ex5, then prints that the records were saved |

## Inheritance

| File | What it does |
|------|----------------|
| `Inheritance/Single Inheritance_Ex1.py` | Same customer bill program as constructor Ex6 (no inheritance yet) |
| `Inheritance/Single Inheritance_Ex2.py` | `Manager` inherits `Employee` and prints number, name, and department |
| `Inheritance/Single Inheritance_Ex3.py` | `Manager` inherits `Employee`; bonus is 10% above 100000, otherwise 5%, then gross salary |
| `Inheritance/Single Inheritance_Ex4.py` | `ItStudent` inherits `Student`; 3 marks, total, and average |
| `Inheritance/MultiLevel Inheritance_Ex5.py` | `C` inherits `B`, `B` inherits `A`; prints x, y, and z |
| `Inheritance/MultiLevel Inheritance_Ex6.py` | `Student` → `ITStudent` → `SWStudent` (subject, duration, and fees) |
