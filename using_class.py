class Student:
    def say_hello(self):
        print("Hello")

    def calculation(self,a,b):
        print("sum of two numbers")
        sum=a+b
        return(sum)

p1=Student()
p1.say_hello()

result=p1.calculation(10,20)
print(result)
