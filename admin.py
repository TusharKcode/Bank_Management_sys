import hashlib
from user import User
from blacklist import Blacklist

class Admin:
    admin_username = "admin"
    admin_password = hashlib.sha256("admin123".encode()).hexdigest()

    @staticmethod
    def login(username, password):
        if username == Admin.admin_username and hashlib.sha256(password.encode()).hexdigest() == Admin.admin_password:
            print("Admin Login Successful.")
            return True
        else:
            print("Invalid Admin Credentials!")
            return False

    @staticmethod
    def view_all_users():
        if not User.users_db:
            print("No User Found.")
        else:
            print("--------User Accounts--------")
            for username, user in User.users_db.items():
                print(f"Username: {username}, Role: {user.role}, Phone: {user.phone_number}, Accounts: {len(user.bank_accounts)}")

    @staticmethod
    def reset_user_pin(username):
        if username in User.users_db:
            new_pin = User.generate_pin()
            User.users_db[username].pin = User.hash_pin(new_pin)
            print(f"User {username}'s PIN has been reset. New PIN: {new_pin}")
        else:
            print("User not found.")

    @staticmethod
    def delete_user(username):
        if username in User.users_db:
            del User.users_db[username]
            print(f"User {username} has been deleted.")
        else:
            print("User not found.")

    @staticmethod
    def logout():
        print("Logging Out from Admin Dashboard...")

    @staticmethod
    def manage_blacklist():
        while True:
            print("\n--- Blacklist Management ---")
            print("1. View Blacklisted Users")
            print("2. Remove User from Blacklist")
            print("3. Exit")

            choice = input("Enter your choice: ").strip()
            if choice == "1":
                Blacklist.view_blacklisted_users()
            elif choice == "2":
                username = input("Enter Username to Remove: ")
                Blacklist.remove_from_blacklist(username)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Try again.")
