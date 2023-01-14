class Laptop:
    discount=10
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
        self.laptop_name=brand_name+" "+model_name
    def off(self):
        return self.price-(self.price*(self.discount/100))


# jo class varibale hai use hum baad mai change bhi kar sakte hai
dell=Laptop("Dell","New enspiron 5515",60000)
apple=Laptop("Apple","Mac 5",120000)
# apple.discount=20
# agar hame pta karna ho hamare object ke pass kya kya hai means kon kon se variable hai
print(apple.__dict__)
print(apple.off())
# par abhi bhi discout 20 apply nahi hua
# so we write self.discount


