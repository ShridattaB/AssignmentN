# 11  21   31   41   51
# 12  22         42  52
# 13         33         53
# 14  24        44  54
# 15  25  35  45  55

for i in range(1,6):
    for j in range(1,6):
        if j==1 or i==1 or j==5 or i==5 or i==j or(j==4 and i==2) or (j==2 and i==4):
            print(str(j)+str(i) , end=" ")
        else:
            print(end="   ")
    print()