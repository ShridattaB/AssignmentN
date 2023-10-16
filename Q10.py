
# 11  21   31   41   51
# 12                      52
# 13                      53
# 14                       54
# 15  25  35  45  55

num=5
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==1 or j==5 or j==1 or i==5:
            print(str(j)+str(i),end=" ")
        else:
            print(end="   ")
    print()