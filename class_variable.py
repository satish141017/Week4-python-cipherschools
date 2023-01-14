# class variables are variales which are same for every instance(object)
class Circle:
    pi=3.14
    # pi is same for every radii of circle
    def __init__(self,radius):
        self.r=radius
    def cicumfrence(self):
        print(2*Circle.pi*self.r)
        # because pi is class variable that's why we write class name in front of it
c1=Circle(5)
print(c1.cicumfrence())