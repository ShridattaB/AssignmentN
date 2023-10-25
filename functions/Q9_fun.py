#  Create a function decorator that measures the execution time of another 
# function and prints the time taken.
# The input and expected output for function decorators may 
# vary based on specific use cases and how you implement them. They may
# not have standardized input/output like the previous questions.


#add the extra feature in exsiting function
#we can change behaviour of exsitinf function
def divide(a,b):
    if a<b:
        a,b=b,a
    return a/b
print(divide(10,20))

 