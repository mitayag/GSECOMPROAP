# 📌 Deliverable: Expense Tracker with Error Handling

## 📖 Project Description
Build a Python program called **`expense_tracker.py`** that helps users record and view daily expenses while practicing **exception handling** and **file I/O**.

---

## ✅ Requirements

### 1. User Menu
The program should present a simple text-based menu:

### 2. Features
- **Add Expense**
  - Ask user for: `date (YYYY-MM-DD)`, `category`, `amount`.
  - Handle invalid input:
    - Wrong date format → show error message.
    - Non-numeric amount → show error message.
    - Negative amounts → not allowed, raise error.
- **View All Expenses**
  - Display records from `expenses.csv`.
  - If file missing, create it with headers (`Date,Category,Amount`).
- **Search Expense by Date**
  - Ask for a date and display all matching entries.
  - Handle invalid dates or no matching records gracefully.
- **Exit**
  - End program safely.

---

## ⚠️ Error Handling Requirements
- Use `try`, `except`, `else`, and `finally` where appropriate.
- Catch and handle:
  - `ValueError` (invalid numbers, invalid date input).
  - `FileNotFoundError` (if `expenses.csv` doesn’t exist).
- Use `raise` to enforce rules:
  - Negative amounts → `raise ValueError("Amount cannot be negative.")`.

---

## 📂 Deliverables
1. **Source Code** → `expense_tracker.py`  
2. **Sample Data File** → `expenses.csv`  
   Example:

3. **Short Reflection (150–200 words)**  
- What errors did you test?  
- Why is exception handling important for this program?

---

## 📊 Grading Rubric

| Criteria            | Excellent (5) | Good (3) | Needs Improvement (1) |
|---------------------|---------------|----------|------------------------|
| Exception Handling  | Anticipates all errors, uses keywords effectively | Handles most errors correctly | Few or no error checks |
| File Handling       | Creates/reads/writes CSV reliably | Works but sometimes fails | Frequent file issues |
| Functionality       | All menu features work correctly | Missing one feature | Multiple features missing |
| Reflection          | Thoughtful and clear, connects errors to reliability | Some insights but shallow | Minimal or off-topic |

---
