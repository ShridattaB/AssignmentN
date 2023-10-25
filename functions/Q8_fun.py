# 8:Write a function that takes keyword arguments to
# calculate the area of a rectangle or a circle. It should 
# accept arguments like shape, length, width, and radius.
#     Input: calculate_area(shape="rectangle", length=5, width=4)
#     Expected Output: 20

def calculateArea(shape,length=None,width=None,radius=None):
    if shape== "reactangle":
        return length * width
    elif shape=="circle":
        return 3.14* radius**2
    else:
        return "invalide"
    
print(calculateArea(shape="reactangle",length=5,width=4))






