class FourCal():
    def setdata(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b

class test(FourCal):
    def pow(self):
        return self.a**self.b
    def div(self):
        if self.b==0:
            return 0
        else:
            return super().div()
        
a=test()
a.setdata(4,2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.pow())
print(a.div())
