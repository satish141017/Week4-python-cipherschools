class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.person_age=age
    @classmethod
    def string_slicer(cls,string):
        first,last,age=string.split(",")
        return cls(first,last,age)
    
    def full_name(self):
        return(self.first_name+" "+self.last_name)
p1=Person("Satish","Kumar",20)
p2=Person("Aryan","Singh",19)
# how can we make a constructor like init
# now we can also pass like
p3=Person.string_slicer("Satish,kumar,45")
print(p3.full_name())