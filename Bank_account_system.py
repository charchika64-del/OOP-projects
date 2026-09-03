class BankAccount:
    def __init__(self,account_no,holder_name,balance):
        self.account_number=account_no
        self.name=holder_name
        self.balance=balance
        self.recent=""
    def deposit(self,money):
          self.balance+=money
          self.recent=f"Recently,deposited ₹{money}"
    def withdraw(self,money):
          self.balance-=money
          self.recent= f"Recently,withdrawed ₹{money}"
    def __str__(self):
       return (f"Name of account holder: {self.name}\n"
            f"Account number: {self.account_number}\n"
            f"Balance: ₹{self.balance}\n"
            f"{self.recent}")
class SavingsAccount(BankAccount):
    def __init__(self, account_no, holder_name, balance, interest_rate):
        super().__init__(account_no, holder_name, balance)
        self.interest_rate=interest_rate
        
    def add_interest(self):
        amount=self.balance*self.interest_rate/100
        amount=round(amount,2)
        self.balance+=amount
        self.recent= f"Recently,got ₹{amount} by savings account"
    def __str__(self):
        return super().__str__() + f"\nInterest rate: {self.interest_rate}%"
    
p2=SavingsAccount(1234,"John",9000,5)
p2.deposit(300)
p2.add_interest()
print(p2)


