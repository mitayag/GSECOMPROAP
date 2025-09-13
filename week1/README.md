# 🚀 Week 1 – Object-Oriented Programming (OOP) Concepts & Design

## 📘 Overview
This lesson introduces **Object-Oriented Programming (OOP)** concepts using simple analogies, Python examples, and UML diagrams.  
By the end of this lesson, you’ll understand the core pillars of OOP and apply them in designing a small class hierarchy.

---

## 🎯 Learning Objectives
- Understand and explain **Encapsulation, Inheritance, Polymorphism, and Abstraction**.  
- Differentiate between **Abstract Classes** and **Interfaces**.  
- Create and interpret **basic UML class diagrams**.  
- Apply OOP principles by building a simple project.  

---

## 🔑 OOP Concepts

### 🔒 Encapsulation
Encapsulation means **hiding details** and exposing only what’s necessary.

**Analogy:** A vending machine. You insert coins and press buttons without knowing its internal mechanics.  

**Python Example:**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # 150
