from models import Book, Member, Magazine, DVD, LibraryItem

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Science Weekly", 2, 42)
dvd = DVD("The Matrix", 3, 136)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# 1. Borrowing with error handling
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

# 2. Trigger the borrow-limit error and the not-borrowed error, catching each
try:
    alice.borrow(magazine)
    print("Alice borrowed:", magazine.describe())
    alice.borrow(dvd)
    print("Alice borrowed:", dvd.describe())
    alice.borrow(Book("Extra Book", 4, "Someone"))  # should fail: limit reached
except ValueError as e:
    print("Could not borrow:", e)

try:
    bob.return_item(magazine)  # Bob never borrowed this
except ValueError as e:
    print("Could not return:", e)

# 3. Polymorphism: one loop, no type checks
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

# 4. Class attribute shared by all objects
print("Total items created:", LibraryItem.total_items)

# 5. Encapsulation demo
print("\n--- Encapsulation demo ---")
try:
    print(book.__available)
except AttributeError as e:
    print("Direct access failed (private):", e)
print("Proper access via is_available():", book.is_available())