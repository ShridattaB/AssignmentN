# 000000
# 0           0
# 0           0
# 0           0
# 0           0
# 000000

num=5
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==1 or j==5 or j==1 or i==5:
            print("0",end=" ")
        else:
            print(end="  ")
    print()