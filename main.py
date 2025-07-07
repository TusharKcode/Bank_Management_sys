from logic.account import create_customers, create_account, deposit, withdraw, InvalidPinError, \
    login
from logic.utils import get_connection

#--------------------------------------------------------------------------------->>>>>Helper Function
def get_acc_id_by_number(account_number):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT account_id FROM accounts WHERE account_number = %s", (account_number,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result:
        return result[0]
    else:
        return None

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

        menu_choice = input("Enter your choice: ")
        if menu_choice == "1":
            account_type = input("Enter your account type (eg. Saving): ")
            create_account(customer_id, account_type)

        elif menu_choice == "2":
            account_number = input("Enter your account number: ")
            account_id = get_acc_id_by_number(account_number)
            if not account_id:
                print("Invalid Account Number. Please check and try again.")
                continue
            amount = float(input("Enter your amount to deposit: "))
            deposit(account_id, amount)

        elif menu_choice == "3":
            account_number = input("Enter your account number: ")
            account_id = get_acc_id_by_number(account_number)
            if not account_id:
                print("Invalid Account Number. Please check and try again.")
                continue
            amount = float(input("Enter your amount to withdraw: "))
            withdraw(account_id, amount)

        elif menu_choice == "4":
            account_number = input("Enter your account number: ")
            account_id = get_acc_id_by_number(account_number)
            if not account_id:
                print("Invalid Account Number. Please check and try again.")
                continue
            view_balance(account_id)

        elif menu_choice == "5":
            account_number = input("Enter your account number: ")
            account_id = get_acc_id_by_number(account_number)
            if not account_id:
                print("Invalid Account Number. Please check and try again.")
                continue
            view_transactions(account_id)

        elif menu_choice == "6":
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

            create_customers(name, email, password, login_username)

        elif choice == "n":
            break
        else:
            print("Please Type 'y' or 'n'.")
    main_menu()


