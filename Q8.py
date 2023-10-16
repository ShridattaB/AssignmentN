# 11
# 12
# 13
# 14
# 15   25  35  45  55

num=5
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==5 or j==1:
            print(str(j)+str(i),end=" ")
        else:
            print(end=" ")
    print()