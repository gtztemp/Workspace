# 🐍 Python Beginner Guide

Welcome! If you're just starting to learn programming through Python, this guide will walk you through essential best practices, naming conventions, and the most important rules you should follow as a beginner.

---

## 📌 General Rules to Remember

- **Use meaningful names** for variables and functions.
- **Indent your code properly** (Python uses indentation to define blocks).
- **Comment your code** to explain why (not what) something is done.
- **Follow PEP8** – Python’s style guide.
- **Avoid global variables** as much as possible.

---

## 🧠 Python Naming Conventions

| Element     | Convention         | Example                      |
| ----------- | ------------------ | ---------------------------- |
| Variable    | `snake_case`       | `user_name`, `total_sum`     |
| Constant    | `UPPER_SNAKE_CASE` | `MAX_LIMIT`, `PI`            |
| Function    | `snake_case()`     | `calculate_total()`          |
| Class       | `PascalCase`       | `UserProfile`, `BankAccount` |
| Module/File | `snake_case.py`    | `user_data.py`               |

---

## 🧰 Python Basics to Master

### ✅ Variables

```python
name = "John"
age = 25
```

### ✅ Functions

```python
def greet_user(name):
    print(f"Hello, {name}!")
```

### ✅ Conditionals

```python
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

### ✅ Loops

```python
for i in range(5):
    print(i)
```

### ✅ Lists and Dictionaries

```python
fruits = ["apple", "banana", "cherry"]
user = {"name": "Alice", "age": 30}
```

---

## 🧼 Clean Code Tips

- Keep functions **short and specific**.
- Avoid hardcoding values; use **constants**.
- Use **docstrings** to describe functions.
- Don’t repeat yourself – **reuse code**.

---

## 🧪 Testing Your Code

Start using simple `assert` statements:

```python
def add(a, b):
    return a + b

assert add(2, 3) == 5
```

---

## 🚀 Good Habits

- Use a code editor like VS Code or PyCharm.
- Run your code often.
- Practice daily with small projects.
- Use version control (Git) early on.

---

## 📚 Suggested Topics After Basics

1. File Handling
2. Error Handling with `try`/`except`
3. Object-Oriented Programming (OOP)
4. Working with External Libraries (e.g., `requests`, `pandas`)
5. Writing Tests with `unittest` or `pytest`

---

> 🎯 **Remember:** Focus on writing readable, working code. As you grow, style and optimization will come naturally!


