class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"Borrowed book: {self.title} by {self.author}")
        else:
            print("Book is not available")
    def return_book(self):
        self.available = True
        print(f"Returned book: {self.title} by {self.author}")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print("Book is not available")
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print("Book not borrowed by user")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title} by {book.author}")
    def register_user(self, user):
        self.users.append(user)
        print(f"Registered user: {user.name} with ID {user.user_id}")
    def show_available_books(self):
        print("Available books:")
        for book in self.books:
            if book.available:
                print(f"{book.title} by {book.author}")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

user1 = User("Alice", 1)
user2 = User("Bob", 2)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.register_user(user1)
library.register_user(user2)

library.show_available_books()