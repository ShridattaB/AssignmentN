# 11
#     22
#          33
#               44
#                    55

num=int(input("Enter the Number:-"))
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==j:
            print(str(j)+str(i),end=" ")
        else:
            print(end=" ")
    print()