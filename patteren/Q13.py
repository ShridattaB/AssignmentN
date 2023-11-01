# 11                       51
# 12   22               52
# 13        33          53
# 14               44  54
# 15                      55
num=int(input("Enter the Number:-"))
for i in range(1,6):
    for j in range(1,6):
        if j==1  or j==num or i==j:
            print(str(j)+str(i) , end=" ")
        else:
            print(end="   ")
    print()