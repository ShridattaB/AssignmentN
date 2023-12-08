from fileoperation import FileHandler  
file=FileHandler.read("file3.txt","r")

file2=FileHandler.wri("file3.txt","w","This is new written")

file3=FileHandler.appen("file3.txt","a","\nthis is second line append")

file4=FileHandler.read("file3.txt","r")






