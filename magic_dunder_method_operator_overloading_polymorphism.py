class Phone:
    def __init__(self,barnd,model,price):
        self.brand=barnd
        self.model=model
        self.price=price
    def phone_name(self):
        return f'{self.brand} {self.model}'
    # for print dunder or magic methods are __str__ , __repr__
    def __str__(self):
        return f"{self.brand} {self.model} of pricce {self.price}"
    def __repr__(self):
        return f"Phone('{self.brand}','{self.model}',{self.price})"

    def __len__(self):
        return len(self.brand)

    # operator overloading
    def __add__(self,other):
        return (self.price+other.price)
p1=Phone("nokia","1100",1000)
p2=Phone("nokia","1200",1200)
# if we try to print the p1 it will give location of objject or instance
print(p1+p2)



print(p1)
print(repr(p1))
print(p2.__repr__())
print(str(p1))
print(len(p1))


# polymorphism
# ek cheez ki do se jada form hona
# like len func ko hum str ckass kist class kisi par bhi use kar sakte hai