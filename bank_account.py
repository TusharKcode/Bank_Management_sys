import time
import random
from utils import InsufficientBalanceError

class BankAccount:
    accounts_db = {}
    Interest_rt = 7.2

    def __init__(self, name, balance, phone_number, account_type):
        self.name = name
        self.phone_number = phone_number
        self.account_no = self.generate_account_no()
        self.account_type = account_type
        self.balance = balance
        self.last_interest_time = time.time()
        self.fixed_dpts = []
        self.transactions = []

        BankAccount.accounts_db[self.account_no] = self
        print(f"{account_type} Account Created Successfully! Your Account Number is: {self.account_no}")

    @staticmethod
    def generate_account_no():
        while True:
            account_no = str(random.randint(1000000000, 9999999999))
            if account_no not in BankAccount.accounts_db:
                return account_no

    def get_balance(self):
        return self.balance

    def deposit(self, amount, user):
        if amount > 0:
            self.balance += amount
            user.send_alert(f"Deposit of Rs.{amount} successful. New Balance: Rs.{self.balance}")
            transaction = f"Deposit: Rs.{amount:.2f}, New Balance: Rs.{self.balance:.2f}"
            self.transactions.append(transaction)
            print(transaction)
            return True
        else:
            print("Deposited amount must be greater than zero.")
            return False

    def withdraw(self, amount, user):
        try:
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient balance! Withdrawal amount exceeds available balance.")
            elif amount <= 0:
                raise ValueError("Withdrawal amount must be greater than 0")

            if amount > 4000:
                entered_pin = input("Enter Transaction PIN: ")
                if not user.verify_transaction_pin(entered_pin):
                    print("Invalid Transaction PIN. Withdrawal denied.")
                    return

            self.balance -= amount
            transaction = f"Withdraw: Rs.{amount:.2f}, New Balance: Rs.{self.balance:.2f}"
            self.transactions.append(transaction)
            print(transaction)
            user.send_alert(f"Withdraw of Rs.{amount:.2f} successful. New Balance: Rs.{self.balance:.2f}")
            if self.balance < 1000:
                user.send_alert("Low Balance Alert! Your Balance is below Rs.1000.")
        except (InsufficientBalanceError, ValueError) as e:
            print(e)

    def disp_transaction_history(self):
        print("------Transaction History------")
        if len(self.transactions) == 0:
            print("No Transaction Found.")
        else:
            for transaction in self.transactions:
                print(transaction)

    def calculate_interest(self):
        if self.account_type == "Savings":
            current_time = time.time()
            elapsed_time = (current_time - self.last_interest_time) / (60 * 60 * 24 * 365)
            if elapsed_time > 0:
                interest_earned = self.balance * BankAccount.Interest_rt * elapsed_time
                self.balance += interest_earned
                self.last_interest_time = current_time
                print(f"Interest of {interest_earned:.2f} added! New Balance: Rs.{self.balance:.2f}")
            else:
                print("No interest earned yet.")
        else:
            print("Interest is only applicable to Savings accounts.")

    def display_acc_dtls(self):
        print("------------Your Account Details------------")
        print(f"Name:           {self.name}")
        print(f"Contact No.:    {self.phone_number}")
        print(f"Account Number: {self.account_no}")
        print(f"Balance:        Rs.{self.balance:.2f}")

class FixedDeposit:
    def __init__(self, account_no, amount, tenure, interest_rate):
        self.account_no = account_no
        self.amount = amount
        self.tenure = tenure
        self.interest_rate = interest_rate
        self.start_time = time.time()
        self.maturity_time = self.start_time + (tenure * 365 * 24 * 60 * 60)

    def check_maturity(self):
        current_time = time.time()
        if current_time >= self.maturity_time:
            interest = self.amount * (self.interest_rate / 100) * self.tenure
            total_amt = self.amount + interest
            return True, total_amt
        else:
            return False, None
