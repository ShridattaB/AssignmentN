class FileHandler():
    def read(url,mode):
        file=open(url,mode)
        data=file.read()
        """"reading the data"""
        print(data)
    def wri(url,mode,text_add):
        file=open(url,mode)
        """"writing the data"""
        file.write(text_add)
    def appen(url,mode,text_append):
        file=open(url,mode)
        """"appending the data"""
        file.write(text_append)
        


