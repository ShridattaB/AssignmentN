# Member Management:


   
# Class: Member

#         -Member-id
#         -name
#         -contact_info
#           type   #must be  'Admin'  or 'User'

   
# Sample Input/Output:
#     > member1 = Member(1,"John Doe", "john.doe@email.com",'user') 
   
 
# Steps to Implement:

# Create the Book class .
# Create the Member class .
# member type eather 'user' or 'Admin'


# Example to solve 2nd Question

# class Person:
#      def __init__(self, name, age):
#         if age > 18:
#             self.name = name
#             self.age = age
#         else:
#             print('error')
            
# p1 = Person("John", 6)


class Member():
    def __init__(self,member,name,info,type):
        if type =="Admin" or type=="user":
            self.type=type
            self.member_id=member
            self.name=name
            self.Contact_info=info
        

member1 = Member(1,"John Doe", "john.doe@email.com",'user') 
print(f"id:{member1.member_id}\nName:{member1.name}\nContact_info:{member1.Contact_info}\nType:{member1.type}")



#         -name
#         -contact_info
#           type 


