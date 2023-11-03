# Question 3: Define a Python class "Book" with attributes for title, author, and ISBN. Create an object of the "Book" class and display its title, author, and ISBN.

# Explanation: In this question, you'll create a class to represent a book, create an object of the class, and display the book's title, author, and ISBN.

# Sample Input:
# Title: "Python Programming"
# Author: "John Smith"
# ISBN: "978-1234567890"

class Book():
    def __init__(self,title, author,ISBN):
        self.title=title
        self.author=author
        self.ISBN=ISBN

About_book=Book("Python Programming","John Smith","978-1234567890")
print(f"TItle:{About_book.title}\nAuthor{About_book.author}\nISBN{About_book.ISBN}")