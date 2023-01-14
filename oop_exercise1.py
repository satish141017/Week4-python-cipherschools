class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
        self.laptop_name=brand_name+" "+model_name
dell=Laptop("Dell","New enspiron 5515",60000)
apple=Laptop("Apple","Mac 5",120000)
print(f"{dell.laptop_name}    :  you want {dell.brand_name} {dell.model_name} with price {dell.price} ")
print("or")
print(f"{apple.laptop_name}    :  you want {apple.brand_name} {apple.model_name} with price {apple.price}")