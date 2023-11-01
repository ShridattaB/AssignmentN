
#file handling we handle the file or we perforam different operation on file line open read  write cloe  something in file
# this is nothing but file handling file is cotainer wehere we stored the data
# there are 
# there are two types of files text and binary file (store photos videos special type of coding human cannot read directly)

#syntax to open file
# file_object=open("filename","mode")
#read # write # append(add something end of the file )R+ w+ a+

# to create a file 
# f1 =open("file1.txt","x")

#read the file
# f1 =open("file1.txt","r")
# data=f1.read()
# print(data)

#w opens the file in write mode if file dones exist then it cerate a new file
# f1 =open("file1.txt","w")
# f1.write("welcome to jenny's lectures")

# r+ mode open the file in raad and write mode both 
#it not create new file if file is dont exist 
# first the content read and then write we use r+ mode 
#print(f.tell()) gives the position of curser

# f1 =open("file1.txt","r+")
# print(f1.read())
# f1.write("This is python course")


#w+ opens in both read and write mode the file handle exist at begining of the file it overwrite
# the previous content of opend file if file is already exst
# it creates a new file if file is doesn't exist 

# f1 =open("file1.txt","w+")
# print(f1.tell())
# f1.write("hi welcome")
# print(f1.tell())
# f1.write("this is python course")
# f1.seek(0)
# print(f1.tell())
# data=f1.read()
# print(f1.tell())
# print(data)
# print(f1.tell())
# f1.close()

#open a file and append the data at end of the file if file is not exist it cretae a new file
# f1 =open("file1.txt","a")
# f1.write("hello_student ")


# a+ mode we can read the file 

f1 =open("file1.txt","a+")
f1.seek(0)
print(f1.read())
f1.write("jennys lecture")
# f1.write("hello_student ")
f1.seek(0)
print(f1.read())


