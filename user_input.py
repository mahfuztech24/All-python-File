def add_num(*args):
    print(args)
nums=list(map(int,input("Enter Number Seperated By Space").split()))
add_num(*nums) 