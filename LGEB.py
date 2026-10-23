
#LEGB example
x="global"
def outer():
    x="enclosing"
    def inner():
        x="local"
        print(x)
    inner()
    print(x)





outer()
# *arguments

def add_numbers(*args):
    print(args)
    print(end=" ")
#num_list=[1,2,3,4,5],[9,2,5,8]
num_list=list(input("Please Enter 5 Numbers"))
add_numbers(num_list)
