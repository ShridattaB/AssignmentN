# 11                        51
#       22         42
#             33
#        24        44
# 15                      55

for i in range(1,6):
    for j in range(1,6):
        if i==j or (j==5,4,3,2,1 and i=1,2,3,4,5):
            print(str(j)+str(i) , end=" ")
        else:
            print(end="   ")
    print()