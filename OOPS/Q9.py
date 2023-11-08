# Question 4: Create a class Book with attributes title and author. Create an object to represent a book and display its details.

#    Sample Input:
#    book1 = Book("To Kill a Mockingbird", "Harper Lee")
#    Sample Output
#    Book Title: To Kill a Mockingbird
#    Author: Harper Lee
#    Explanation: Here, you define a class to represent a book and create an object to display its details.

class book():
   def __init__(self,Title,Author):
      self.Title=Title
      self.Author=Author

book1=book("To Kill a Mockingbird", "Harper Lee")
print(f"Book_title{book1.Title}\nBook_Author{book1.Author}")