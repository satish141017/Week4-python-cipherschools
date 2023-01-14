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
print(p1.full)