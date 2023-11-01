# 8:Write a function that takes keyword arguments to
# calculate the area of a rectangle or a circle. It should 
# accept arguments like shape, length, width, and radius.
#     Input: calculate_area(shape="rectangle", length=5, width=4)
#     Expected Output: 20

def calculate_area(shape,length=None,width=None,redius=None):
    if shape=="ractangle":
        area_reactangle=length*width
        print("area of reactangle is " , area_reactangle)
    elif shape=="circle":
        area_of_circle=3.14*redius*redius
        print("area of circlr is " ,area_of_circle)

calculate_area(shape="ractangle",length=5,width=5)
calculate_area(shape="circle",redius=5)
    










