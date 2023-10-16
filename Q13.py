# 11                       51
# 12   22               52
# 13        33          53
# 14               44  54
# 15                      55

for i in range(1,6):
    for j in range(1,6):
        if j==1 or i==j or j==5:
            print(str(j)+str(i) , end=" ")
        else:
            print(end="   ")
    print()