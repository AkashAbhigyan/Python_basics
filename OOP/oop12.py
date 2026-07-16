class BankAccount:
    MIN_BALANCE = 100
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit_money(self, deposit_amount):
        if deposit_amount > 0:
            self.__balance += deposit_amount
            print(f"Rs.{deposit_amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw_money(self, withdraw_amount):
        if withdraw_amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif withdraw_amount > self.__balance:
            print("Insufficient balance.\n")
        else:
            self.__balance -= withdraw_amount
            print(f"Rs.{withdraw_amount} withdrawn successfully.")

    def display_balance(self):
        print(f"Current Balance: Rs.{self.__balance}")

    @staticmethod
    def valid_intrest_rate(rate):
        return 0<= rate <= 5
            

account = BankAccount("Akash",2000)
print(BankAccount.valid_intrest_rate(3))