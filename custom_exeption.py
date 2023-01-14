# how to create custum cxeption in py
class NameTooShortError(ValueError):
    pass
def validate(name):
    if len(name)<8:
        raise NameTooShortError("bro  your name is too short write your sir name also")
name=input("Enter your name : ")
validate(name)
print("hello",name)