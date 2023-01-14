class Mobile:
    def __init__(self,name):
        self.name=name
    
class MobileStore:
    def __init__(self):
        self.mobiles=[]
    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("you can pass only object of Mobile class")
oneplus=Mobile("one plus 6t")
mobo=MobileStore()
mobo.add_mobile(oneplus)
mobil=mobo.mobiles
k=mobo.mobiles[0]
print(k.name)
