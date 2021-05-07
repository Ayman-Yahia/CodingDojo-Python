
class BankAccount:
    def __init__(self,name,email,int_rate,balance):
        self.name=name
        self.email=email
        self.balance=balance
        self.int_rate=int_rate
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def yield_interest(self):
        self.balance += self.balance * (self.int_rate / 100)
    def display_account(self):
        print("Account balance: $" + str(self.balance) +'  '+ "Interest rate: "+str(self.int_rate))
ayman=BankAccount('ayman','ayman@gmail.com',3,500)
mousa=BankAccount('mousa','mousa@gmail.com',8,200)
ayman.deposit(200)
ayman.deposit(100)
ayman.deposit(300)
ayman.withdraw(150)
ayman.display_account()
mousa.deposit(150)
mousa.deposit(100)
mousa.withdraw(50)
mousa.withdraw(40)
mousa.withdraw(30)
mousa.withdraw(20)
mousa.yield_interest()
mousa.display_account()


