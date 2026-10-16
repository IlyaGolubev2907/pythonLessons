class CreditCard:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def show_info(self):
        print(f"Номер карты: {self.account_number}, Баланс: {self.balance}")


card = CreditCard("1", 100)
card.deposit(50)
card.show_info()
card2 = CreditCard("2", 150)
card2.deposit(200)
card2.show_info()
card3 = CreditCard("3", 50)
card3.withdraw(25)
card3.show_info()
