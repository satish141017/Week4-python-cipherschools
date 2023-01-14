# 1. notimplemented error
# 2.Abstract classs
class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        raise NotImplementedError("you have define a sound class in every subclasses or child classes like def sound(self)")
        # this type of method is called a abstract method 
class Dogesh(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return "Wada wao wao wada wao wao wada wao"
class Bagad_Billa(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
doggy=Dogesh("kallu","vodafone")
billi=Bagad_Billa("billo","kali_billi")
print(doggy.sound())
print(billi.sound())

# as you can see har animal ke liye sound same aa raha ahhi hum chahate hai ki har inherit class hai unhe animal ka sound define karna pade warna error 
# konsa Error    not implement3e3d error