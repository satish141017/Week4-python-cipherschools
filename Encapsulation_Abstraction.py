# Encapsilation means hane jo data likha hai uski functanility ko ek hi jagah likhna
# abstraction means hiding a complexicity prospective of user
# list ko sort karne ke kayee method hotte hai pyten mai tim sort use hota jo list class me method banaya gya hoga
# some speccial naming conventions 
# har language mai kuch private variable hotee hai kuch public
# but in python sare hi public hote hai




# convention for developers :
# hum python mai _varname likhte hai jaha _ batata hai ki ye private variable hai iske satth chhed chhad na kare
#  __name__ double underscore or dunders or also magic methods

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.__person_age=age
    
    def full_name(self):
        return(self.first_name+" "+self.last_name)
p1=Person("Satish","Kumar",20)
p2=Person("Aryan","Singh",19)
print(p1.__dict__)
# you we see hame person ke age jo __ lagaya hai wo ese _Person__person_age change kar dega
print(p1._Person__person_age)