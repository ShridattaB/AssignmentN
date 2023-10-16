
# 11   12   13   14   15
# 21  22   23  24  25
# 31  32   33  34  35
# 41  42   43  44  45
# 51  52   53  54  55
# num=6
# for i in range(1,num):
#     for j in range(1,num):
#         if(i==j):
#             print(str(i)+str(j),end=" ")
#         else:
#             print(end=" ")
#     print()
# 11
# 12
# 13
# 14
# 15   25  35  45  55
num=6
for i in range(1,num):
    for j in range(1,num):
        if(i==1):
            print(str(i)+str(j),end=" ")
        else:
            print(end=" ")
    print()



