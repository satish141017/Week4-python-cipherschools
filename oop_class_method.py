class Person:
    tempo=0
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.person_age=age
        Person.tempo+=1
    @classmethod
    def class_instance(cls):
        return f"YOu have made {cls.tempo} instace of this class"
    def full_name(self):
        return(self.first_name+" "+self.last_name)
p1=Person("Satish","Kumar",20)
p2=Person("Aryan","Singh",19)
# we can use class method like   :-      classname.method_name()
print(Person.class_instance())
