# 11
# 12  22
# 13       33
# 14              44 
# 15                   55

num=int(input("Enter the Number:-"))
for i in range(1,num+1):
    for j in range(1,num+1):
        if j==1 or i==j:
            print(str(j)+str(i) , end=" ")
        else:
            print(end="  ")
    print()