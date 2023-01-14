# Multiple inheritance means we can inherit multiple vlas at a same timr
# we generallly dont use ite
# generally use for patterns
class A:
    def class_a(self):
        return "This is Class A method"
class B:
    def class_b(self):
        return "This is Class B method"
class C(A,B):
    pass
c=C()
print(c.class_a())
print(c.class_b())
# we can also use mro method to check method resolution order
print(C.mro())
print(C.__mro__)