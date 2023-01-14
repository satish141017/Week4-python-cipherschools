class Person:
    count_instance=0
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.person_age=age
        Person.count_instance+=1
p1=Person("Satish","Kumar",20)
p2=Person("Aryan","Singh",19)
print(Person.count_instance)