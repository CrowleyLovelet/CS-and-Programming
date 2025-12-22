class BankAcc:
    def __init__(self, name, accnumber, balance=0):
        self.name = name
        self._balance = balance
        self.__accnumber = accnumber
    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} is added to the balance")
        else:
            print(f"{amount} amount cannot be deposited.")
    def withdraw(self,amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            print(f"{amount} is subtracted from the balance")
        else:
            print(f"{amount} amount cannot be withdrawn.")
    def get_balance(self):
        return self._balance
    def display_info(self):
        masked_accnumber = "#######"
        print(f"Account name: {self.name}")
        print(f"Account number: {masked_accnumber}")
        print(f"Account balance: {self._balance}")
class SavingAccount(BankAcc):
    def __init__(self, name, accnumber, interest_rate, balance=0):
        super().__init__( name, accnumber, balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        interest =self._balance * self.interest_rate / 100
        self._balance += interest
        print(f"Added interest of{interest} to the balance: {self._balance}")
account = BankAcc("Bibizyanka", 121315,100)
account.deposit(50)
account.withdraw(20)
print("Current Balance:",account.get_balance())
account.display_info()
savingacc = SavingAccount(super(BankAcc), super(BankAcc), 10, 100)
savingacc.apply_interest()
