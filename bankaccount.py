# make a bank account that can do things with some funcs.


# the bank account class object
class BankAccount:
    def __init__(self, int_rate, balance):
        # attributes go here
        self.myBalance = balance
        self.myInt_rate = int_rate
    def deposit(self, amount):
        # increase the account balance by the given amount
        self.myBalance += amount
        return self
    def withdraw(self, amount):
        # decrease the account balance by the given amount if there is enough to take, else if not enough, print charging 5 bucks.
        if self.myBalance >=amount:
            self.myBalance -= amount
        else:
            print("Not enough funds in your account, sorry bro you are getting charged $5... which makes no sense that was are taking what you don't have, but we are greedy mofos!")
        return self
    def display_account_info(self):
        # print to console the balance. example: "balances: $100"
        print("Balances:",self.myBalance)
        return self
    def yield_interest(self):
        # increase the account balance by the current balance * the interest rate (as long as the account is positive.)
        if self.myBalance >= 1:
            self.myBalance += self.myBalance * self.myInt_rate
        else:
            print("Sorry, no interest for you! Not enough funds to accrue!")
        return self


account1 = BankAccount(1.3,50)
account2 = BankAccount(2.5,100)

account1.deposit(50).deposit(100).deposit(10).withdraw(80).yield_interest().display_account_info()
account2.deposit(100).deposit(50).withdraw(10).withdraw(15).withdraw(20).withdraw(10).yield_interest().display_account_info()