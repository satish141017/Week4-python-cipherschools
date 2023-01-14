def add(num1,num2):
    if (type(num1) is int) and (type(num2) is int):
        return num1 + num2
    raise TypeError("this function takes only int type")
print(add("4","5"))