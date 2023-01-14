class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.person_age=age
    
    def full_name(self):
        return(self.first_name+" "+self.last_name)
class School_info(Person): #derived or child class
    def __init__(self,first_name,last_name,age,study,subject):
        # Person.__init__(self,first_name,last_name,age)
        super().__init__(first_name,last_name,age)
        self.study=study
        self.subject=subject
    @property
    def full(self):
        return f"{ self.first_name}  {self.last_name}  {self.person_age}  {self.study} {self.subject}  "

p1=School_info("j","k",23,"6th","english")
# print(p1.full)

# multi level inheritance



# method resolution order
# method resolution order har class ka hota hai how to find it or ye kya hota hai print(help(Smaprtphone)) karke dekhlon 
# how pythen find method
# print(help(School_info))

# method overriding
# agr hum inherited class mao new method define karenge to wo over ride ho jayega



# 2 builtin functions
# 1.
# to check if object is of given class
print(isinstance(p1,School_info))

# 2.
# to check subclass
print(issubclass(School_info,Person))




