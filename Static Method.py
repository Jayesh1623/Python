class math:
    def add(self, a, b):
        return (a+b)
    
a= math()
print(a.add(5,5))


class math:
    def __init__(self,a ,b):
        self.a = a
        self.b = b
        
    def add(self):
        print(f"The addition of two no is {self.a + self.b}")
        
    @staticmethod   
    def mul(c,d):
        print(f"The multiplication of two no is {c * d}")
        
    def sub(self):
        print(f"The subtraction of two no is {self.a - self.b}")
    
k = math(5,6)

k.add()
# k.a=2
k.mul(6,5)
k.sub()
print(k.a)

math.mul(5,4)
