class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
            return self.a + self.b
    def sub(self):
           return self.a - self.b
            
    def mul(self):
            return self.a * self.b              
            
    def div(self):
            return self.a / self.b       
ob1=Calculator(50,20) 
print("summation=",ob1.sum())  
print("Subtraction=",ob1.sub())  
print("Multiplication=",ob1.mul())  
print("devide=",ob1.div())  