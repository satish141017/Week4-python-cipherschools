class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.person_age=age
    # now we define full naame method in class
    def full_name(self):
        return(self.first_name+" "+self.last_name)
p1=Person("Satish","Kumar",20)
p2=Person("Aryan","Singh",19)
print(p1.full_name())
print(p2.full_name())
print(Person.full_name(p1))
# asal mai ye cheez aise ho rahe hotee hai
# i give a good example
l=[2,3,4,5,6]
# if we use clear method how we use it
# l.clear()
# print(l)
list.clear(l)
print(l)
# *********************************************************
# append wala case
list.append(l,"Satish")
print(l)