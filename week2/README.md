# Week 2 – Exception Handling & File I/O

## 1. Introduction (15 minutes)
- **Quick Recap (Week 1 – OOP basics).**
- **Discussion:** What happens if a program crashes due to errors?
- **Real-world examples:**
  - ATM transaction logs  
  - Online form submissions  
  - File corruption handling
- **Transition to topic:** Why we need error handling and file I/O.

---

## 2. Lecture & Demo (45 minutes)

### a. Exception Handling Basics
- **Why errors occur**
  - Syntax errors (caught before running)
  - Runtime errors (occur during execution)
- **Keywords**
  - `try` → wrap code that might fail
  - `except` → handle the error
  - `else` → runs if no error occurs
  - `finally` → always runs (cleanup tasks)
  - `raise` → manually trigger an error
- **Common Exceptions**
  - `ValueError`
  - `FileNotFoundError`
  - `ZeroDivisionError`

**Demo Example:**
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("Division successful:", result)
finally:
    print("Program finished.")


---



