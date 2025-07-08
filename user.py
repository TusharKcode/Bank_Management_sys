import random
import hashlib
import datetime
from blacklist import Blacklist

class User:
    users_db = {}
    transactions = []

    def __init__(self, username, phone_number, role="Customer"):
        self.role = role
        self.username = username
        self.phone_number = phone_number
        raw_pin = self.generate_pin()
        raw_transaction_pin = self.generate_pin()
        print(f"Your Login PIN is: {raw_pin}. Please remember it!")
        print(f"Your Transaction PIN is: {raw_transaction_pin}.")
        self.pin = self.hash_pin(raw_pin)
        self.transaction_pin = self.hash_pin(raw_transaction_pin)
        self.bank_accounts = {}
        self.alerts_enabled = True
        self.failed_attempts = 0
        User.users_db[self.username] = self
        print(f"Account Created Successfully as {self.role}!")

    @staticmethod
    def generate_pin():
        return str(random.randint(1000, 9999))

    @staticmethod
    def hash_pin(pin):
        return hashlib.sha256(pin.encode()).hexdigest()

    def verify_transaction_pin(self, entered_pin):
        return self.transaction_pin == self.hash_pin(entered_pin)

    def reset_transaction_pin(self, phone_number):
        if self.phone_number == phone_number:
            new_pin = self.generate_pin()
            self.transaction_pin = self.hash_pin(new_pin)
            print(f"Your new transaction PIN is: {new_pin}. Don't share it with others.")
        else:
            print("Phone number mismatched. Try again.")

    def send_alert(self, message):
        if self.alerts_enabled:
            print(f"Alert for {self.username}: {message}")

    @staticmethod
    def login(username, pin):
        if Blacklist.is_blacklisted(username):
            print(f"Access Denied! User {username} is BLACKLISTED.")
            return None
        user = User.users_db.get(username)
        if user:
            if user.pin == User.hash_pin(pin):
                print(f"Login Successful! Welcome, {username}")
                user.failed_attempts = 0
                return user
            else:
                print("Incorrect PIN.")
                user.failed_attempts += 1
                if user.failed_attempts >= 3:
                    Blacklist.add_to_blacklist(username)
                    print(f"User {username} has been BLACKLISTED due to multiple failed attempts!")
                return None
        else:
            print("User not found!")
            return None

    @staticmethod
    def reset_pin(username, phone_number):
        if username in User.users_db:
            user = User.users_db[username]
            if user.phone_number == phone_number:
                new_pin = user.generate_pin()
                user.pin = user.hash_pin(new_pin)
                print(f"Your new Login PIN is: {new_pin}. Please remember it!")
                return new_pin
        print("Invalid Username or Phone Number.")
        return None

    def add_transaction(self, transaction_type, amount):
        timestamp = datetime.datetime.now()
        transaction = {
            "username": self.username,
            "type": transaction_type,
            "amount": amount,
            "date": timestamp.strftime("%Y-%m-%d"),
            "time": timestamp.strftime("%H:%M:%S")
        }
        User.transactions.append(transaction)

    def perform_transaction(self):
        print("\n-------- Transaction Menu --------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice in ["1", "2"]:
            amount = float(input("Enter amount: "))
            transaction_type = "Deposit" if choice == "1" else "Withdrawal"
            self.add_transaction(transaction_type, amount)
            print(f"{transaction_type} of Rs.{amount} successful!")
