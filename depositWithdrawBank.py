class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        return(amount)
    def withdraw(self,withdraw):
        self.balance=self.balance-withdraw
        return(withdraw)

ob1=BankAccount("Mahfuz",2000)
print("Name of the Account Holder:",ob1.name)
print("deposit=",ob1.deposit(1200))
print("Withdraw=",ob1.withdraw(500))
print("Balance=",ob1.balance)
          