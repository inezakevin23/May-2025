class bankaccount:
    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def display(self):
        print(f'{self.name} has {self.balance}')

account= bankaccount('kevin', 30)
account.deposit(30)
account.display()
