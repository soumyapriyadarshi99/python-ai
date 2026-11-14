# Campus Library Management

A Python OOP project for a campus library system: lends books, magazines, and DVDs to members, tracks availability, calculates late fees, and handles invalid actions with clear exceptions instead of crashing.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Class Design](#class-design)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Example Output](#example-output)
- [Step-by-Step Development Guide](#step-by-step-development-guide)
- [Checkpoints Summary](#checkpoints-summary)
- [Deliverables / Reflection](#deliverables--reflection)
- [License](#license)

---

## Overview

A campus library lends three kinds of items: **books**, **magazines**, and **DVDs**. Staff need a program that stores the items, lets members borrow and return them, and refuses invalid actions with clear messages instead of crashing. The program demonstrates core object-oriented programming concepts: inheritance, abstraction, encapsulation, polymorphism, class attributes, and exception handling.

---

## Features

| Feature | Description |
|---------|-------------|
| **Abstract parent class** | `LibraryItem` cannot be instantiated directly; forces children to define `late_fee()` |
| **Three item types** | `Book`, `Magazine`, `DVD` — each with its own extra field and late fee rate |
| **Late fee calculation** | Books: Rs 2/day, Magazines: Rs 1/day, DVDs: Rs 5/day |
| **Encapsulation** | `__available` and `__borrowed` are private; changed only through methods |
| **Class attribute** | `total_items` counts every item created across all types |
| **Borrow validation** | Rejects already-borrowed items and borrow-limit overflows with `ValueError` |
| **Return validation** | Rejects returning items not borrowed with `ValueError` |
| **Polymorphism** | One loop over mixed item types calls `late_fee()` with no type checks |

---

## Project Structure

```
Campus-Library-Management/
├── .gitignore
├── readme.md
├── models.py
└── main.py
```

---

## Class Design

### `LibraryItem` (Abstract Parent)

The base blueprint for every library item. It is **abstract** — you cannot create a plain `LibraryItem` directly.

| Attribute/Method | Type | Description |
|------------------|------|-------------|
| `total_items` | Class attribute | Shared counter incremented in `__init__` |
| `__available` | Private attribute | Starts `True`; tracks whether the item is on the shelf |
| `__init__(title, item_id)` | Constructor | Sets title, item_id, availability; increments `total_items` |
| `is_available()` | Method | Returns `True` if the item can be borrowed |
| `mark_borrowed()` | Method | Sets availability to `False` |
| `mark_returned()` | Method | Sets availability to `True` |
| `late_fee(days_late)` | Abstract method | **Must** be implemented by every child class |

**Why abstract?** A generic "library item" doesn't exist — every item is specifically a Book, Magazine, or DVD, each with its own late fee rate.

---

### `Book`

| Attribute | Value |
|-----------|-------|
| Extra field | `author` |
| Late fee rate | Rs 2 per day |

```python
Book("Python 101", 1, "A. Rao")
```

---

### `Magazine`

| Attribute | Value |
|-----------|-------|
| Extra field | `issue_number` |
| Late fee rate | Rs 1 per day |

```python
Magazine("Science Weekly", 2, 42)
```

---

### `DVD`

| Attribute | Value |
|-----------|-------|
| Extra field | `duration_minutes` |
| Late fee rate | Rs 5 per day |

```python
DVD("The Matrix", 3, 136)
```

---

### `Member`

Represents a library member who can borrow and return items.

| Attribute/Method | Type | Description |
|------------------|------|-------------|
| `name` | Attribute | Member's name |
| `member_id` | Attribute | Member's ID number |
| `max_items` | Attribute | Maximum borrowable items (default: 3) |
| `__borrowed` | Private attribute | List of currently borrowed items |
| `borrow(item)` | Method | Borrows an item; raises `ValueError` if unavailable or limit reached |
| `return_item(item, days_late=0)` | Method | Returns an item; raises `ValueError` if not borrowed; returns late fee |
| `borrowed_titles()` | Method | Returns a list of borrowed titles (without exposing `__borrowed`) |

---

## Installation & Setup

1. Navigate to the project folder:

   ```bash
   cd /Users/soumyapriyadarshidas/Learning/python-ai/assigments/Campus-Library-Management
   ```

2. Ensure Python 3 is installed:

   ```bash
   python3 --version
   ```

3. No external dependencies are required — only Python standard library (`abc`).

---

## Usage

Run the demo program:

```bash
python3 main.py
```

### What `main.py` demonstrates

1. **Creating items and members** — one Book, one Magazine, one DVD; two Members (Alice and Bob)
2. **Borrowing with error handling** — Alice borrows items; Bob tries to borrow an already-taken book
3. **Borrow-limit enforcement** — Alice tries to borrow a 4th item
4. **Return validation** — Bob tries to return an item he never borrowed
5. **Polymorphism** — one loop over all three item types prints late fees with no `if/else` on type
6. **Class attribute** — prints total number of items created
7. **Encapsulation proof** — direct access to `__available` raises `AttributeError`; `is_available()` works

---

## Example Output

```
Alice borrowed: Book: Python 101 by A. Rao (ID 1) Available: False
Could not borrow: 'Python 101' is already borrowed.
Alice borrowed: Magazine: Science Weekly, Issue 42 (ID 2) Available: False
Alice borrowed: DVD: The Matrix, Duration 136 mins (ID 3) Available: False
Could not borrow: Alice has reached the borrow limit of 3 items.
Could not return: Bob did not borrow 'Science Weekly'.
Book: Python 101 by A. Rao (ID 1) Available: False -> late fee for 3 days: Rs 6
Magazine: Science Weekly, Issue 42 (ID 2) Available: False -> late fee for 3 days: Rs 3
DVD: The Matrix, Duration 136 mins (ID 3) Available: False -> late fee for 3 days: Rs 15
Total items created: 4

--- Encapsulation demo ---
Direct access failed (private): 'Book' object has no attribute '__available'
Proper access via is_available(): False
```

---

## Step-by-Step Development Guide

Work in order and run your code after every step.

### Step 1 — Set Up the Project

Create `models.py` and `main.py` directly inside `Campus-Library-Management/`.

> **Checkpoint:** `python3 main.py` runs without errors.

### Step 2 — Build `LibraryItem` (Abstract Parent)

- Constructor takes `title` and `item_id`; store private `__available = True`
- Add class attribute `total_items` that increments in `__init__`
- Add `is_available()`, `mark_borrowed()`, `mark_returned()`
- Declare `late_fee(days_late)` with `@abstractmethod`

> **Checkpoint:** `LibraryItem("x", 1)` raises a `TypeError` because the class is abstract.

### Step 3 — Create the Three Child Classes

- **Book** (extra `author`)
- **Magazine** (extra `issue_number`)
- **DVD** (extra `duration_minutes`)

Each calls `super().__init__(title, item_id)` and implements `late_fee()` with its own daily rate. Add a `describe()` method to each.

> **Checkpoint:** `print(Book("Python 101", 1, "A. Rao").describe())` shows a readable line, and `LibraryItem.total_items` increases with each object.

### Step 4 — Build the `Member` Class

- Constructor: `name`, `member_id`, `max_items=3`; private `__borrowed = []`
- `borrow(item)` raises `ValueError` if item is taken or limit is reached
- `return_item(item, days_late=0)` raises `ValueError` if item not borrowed; otherwise returns the fee
- `borrowed_titles()` returns a list of titles without exposing `__borrowed`

> **Checkpoint:** Borrowing a 4th item, or the same item twice, raises a `ValueError` with the right message.

### Step 5 — Polymorphism and Error Handling in `main.py`

- Create 2 members and one of each item type
- Loop over a mixed list of items and print `late_fee(3)` with no `if` on type
- Wrap borrow/return calls in `try / except ValueError as e`

> **Checkpoint:** Output shows fees of Rs 6, Rs 3, and Rs 15 for 3 days late.

### Step 6 — Prove Encapsulation & Write Reflection

- Try `item.__available` from outside the class; note the `AttributeError`
- Read availability properly with `is_available()`
- Answer the three questions in the **Deliverables** section below

---

## Checkpoints Summary

| # | Checkpoint | Status |
|---|------------|--------|
| 1 | `python3 main.py` runs without errors | ✅ |
| 2 | `LibraryItem("x", 1)` raises `TypeError` | ✅ |
| 3 | `Book(...).describe()` prints readable line; `total_items` increases | ✅ |
| 4 | Borrowing 4th item or same item twice raises `ValueError` | ✅ |
| 5 | Late fees: Book Rs 6, Magazine Rs 3, DVD Rs 15 | ✅ |
| 6 | `book.__available` raises `AttributeError`; `is_available()` works | ✅ |

---

## Deliverables / Reflection

### 1. Why is `LibraryItem` an abstract class?

`LibraryItem` is abstract because you should never create a plain "library item" by itself — every item in the library is specifically a Book, Magazine, or DVD. Making it abstract (with `@abstractmethod` on `late_fee()`) forces every child class to define its own late fee calculation. If you try `LibraryItem("x", 1)`, Python raises a `TypeError`, which prevents invalid or incomplete objects from being created.

### 2. Why are `__available` and `__borrowed` private?

They are private (double underscore prefix) so they can only be changed through controlled methods, never directly from outside the class.

- **`__available`**: Only `mark_borrowed()` and `mark_returned()` should change availability. If outside code could set `item.__available = True` directly, it could mark a borrowed item as available without going through the return process, breaking the library's rules.
- **`__borrowed`**: Only `borrow()` and `return_item()` should modify the borrowed list. They enforce validation (availability check, borrow limit, return check). If outside code could append to `__borrowed` directly, a member could bypass limits or borrow items that are already taken.

Private attributes ensure the object's internal state stays consistent and all business rules are enforced.

### 3. How does polymorphism help in `main.py`?

Polymorphism lets you treat Book, Magazine, and DVD objects the same way through their shared parent interface. In `main.py`, you can put all three in one list and call `item.late_fee(3)` without checking what type each item is:

```python
items = [book, magazine, dvd]
for item in items:
    print(item.late_fee(3))  # Rs 6, Rs 3, Rs 15 — no if/else needed
```

Python automatically calls the correct `late_fee()` for each object. This means if you add a new item type later (e.g., Journal), the loop still works without any changes — you only need to add the new class.

---

## License

This project is for educational purposes as part of a Python OOP assignment.
