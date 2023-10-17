# a
# ab
# abc
# abcd
# abcde
# A=65
num=int(input("Enter the Number:-"))
for i in range(65,num+65):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print()
