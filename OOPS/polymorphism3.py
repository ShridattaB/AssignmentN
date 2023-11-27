#means same function but different signature 
#same functions used for different type
l=[10,20,30,40]
print(len(l))

s="welcome"
print(len(s))
#functon overloading
#same function but change class

class ws:
    def displayinfo(self,name=""):
        print("werlcome to ws "+name)

obj=ws()
obj.displayinfo()

obj.displayinfo("python")