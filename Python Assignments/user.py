class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.balance=0
    def withdrawl(self, amount):
        self.balance-=amount
    def deposit(self, amount):
        self.balance+=amount
    def display_account(self):
        print(self.name+' '+" balance currently is " +' '+str(self.balance))


mousa=User('mousa','mousa@gmail.com')
ayman=User('ayman','ayman@gmail.com')
ahmad=User('ahmad','ahmad@hotmail.com')
mousa.deposit(200)
mousa.deposit(100)
mousa.deposit(150)
mousa.withdrawl(100)
mousa.display_account()
ayman.deposit(200)
ayman.deposit(150)
ayman.withdrawl(50)
ayman.withdrawl(45)
ayman.display_account()
ahmad.deposit(100)
ahmad.withdrawl(20)
ahmad.withdrawl(10)
ahmad.withdrawl(15)
ahmad.display_account()