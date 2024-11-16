class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def showNum(self):
        print(f"{self.real}i+{self.img}j")    
    def __sub__(num1, num2):
        newReal = num1.real-num2.real
        newImg = num1.img-num2.img
        return Complex(newReal,newImg)
num1 = Complex(1,4)
num1.showNum()
num2 = Complex(23,43)
num2.showNum()


num3 = num1-num2
num3.showNum()
