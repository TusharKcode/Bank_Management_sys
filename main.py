from tkinter.font import names

from logic.account import create_customers, create_account, deposit, withdraw
from logic.utils import get_connection

def view_balance(account_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (account_id,))
    result = cursor.fetchone()
    if result:
        print(f"Current Balance: ₹{result[0]:.2f}")
    else:
        print(f"No account with account_id {account_id}")
    cursor.close()
    conn.close()

def view_transactions(account_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT transaction_type, amount, transaction_date FROM transactions WHERE account_id = %s ORDER BY transaction_date DESC", (account_id,))
    results = cursor.fetchall()
    if results:
        print(f"Transaction History: ")
        for row in results:
            print(f"Type: {row[0]}, Amount: ₹{row[1]:.2f}, Date: {row[2]}")
    else:
        print(f"No Transaction Found")
    cursor.close()
    conn.close()

def main_menu():
    while True:
        print("1. Create Customer")
        print("2. Create Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. View Account Balance")
        print("6. View Transactions")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            create_customers(name, email, password)

        elif choice == "2":
            customer_id = input("Enter your customer id: ")
            account_type = input("Enter your account type: ")
            create_account(customer_id, account_type)

        elif choice == "3":
            account_id = input("Enter your account id: ")
            amount = float(input("Enter your amount to deposit: "))
            deposit(account_id, amount)

        elif choice == "4":
            account_id = input("Enter your account id: ")
            amount = float(input("Enter your amount to withdraw: "))
            withdraw(account_id, amount)

        elif choice == "5":
            account_id = input("Enter your account id: ")
            view_balance(account_id)

        elif choice == "6":
            account_id = input("Enter your account id: ")
            view_transactions(account_id)

        elif choice == "7":
            print("Thanks for using this Bank Management System. Goodbye!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main_menu()


