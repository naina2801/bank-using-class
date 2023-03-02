class BankAccount:
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    def deposit(self,dep):
        self.balance += dep
    def withdraw(self,wd):
        self.balance -= wd
    @property
    def bankfees(self):
        self.balance *= 0.1
        # self.balance = str(self.balance * 0.1) 
    @property
    def display(self):
        print("AccountNumber : {} Name : {} Balance: {}".format(self.accountNumber,self.name,self.balance))
b = BankAccount(1006101070685,"Neha",5000)
print("Initial Amount")
b.display
print("After Deposit")
b.deposit(300)
b.display
print("After withdraw")
b.withdraw(100)
b.display
print("After Discount")
b.bankfees
b.display
        