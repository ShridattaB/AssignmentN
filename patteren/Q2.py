# 000000
# 0           0
# 0           0
# 0           0
# 0           0
# 000000

# num=int(input("Enter the Number:-"))
# for i in range(1,num+1):
#     for j in range(1,num+1):
#         if i==1 or j==1 or i==num or j==num:
#             print("0",end=" ")
#         else:
#             print(end="  ")
#     print()


num=int(input("Enter the Number:-"))
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==1 or j==1 or i==num or j==num:
            print("0",end=" ")
        else:
            print(end="  ")
    print()