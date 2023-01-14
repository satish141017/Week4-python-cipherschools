class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
        self.laptop_name=brand_name+" "+model_name
    def off(self,num1):
        return self.price-(self.price*(num1/100))
dell=Laptop("Dell","New enspiron 5515",60000)
apple=Laptop("Apple","Mac 5",120000)
disc=float(input("Your Discount is (in%) : "))
print(f"Your new price for {dell.laptop_name} is {dell.off(disc)}")
print(f"Your new price for {apple.laptop_name} is {apple.off(disc)}")
