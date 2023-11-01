# 11    21   31   41    51
# 12   22                 52
# 13         33           53
# 14                 44    54
# 15   25  35  45    55

num=int(input("Enter the Number:-"))
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==1 or i==1 or i==num or j==num or i==j:
            print(str(j)+str(i) , end=" ")
        else:
            print(end="   ")
    print()