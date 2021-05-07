class User:
    def __init__(self, name, email,int_rate,balance):
        self.name=name
        self.email=email
        self.account=BankAccount(int_rate,balance)
class BankAccount:
        def __init__(self,int_rate,balance):
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
ayman=User('ayman','ayman@gmail.com',3,500)
mousa=User('mousa','mousa@gmail.com',8,200)
ayman.account.deposit(200)
ayman.account.deposit(100)
ayman.account.deposit(300)
ayman.account.withdraw(150)
ayman.account.display_account()
mousa.account.deposit(150)
mousa.account.deposit(100)
mousa.account.withdraw(50)
mousa.account.withdraw(40)
mousa.account.withdraw(30)
mousa.account.withdraw(20)
mousa.account.yield_interest()
mousa.account.display_account()

