# Learn AI With Python

Practice Python as the first step toward AI: functions, files, classes, and inheritance.

Coded in **IDLE (Python 3.14.7)**. No extra packages. There is no machine-learning code in this repo yet.

**47** `.py` files in **6** folders. **2** of them are still empty.

## How to run

1. Open IDLE.
2. File → Open the `.py` file.
3. Run → Run Module (`F5`).

Text files (`.txt`) are created in IDLE’s current folder. Many programs open files in append mode (`"a"`), so running the same exercise twice adds another copy of the records. A few programs use write mode (`"w"`) and replace the file.

Several exercises share the same output names (`pass.txt`, `fail.txt`, `Stud2.txt`, `Customer.txt`, `customers.txt`). Run them from different folders, or delete the old `.txt` file, if you do not want the records mixed.

## Learning order

1. **Functions** — menus, `match`/`case`, calculator, totals, salary.
2. **File handling** — write student and employee records, then read them back.
3. **Accessors and mutators** — classes with setters and getters.
4. **Constructors** — `__init__` to set object data, then bills saved to a file.
5. **Inheritance** — single, multilevel, and hierarchical classes.
6. **Processing with Strings** — folder is started, but the files inside are still inheritance practice.

## Functions

| File | What it does |
|------|----------------|
| `Function/Ex1.py` | Menu with 3 functions and `match`/`case`; option 4 exits |
| `Function/Ex2.py` | Calculator for two integers (`+ - * / // %`) |
| `Function/Ex3.py` | Menu: input 3 numbers, then total and average |
| `Function/Ex4.py` | Employee name and salary; bonus is 25% above 100000, otherwise 10% |

## File handling

| File | What it does |
|------|----------------|
| `file-handling/File_Write_Ex1.py` | 3 students, 2 marks → total and average → `Stud1.txt` |
| `file-handling/File_Write_Ex2.py` | 5 students → pass (`avg >= 75`) to `pass.txt`, fail to `fail.txt` |
| `file-handling/File_Write_Ex3.py` | 5 employees → Manager (`salary > 1000000`) to `Manager.txt`, others to `Staff.txt` |
| `file-handling/File_Write_Ex4.py` | Employees until ID `000` → allowance, bonus, and gross salary → `emp.txt` |
| `file-handling/File_Write_Read_Ex5.py` | One product: write `prod.txt`, then read and print it |
| `file-handling/File_Write_Read_Ex6.py` | Employees until ID `0000` → 10% or 5% bonus → write and read `Emp2.txt` |
| `file-handling/File_Write_Read_Ex7.py` | Students until index `0000` → total, average, Pass/Fail (`avg >= 50`) → `Stud2.txt` |
| `file-handling/File_Write_Read_Ex8.py` | Same idea as Ex7, but total, average, and grade are a separate `cal()` function. Pass is `average > 50` |
| `file-handling/File_Write_Read_Ex9.py` | Students until `0000`; pass (`avg >= 75`) and fail go to two files, then both files are read |

## Accessors and mutators

Setters store data. Getters return it.

| File | What it does |
|------|----------------|
| `Accessor_and_mutator/Accessor_and_mutator_Ex1.py` | `student`: set and get id and name (fixed data) |
| `Accessor_and_mutator/Accessor_and_mutator_Ex2.py` | `product`: code, name, and manufacturing company |
| `Accessor_and_mutator/Accessor_and_mutator_Ex3.py` | `Employee`: salary, 25% bonus, and gross salary |
| `Accessor_and_mutator/Accessor_and_mutator_Ex4.py` | `Student`: name, 3 marks, total, and average |
| `Accessor_and_mutator/Accessor_and_mutator_Ex5.py` | `Customer` bank: register, deposit, withdraw (fixed data). Withdraw stops if the amount is above the balance |
| `Accessor_and_mutator/Accessor_and_mutator_Ex6.py` | Same bank, but name, account, deposit, and withdraw come from input |
| `Accessor_and_mutator/Accessor_and_mutator_Ex7.py` | Same bank with input, using a setter and getter for each field |

## Constructors

`__init__` sets the object when it is created.

| File | What it does |
|------|----------------|
| `Constructor_Declaration/Constructor_Declaration_Ex1.py` | `Employee`: `__init__` sets number, name, and salary |
| `Constructor_Declaration/Constructor_Declaration_Ex2.py` | `Parts`: name, code, manufacturing date, and cost |
| `Constructor_Declaration/Constructor_Declaration_Ex3.py` | `Student`: constructor sets name and 3 marks; setters add total and average |
| `Constructor_Declaration/Constructor_Declaration_Ex4.py` | `Employee`: constructor sets number, name, and salary; setters add 50% allowance and gross salary |
| `Constructor_Declaration/Constructor_Declaration_Ex5.py` | Customers until number `000` → commercial (`C`) or domestic (`D`) slab bill → print and save `Customer.txt` |
| `Constructor_Declaration/Constructor_Declaration_Ex6.py` | Same bill rules as Ex5, then prints that the records were saved |

Commercial slabs in Ex5 and Ex6: units 1–5 free, 6–25 at Rs. 5, 26–50 at Rs. 10, 51–75 at Rs. 15, above 75 at Rs. 25.

Domestic slabs in Ex5 and Ex6: units 1–10 free, 11–25 at Rs. 5, 26–50 at Rs. 3, 51–75 at Rs. 6, above 75 at Rs. 9.

## Inheritance

A child class uses `super()` to call the parent.

### Single inheritance

| File | What it does |
|------|----------------|
| `Inheritance/Single Inheritance_Ex1.py` | Same customer bill program as constructor Ex6 (one class, no child class yet) |
| `Inheritance/Single Inheritance_Ex2.py` | `Manager` inherits `Employee` and prints number, name, and department |
| `Inheritance/Single Inheritance_Ex3.py` | `Manager` inherits `Employee`; bonus is 10% above 100000, otherwise 5%, then gross salary |
| `Inheritance/Single Inheritance_Ex4.py` | `ItStudent` inherits `Student`; 3 marks, total, and average |

### Multilevel inheritance

Each class inherits the one above it: `C` from `B`, `B` from `A`.

| File | What it does |
|------|----------------|
| `Inheritance/MultiLevel Inheritance_Ex5.py` | `C` inherits `B`, `B` inherits `A`; prints x, y, and z |
| `Inheritance/MultiLevel Inheritance_Ex6.py` | `Student` → `ITStudent` → `SWStudent` (subject, duration, and fees). Two sample students |
| `Inheritance/MultiLevel Inheritance_Ex7.py` | `Student` → `SwStudent` → `ItStudent`; duration, fee, 3 marks, total, and average |
| `Inheritance/MultiLevel Inheritance_Ex8.py` | Same chain as Ex7, plus `writeFile()` appends the IT student to `ITStudent.txt` |
| `Inheritance/MultiLevel Inheritance_Ex9.py` | `Employee` → `Manager` → `AssManager`; 50% bonus and gross salary |
| `Inheritance/MultiLevel Inheritance_Ex10.py` | Only two classes: `B` inherits `A`. Writes x and y to `Myfile.txt`, then reads the file. The file name says multilevel; the code is single inheritance plus file I/O |
| `Inheritance/MultiLevel Inheritance_Ex11.py` | `Student` → `SWStudent` → `ITStudent`; calculates marks, writes `Student.txt` (replaces the file), then reads it |

### Hierarchical inheritance

Two or more child classes inherit the same parent.

| File | What it does |
|------|----------------|
| `Inheritance/Hierarchical Inheritance_Ex1.py` | `B` and `C` both inherit `A`; prints x with y, and x with z |
| `Inheritance/Hierarchical Inheritance_Ex2.py` | `Director` and `Manager` both inherit `Employee` |
| `Inheritance/Hierarchical Inheritance_Ex3.py` | `ItStudent` and `ManagementStudent` both inherit `Student` (marks vs viva and final dates), from input |
| `Inheritance/Hierarchical Inheritance_Ex4.py` | Empty |
| `Inheritance/Hierarchical Inheritance_Ex5.py` | `CommercialCustomer` and `DomesticCustomer` inherit `Customer`. Slab bills, write both to `customers.txt`, then read the file |
| `Inheritance/Hierarchical Inheritance_Ex6.py` | Same two customer types. Loop until code `XXX`. Optional search of `customers.txt` by customer number |

Domestic rates in hierarchical Ex5 and Ex6 are not the same as constructor Ex5. Here the domestic steps are Rs. 3, Rs. 6, Rs. 9, then Rs. 15. Commercial steps stay Rs. 5, Rs. 10, Rs. 15, then Rs. 25.

## Processing with Strings

This folder does not use string methods yet (`split`, `upper`, `find`, slicing, and so on). The files repeat earlier inheritance exercises.

| File | What it does |
|------|----------------|
| `Processing_with_Strings/Processing_with_Strings_Ex1.py` | Single inheritance: `B` inherits `A` and prints x and y |
| `Processing_with_Strings/Processing_with_Strings_Ex2.py` | Same program as `Inheritance/Single Inheritance_Ex2.py` (`Manager` inherits `Employee`) |
| `Processing_with_Strings/Processing_with_Strings_Ex3.py` | Empty |
| `Processing_with_Strings/Processing_with_Strings_Ex4.py` | Same program as `Inheritance/Single Inheritance_Ex4.py` (`ItStudent` inherits `Student`) |

## Review notes

What is in good shape:

- The path is clear: functions, then files, then classes, then inheritance.
- Menus use `match`/`case` and an infinite `while` loop with a real exit option.
- Later class exercises call `super()` and keep parent data in the child.
- Bank withdraw checks the balance before subtracting.
- Bill programs use slabs (each band has its own rate), not one rate for every unit.

Worth fixing when you revise:

- `Hierarchical Inheritance_Ex4.py` and `Processing_with_Strings_Ex3.py` are empty.
- `Processing_with_Strings` still holds inheritance copies. String practice is the next topic to write.
- `Accessor_and_mutator_Ex1.py`: `setName` uses the parameter name `seld` instead of `self`. It still runs. The second print label says `Id` for the name.
- File Ex7 treats average `50` as Pass (`>= 50`). File Ex8 treats `50` as Fail (`> 50`).
- Constructor bills and hierarchical Ex5/Ex6 use different domestic rates. Keep one tariff if both programs should match.
- Many files end statements with `;`. Python allows it, but you do not need it.
- Shared `.txt` names mean a later exercise can append onto an earlier exercise’s file.
