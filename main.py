from user import User
from bank_account import BankAccount

logged_in_user = None

while True:
    print("\n------------PY BANK------------")
    print("1. Register/Login")
    print("2. Reset PIN")
    print("3. Create Account")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Display Account Details")
    print("7. Reset Transaction PIN")
    print("8. Calculate Interest")
    print("9. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        username = input("Enter Username: ")
        if username in User.users_db:
            pin = input("Enter Login PIN: ")
            if not pin.isdigit() or len(pin) != 4:
                print("Invalid PIN! PIN must be a 4-digit number.")
                continue
            logged_in_user = User.login(username, pin)
            if logged_in_user and logged_in_user.role == "Customer":
                if not logged_in_user.bank_accounts:
                    print("You must create a bank account before transactions.")
                else:
                    while True:
                        print("\n1. Perform Transaction")
                        print("2. Logout")
                        action = input("Enter your choice: ")
                        if action == "1":
                            logged_in_user.perform_transaction()
                        elif action == "2":
                            break
                        else:
                            print("Invalid choice.")
        else:
            phone_number = input("Enter Phone Number: ")
            role = input("Enter Role (Admin, Manager, Customer): ").capitalize()
            if role not in ["Admin", "Manager", "Customer"]:
                print("Invalid Role! Defaulting to Customer.")
                role = "Customer"
            if username in User.users_db:
                print("Username already exists. Please login instead.")
                continue
            new_user = User(username, phone_number, role)
            logged_in_user = new_user

    elif choice == "2":
        username = input("Enter Username: ")
        phone_number = input("Enter Registered Phone Number: ")
        User.reset_pin(username, phone_number)

    elif choice == "3":
        if not logged_in_user:
            print("Please login first to create an account.")
            continue
        name = input("Enter Full Name: ")
        phone_number = logged_in_user.phone_number
        account_type = input("Enter Account Type (Savings/Business/etc.): ")
        while True:
            try:
                balance = float(input("Enter Initial Balance: "))
                if balance < 0:
                    raise ValueError("Balance cannot be negative.")
                break
            except ValueError as e:
                print(e)
        new_account = BankAccount(name, balance, phone_number, account_type)
        logged_in_user.bank_accounts[new_account.account_no] = new_account

    elif choice == "4":
        if not logged_in_user or not logged_in_user.bank_accounts:
            print("Please login and create an account first.")
            continue
        selected_acc_no = input("Enter account number: ")
        if selected_acc_no not in logged_in_user.bank_accounts:
            print("Invalid account number.")
            continue
        account = logged_in_user.bank_accounts[selected_acc_no]
        amount = float(input("Enter Deposit amount: "))
        account.deposit(amount, logged_in_user)

    elif choice == "5":
        if not logged_in_user or not logged_in_user.bank_accounts:
            print("Please login and create an account first.")
            continue
        selected_acc_no = input("Enter account number: ")
        if selected_acc_no not in logged_in_user.bank_accounts:
            print("Invalid account number.")
            continue
        account = logged_in_user.bank_accounts[selected_acc_no]
        amount = float(input("Enter Withdrawal amount: "))
        account.withdraw(amount, logged_in_user)

    elif choice == "6":
        if not logged_in_user or not logged_in_user.bank_accounts:
            print("Please login and create an account first.")
            continue
        selected_acc_no = input("Enter account number: ")
        if selected_acc_no not in logged_in_user.bank_accounts:
            print("Invalid account number.")
            continue
        account = logged_in_user.bank_accounts[selected_acc_no]
        account.display_acc_dtls()

    elif choice == "7":
        if logged_in_user:
            phone_number = input("Enter Registered Mobile Number: ")
            logged_in_user.reset_transaction_pin(phone_number)
        else:
            print("Please login first.")

    elif choice == "8":
        if not logged_in_user or not logged_in_user.bank_accounts:
            print("Please login and create an account first.")
            continue
        selected_acc_no = input("Enter account number: ")
        if selected_acc_no not in logged_in_user.bank_accounts:
            print("Invalid account number.")
            continue
        account = logged_in_user.bank_accounts[selected_acc_no]
        account.calculate_interest()

    elif choice == "9":
        print("Exiting... Thank you for using PY BANK.")
        break

    else:
        print("Invalid choice. Please try again.")
