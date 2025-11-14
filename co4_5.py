# Base class
class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher Name:", self.name)


# Derived class
class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)  # invoking base class constructor
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Book Title:", self.title)
        print("Author:", self.author)


# Derived class
class PythonBook(Book):
    def __init__(self, name, title, author, price, number_of_pages):
        super().__init__(name, title, author)
        self.price = price
        self.number_of_pages = number_of_pages

    # Method overriding
    def display(self):
        super().display()
        print("Price:", self.price)
        print("Number of Pages:", self.number_of_pages)


# -------- MAIN PROGRAM --------

pub_name = input("Enter Publisher Name: ")
title = input("Enter Book Title: ")
author = input("Enter Author Name: ")
price = float(input("Enter Book Price: "))
pages = int(input("Enter Number of Pages: "))

# Creating object
python_book = PythonBook(pub_name, title, author, price, pages)

print("\n---- PYTHON BOOK DETAILS ----")
python_book.display()


