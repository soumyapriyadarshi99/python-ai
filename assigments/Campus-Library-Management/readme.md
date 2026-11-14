Brief
Problem statement
A campus library lends three kinds of items: books, magazines and DVDs. Staff need a program that stores the items, lets members borrow and return them, and refuses invalid actions with clear messages instead of crashing.

Your program must:

Model each item type as its own class, sharing common behaviour through a parent class.

Calculate a late fee that differs per item type (books Rs 2/day, magazines Rs 1/day, DVDs Rs 5/day).

Keep an item's availability and a member's borrowed list private, changed only through methods.

Handle bad input (item already borrowed, borrow limit reached, returning something not borrowed) with exceptions.

Run a short demo in main.py that exercises every feature and prints readable output.

Learning objectives
Each part of the brief maps to a topic from class, so you can revise as you go.

Step-by-step tasks
Work in order and run your code after every step. Each step ends with a checkpoint to confirm it works.

Set up the project.

Create a folder library_manager with main.py and models.py.

Paste the starter code into the matching files.

Checkpoint: python3 main.py runs without errors (on Windows, python main.py).

Build the abstract parent LibraryItem in models.py.

Constructor takes title and item_id; store a private \_\_available = True.

Add a class attribute total_items that increases by 1 in init.

Add is_available(), mark_borrowed() and mark_returned().

Declare late_fee(self, days_late) with @abstractmethod.

Checkpoint: LibraryItem("x", 1) raises a TypeError because the class is abstract.

Create the three child classes.

Book (extra author), Magazine (extra issue_number), DVD (extra duration_minutes).

Each calls super().**init**(title, item_id) and implements late_fee() with its own daily rate.

Add a describe() method to each that returns a one-line description (see Book).

Checkpoint: print(Book("Python 101", 1, "A. Rao").describe()) shows a readable line, and LibraryItem.total_items goes up with each object.

Build the Member class.

Constructor: name, member_id, max_items=3 (default argument); private \_\_borrowed = [].

borrow(item) raises a ValueError with a clear message if the item is taken, or if the limit is reached.

return_item(item, days_late=0) raises a ValueError if the item is not on the member's list, otherwise returns the fee.

borrowed_titles() returns a list of titles without exposing \_\_borrowed.

Checkpoint: borrowing a 4th item, or the same item twice, raises a ValueError with the right message.

Show polymorphism and error handling in main.py.

Create 2 members and one of each item type.

Loop over a mixed list of items and print late_fee(3) for each, with no if on the type.

Wrap borrow and return calls in try / except ValueError as e and print friendly messages.

Checkpoint: the output shows fees of Rs 6, Rs 3 and Rs 15 for 3 days late.

Prove encapsulation and write the reflection.

Try item.\_\_available from outside the class and note the AttributeError; then read availability properly with is_available().

In README.md, answer the three questions in the deliverables section.
