class ATM:

    def __init__(self, banknote_20, banknote_50, banknote_100):
        self.banknote_20 = banknote_20
        self.banknote_50 = banknote_50
        self.banknote_100 = banknote_100

    def add_money(self, add_20, add_50, add_100):
        self.banknote_20 = self.banknote_20 + add_20
        self.banknote_50 = self.banknote_50 + add_50
        self.banknote_100 = self.banknote_100 + add_100

    def withdraw(self, amount):
        find_20 = 0
        find_50 = 0
        find_100 = 0

        found = False

        for n100 in range(0, self.banknote_100 + 1):
            for n50 in range(0, self.banknote_50 + 1):
                for n20 in range(0, self.banknote_20 + 1):
                    if n100 * 100 + n50 * 50 + n20 * 20 == amount:
                        find_100 = n100
                        find_50 = n50
                        find_20 = n20
                        found = True
                        break
                if found:
                    break
            if found:
                break
        if not found:
            return False

        self.banknote_100 -= find_100
        self.banknote_50 -= find_50
        self.banknote_20 -= find_20

        print(f"Выдано: 100 — {find_100}, 50 — {find_50}, 20 — {find_20}")
        return True


atm = ATM(0, 0, 0)
atm.add_money(5, 5, 5)
atm.withdraw(280)
print(atm.banknote_100, atm.banknote_50, atm.banknote_20)
atm.withdraw(200)
print(atm.banknote_100, atm.banknote_50, atm.banknote_20)
