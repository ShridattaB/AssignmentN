# 11    21   31   41    51
# 12   22                 52
# 13         33           53
# 14                 44    54
# 15   25  35  45    55

for i in range(1,6):
    for j in range(1,6):
        if j==1 or i==j or i==1 or j==5 or i==5:
            print(str(j)+str(i) , end=" ")
        else:
            print(end="   ")
    print()