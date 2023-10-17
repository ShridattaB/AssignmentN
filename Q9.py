# 11  21   31   41   51
#                            52
#                            53
#                            54
#                            55

num=int(input("Enter the Number:-"))
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==1 or j==num:
            print(str(j)+str(i),end=" ")
        else:
            print(end="   ")
    print()
