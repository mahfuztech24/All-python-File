def add_num(*args):
     print(args)
     sum=0
     for n in args:
            sum=sum+n
     return(sum)
nums=list(map(int,input("Enter Number by Seperated by Space").split()))
print(add_num(*nums))