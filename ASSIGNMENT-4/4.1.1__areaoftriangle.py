class s():
    def __init__(self):
        self.a=int(input("side1 : "))
        self.b=int(input("side2 : "))
        self.c=int(input("side3 : "))
        self.s=(self.a+self.b+self.c)/2
       
class area(s):
    def __init__(self,*args):
        super(area,self).__init__(*args)
    
    def triarea(self):
        if self.a+self.b>self.c and self.c+self.b>self.a and self.a+self.c>self.b:
            area=(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c)) ** 0.5
            return area
        
        else:
            return "these three sides can form a triangle"


tri=area()
print(tri.triarea())
