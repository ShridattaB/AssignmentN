# 11  21   31   41   51
# 12  22  32  42  52
# 13  23  33  43  53
# 14  24  34  44  54
# 15  25  35  45  55

num=5
for i in range(1,num+1):
    for j in range(1,num+1):
        print(str(j)+str(i),end=" ")
    print()