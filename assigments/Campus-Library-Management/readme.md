# Campus Library Management

## Brief

### Problem Statement

A campus library lends three kinds of items: **books**, **magazines**, and **DVDs**. Staff need a program that:

- Stores the items
- Lets members borrow and return them
- Refuses invalid actions with clear messages instead of crashing

### Requirements

Your program must:

1. Model each item type as its own class, sharing common behaviour through a parent class.
2. Calculate a late fee that differs per item type:
   - Books: Rs 2/day
   - Magazines: Rs 1/day
   - DVDs: Rs 5/day
3. Keep an item's availability and a member's borrowed list **private**, changed only through methods.
4. Handle bad input (item already borrowed, borrow limit reached, returning something not borrowed) with exceptions.
5. Run a short demo in `main.py` that exercises every feature and prints readable output.

---

## Learning Objectives

Each part of the brief maps to a topic from class, so you can revise as you go:

| Concept | Where It Appears |
|---------|-----------------|
| Abstract base class | `LibraryItem` parent class |
| Encapsulation (private attributes) | `__available`, `__borrowed` |
| Class attribute | `total_items` |
| Polymorphism | `late_fee()` called on mixed item types |
| Exception handling | `try / except ValueError` |

---

## Step-by-Step Tasks

Work in order and run your code after every step. Each step ends with a checkpoint to confirm it works.

### 1. Set Up the Project

Create `models.py` and `main.py` directly inside the `Campus-Library-Management` folder. Paste the starter code into the matching files.

**Checkpoint:** `python3 main.py` runs without errors.

### 2. Build the Abstract Parent `LibraryItem` in `models.py`

- Constructor takes `title` and `item_id`; store a private `__available = True`.
- Add a class attribute `total_items` that increases by 1 in `__init__`.
- Add `is_available()`, `mark_borrowed()` and `mark_returned()`.
- Declare `late_fee(self, days_late)` with `@abstractmethod`.

**Checkpoint:** `LibraryItem("x", 1)` raises a `TypeError` because the class is abstract.

### 3. Create the Three Child Classes

- **Book** (extra `author`)
- **Magazine** (extra `issue_number`)
- **DVD** (extra `duration_minutes`)

Each calls `super().__init__(title, item_id)` and implements `late_fee()` with its own daily rate. Add a `describe()` method to each that returns a one-line description.

**Checkpoint:** `print(Book("Python 101", 1, "A. Rao").describe())` shows a readable line, and `LibraryItem.total_items` goes up with each object.

### 4. Build the `Member` Class

- Constructor: `name`, `member_id`, `max_items=3` (default argument); private `__borrowed = []`.
- `borrow(item)` raises a `ValueError` with a clear message if the item is taken, or if the limit is reached.
- `return_item(item, days_late=0)` raises a `ValueError` if the item is not on the member's list, otherwise returns the fee.
- `borrowed_titles()` returns a list of titles without exposing `__borrowed`.

**Checkpoint:** Borrowing a 4th item, or the same item twice, raises a `ValueError` with the right message.

### 5. Show Polymorphism and Error Handling in `main.py`

- Create 2 members and one of each item type.
- Loop over a mixed list of items and print `late_fee(3)` for each, with no `if` on the type.
- Wrap borrow and return calls in `try / except ValueError as e` and print friendly messages.

**Checkpoint:** The output shows fees of Rs 6, Rs 3 and Rs 15 for 3 days late.

### 6. Prove Encapsulation and Write the Reflection

- Try `item.__available` from outside the class and note the `AttributeError`; then read availability properly with `is_available()`.
- In `README.md`, answer the three questions in the **Deliverables** section below.

---

## Deliverables

### 1. Why is `LibraryItem` an abstract class?

`LibraryItem` is abstract because you should never create a plain "library item" by itself — every item in the library is specifically a Book, Magazine, or DVD. Making it abstract (with `@abstractmethod` on `late_fee()`) forces every child class to define its own late fee calculation. If you try `LibraryItem("x", 1)`, Python raises a `TypeError`, which prevents invalid or incomplete objects from being created.

### 2. Why are `__available` and `__borrowed` private?

They are private (double underscore prefix) so they can only be changed through controlled methods, never directly from outside the class.

- `__available`: Only `mark_borrowed()` and `mark_returned()` should change availability. If outside code could set `item.__available = True` directly, it could mark a borrowed item as available without going through the return process, breaking the library's rules.
- `__borrowed`: Only `borrow()` and `return_item()` should modify the borrowed list. They enforce validation (availability check, borrow limit, return check). If outside code could append to `__borrowed` directly, a member could bypass limits or borrow items that are already taken.

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


## File Structure

```
Campus-Library-Management/
├── .gitignore
├── readme.md
├── models.py
└── main.py
```

### How to Run

```bash
cd /Users/soumyapriyadarshidas/Learning/python-ai/assigments/Campus-Library-Management
python3 main.py
```
