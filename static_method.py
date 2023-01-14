# if we want to define a function jiska samband class ya instance method se na ho t hum static method use karte hai
# hame ese function likhne hoon jisme self ki load hi na ho
# we can use static by useing decorators static method
class Person:
    count_instance=0
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.person_age=age
        Person.count_instance+=1
    @staticmethod
    def hello():
        return "hello world mughe self ki jaroorat nahi hai"
p1=Person("Satish","Kumar",20)
p2=Person("Aryan","Singh",19)
print(Person.count_instance)
print(p1.hello())