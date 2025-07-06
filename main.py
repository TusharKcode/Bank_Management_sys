
from logic.account import create_customers, create_account, deposit, withdraw, InvalidPinError, InvalidAccountError, login
from logic.utils import get_connection

class InsufficientBalanceError:
    pass

#--------------------------------------------------------------------------------->>>>>Balance & Transaction
def view_balance(account_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (account_id,))
    result = cursor.fetchone()
    if result:
        print(f"Current Balance: Rs.{result[0]:.2f}")
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
            print(f"Type: {row[0]}, Amount: Rs.{row[1]:.2f}, Date: {row[2]}")
    else:
        print(f"No Transaction Found")
    cursor.close()
    conn.close()

#------------------------------------------------------------------------------------->>>>>>>>>> Main Menu
def main_menu():

    print("Welcome to P.Y. Bank Management System")
    print("Please Login in First!")

    username = input("Enter your Username: ")
    pin = input("Enter your Pin (4-6 digits): ")

    try:
        customer_id = login(username, pin)
    except InvalidPinError as e:
        print(e)
        return

    while True:
        print("Logged In as: ", username)
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Account Balance")
        print("5. View Transactions")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_type = input("Enter your account type (eg. Saving): ")
            create_account(customer_id, account_type)

        elif choice == "2":
            account_id = input("Enter your account id: ")
            amount = float(input("Enter your amount to deposit: "))
            deposit(account_id, amount)

        elif choice == "3":
            account_id = input("Enter your account id: ")
            amount = float(input("Enter your amount to withdraw: "))
            withdraw(account_id, amount)

            try:
                withdraw(account_id, amount)
            except InvalidAccountError as e:
                print(e)
            except InsufficientBalanceError as e:
                print(e)

        elif choice == "4":
            account_id = input("Enter your account id: ")
            view_balance(account_id)

        elif choice == "5":
            account_id = input("Enter your account id: ")
            view_transactions(account_id)

        elif choice == "6":
            print("Thanks for using this Bank Management System. Goodbye!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    print("Welcome, You must create a customer account, if you don't have one.")
    while True:
        choice = input("Do you want to create a new customer account? (y/n): ").lower()
        if choice == "y":
            name = input("Enter your name: ")
            phone_number = input("Enter your phone number: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            login_username = input("Choose a Login Username: ")

            create_customers(name, phone_number, email, password, login_username)

        elif choice == "n":
            break
        else:
            print("Please Type 'y' or 'n'.")
    main_menu()


