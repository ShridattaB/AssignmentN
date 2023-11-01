values=[1,2,3,4,5]
# multiply by one less than index number
# 1 * -1  = -1
# 2 *  0  =  0
# 3 * (1) =  3
# 4 * (2) =  8
# 5 * (3) =  15
################
#            25



def multiply_element_one_less_than_index(numbers):
    total=0
    for index,numbers in enumerate(numbers):
        total+=numbers * (index-1)
        return total

print(multiply_element_one_less_than_index)