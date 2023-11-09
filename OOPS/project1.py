# Project Title: Online Library Management System

# Project Description:

# Create an online library management system using Python that adheres to Object-Oriented Programming principles to efficiently manage books, library members, and various library operations. This system will offer a user-friendly interface for both librarians and library members, enabling them to perform a wide range of tasks. Here's a more detailed explanation of the key features:

# Book Management:


   
# Class: Book

#         -id
#         -title 
#         -author


   
# Sample Input/Output:
#    > book1 = Book("9780316769488","The Catcher in the Rye", "J.D. Salinger") 
   


class book():
    def __init__(self,id,title,author):
        self.id=id
        self.title=title
        self.author=author

book1 = book("9780316769488","The Catcher in the Rye", "J.D. Salinger")
print(f"id:{book1.id}\nTitle:{book1.title}\nAuthor:{book1.author}")





