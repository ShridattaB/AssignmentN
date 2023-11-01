# 11                        51
#       22         42
#             33
#        24        44
# 15                      55
num=int(input("Enter the Number:-"))
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==j or i+j==num+1:
            print(str(j)+str(i) , end=" ")
        else:
            print(end="   ")
    print()