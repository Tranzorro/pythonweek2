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

# add users class that inherits from bank account class

class user(BankAccount): #setting parent class inside here allows use of super (inheritance)
    def __init__(self,):
        super().__init__(0.02, 0) #this gives access to EVERYTHING in bank account class
        self.account = BankAccount(0.02,0) #this gives access to bank account funcs without super
    def make_deposit(self, amount): #not needed with super
        self.account.deposit(amount)
        print("deposited",amount,"balance is now",self.account.myBalance)
        return self
    def make_withdrawal(self, amount): #not needed with super
        self.account.withdraw(amount)
        print("withdrew",amount,"balance is now",self.account.myBalance)
        return self
    def display_user_balance(self): #not needed with super
        print(self.account.myBalance)
        return self

someuser = user()
otheruser = user()
# someuser.deposit(100) #super version
# print(someuser.deposit(50).display_account_info()) #super version
someuser.make_deposit(50).display_user_balance()
# print(someuser.display_user_balance())