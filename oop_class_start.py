class Person:
    def __init__(self,first_name,last_name,age):
        # ab hum instance variables declear karenge
        # self represent onject aur constructor
        # hum har jagah self ki jagah kuch aur bhi likh sakte hain
        # like self ki jagah person instance bhi likh sakte hain
        print("init method // counstructor get called")
        self.first_name=first_name
        self.last_name=last_name
        self.person_age=age
    # thats how we just created a simple class
p1=Person("Satish","Kumar",20)
p2=Person("Aryan","Singh",19)
print(p1.first_name)
print(p1.last_name)
print(p1.person_age)
print(p2.first_name)
print(p2.last_name)
print(p2.person_age)