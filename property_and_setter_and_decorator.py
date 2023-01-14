class Phone:
    def __init__(self,band_name,model_name,price):
        self.band_name=band_name
        self.model_name=model_name
        self._price=max(price,0)
        # if price>0:
        #     self._price=price
        # else:
        #     self._price=0
        # self.total_specification=f'{band_name} {model_name} price is {price}'
    @property #getter()
    def total_specification(self):
        return f'{self.band_name} {self.model_name} price is {self._price}'
    
    # setter()
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,new_price):
        self._price=max(new_price,0)
        
    def make_a_call(self,phone_no):
        return f"calling {phone_no}"
# 1.now can't change price to negative
p1=Phone("Nokia","1100",1250)
p1.price=-500
print(p1.price)

# but total specification mai price update nahi hoga  how to solve this problem hum total_specification name se ek method define karenge fir use property mai chnage kar denge