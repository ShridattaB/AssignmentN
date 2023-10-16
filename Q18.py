# 11        31
#       22
# 11        33 
i=3
j=3
for m in range(1,i+1):
    for n in range(1,j+1):
        if m==n:
            print(str(n)+str(m),end=" ")
        else:
            print(end=" ")
    print()