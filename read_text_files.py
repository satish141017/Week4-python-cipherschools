# readfile
# open function
# read  method
# seek  method   to change the position of the cursor
# tell method    to check where is our curser right now
# readline method  to read oneline one time
# readlines method  to read lines  it store lines as a string
# close method


# f=open('temp_file.txt') # default file ko hum read kar sakte hai
f=open(r"D:\pythen cipher school\Week4-Python-Cipherschools\temptexts\kamlesh.txt")
# we can also iterate this f object 

# print(f"cursor position : {f.tell()}")
# print(f.read()) 


# print(f.read()) 
# print("Before seek method ")
# print(f"cursor position : {f.tell()}")
# f.seek(0)
# print("After seek method")
# print(f"cursor position : {f.tell()}")



# print(f.readline(),end="")
# print(f.readline(),end="")
# print(f.readline(),end="")

list1=f.readlines()
print(list1)
print(len(list1))

# we can also use loops


# descripters: 1. name 2. closed    inke baad apko () lagane ki need nahi hoteee
print(f.name)
print(f.closed) # to check if file is closed


f.close()