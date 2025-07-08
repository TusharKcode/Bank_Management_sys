import datetime
from user import User

class Manager:
    @staticmethod
    def view_customers():
        if not User.users_db:
            print("No User Found.")
        else:
            print("----------Customer Accounts----------")
            for username, user in User.users_db.items():
                if user.role == "Customer":
                    print(f"Username: {username}, Phone: {user.phone_number}")

    @staticmethod
    def reset_transaction_pin(username):
        if username in User.users_db and User.users_db[username].role == "Customer":
            new_pin = User.generate_pin()
            User.users_db[username].transaction_pin = User.hash_pin(new_pin)
            print(f"Transaction PIN for {username} has been reset to: {new_pin}")
        else:
            print("User not found or not a Customer.")

    @staticmethod
    def generate_daily_report():
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        print(f"Daily Report ({today})")
        transactions_today = [t for t in User.transactions if t["date"] == today]

        if transactions_today:
            for t in transactions_today:
                print(f"{t['time']} | {t['username']} | {t['type']} | Rs.{t['amount']}")
        else:
            print("No transactions found for today.")

    @staticmethod
    def generate_monthly_report():
        current_month = datetime.datetime.now().strftime("%Y-%m")
        print(f"Monthly Report ({current_month})")
        transactions_this_month = [t for t in User.transactions if t["date"].startswith(current_month)]

        if transactions_this_month:
            total_deposits = sum(t["amount"] for t in transactions_this_month if t["type"] == "Deposit")
            total_withdrawals = sum(t["amount"] for t in transactions_this_month if t["type"] == "Withdrawal")

            print(f"Total Deposits: Rs.{total_deposits}")
            print(f"Total Withdrawals: Rs.{total_withdrawals}")
            print(f"Total Transactions: {len(transactions_this_month)}")
        else:
            print("No transactions found for this month.")
