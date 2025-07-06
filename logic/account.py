import random
from logic.utils import get_connection

class InvalidAccountError(Exception):
    pass
class InSufficientBalanceError(Exception):
    pass
class InvalidPinError(Exception):
    pass

#--------------------------------------------------------------------------------------->>>>>Account Part
def generate_acc_no():
    return str(random.randint(10**12, 10**13 - 1))              #<<<<<<-------------------Unique Acc. No.

def generate_pin():
    return str(random.randint(1000, 999999))              #<<<<<<----------Auto generate Login PIN

#--------------------------------------------------------------------------------------->>>>>User Login Part
def login(username, pin):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT customer_id FROM customers WHERE login_username = %s AND pin = %s", (username, pin))
    result =  cursor.fetchone()

    if result is None:
        cursor.close()
        conn.close()
        raise InvalidPinError("Invalid Username or Pin")

    customer_id = result[0]
    cursor.close()
    conn.close()
    print("Login successful.")
    return customer_id

#--------------------------------------------------------------------------------------->>>>>Customer Part
def create_customers(name, email, password, login_username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers WHERE email = %s", (email,))
    if cursor.fetchone():
        print("Customer with this email already exists.")
        cursor.close()
        conn.close()
        return None

    pin = generate_pin()

    sql = "INSERT INTO customers (name, email, password, login_username, pin) VALUES (%s, %s, %s, %s, %s)"
    val = (name, email, password, login_username, pin)
    cursor.execute(sql, val)
    conn.commit()

    customer_id = cursor.lastrowid  # Get new ID
    print("Customer created successfully, ID:", customer_id)
    print(f"Your Login PIN: {pin}. Don't share to anyone and keep it safe." )
    cursor.close()
    conn.close()
    return customer_id

#------------------------------------------------------------------------------------>>>>>Create Account Part
def create_account(customer_id, account_type):
    conn = get_connection()
    cursor = conn.cursor()

    account_number = generate_acc_no()
    sql = "INSERT INTO accounts (customer_id, balance, account_type, account_number) VALUES (%s, %s, %s, %s)"
    val = (customer_id, 0.00, account_type, account_number)
    cursor.execute(sql, val)
    conn.commit()
    account_id = cursor.lastrowid  # ✅ Get new account ID
    print(f"Account created successfully! Your Account Number is: {account_number}")
    cursor.close()
    conn.close()
    return account_id

def deposit(account_id, amount):
    conn = get_connection()
    cursor = conn.cursor()

    #Update balance
    sql_update = "UPDATE accounts SET balance = balance +  %s WHERE account_id = %s"
    cursor.execute(sql_update, (amount, account_id))

    #Insert transaction record
    sql_insert = "INSERT INTO transactions (account_id, transaction_type, amount) VALUES (%s, %s, %s)"
    cursor.execute(sql_insert, (account_id, "Deposit", amount))
    conn.commit()
    print("Deposit successful.")
    cursor.close()
    conn.close()

def withdraw(account_id, amount):
    conn = get_connection()
    cursor = conn.cursor()

    #--------------------------------------------------------------------------->>>>>>>Check current balance
    cursor.execute("SELECT balance FROM accounts WHERE account_id = %s ", (account_id,))
    result = cursor.fetchone()
    if not result:
        raise InvalidAccountError("Invalid Account number. Account does not exist")

    current_balance = result[0]
    if amount > current_balance:
        raise InSufficientBalanceError("Insufficient balance")

    #---------------------------------------------------------------------------------->>>>>>>Update balance
    sql_update = "UPDATE accounts SET balance = balance - %s WHERE account_id = %s"
    cursor.execute(sql_update, (amount, account_id))

    #----------------------------------------------------------------------->>>>>>>Insert transaction record
    sql_insert = "INSERT INTO transactions (account_id, transaction_type, amount) VALUES (%s, %s, %s)"
    cursor.execute(sql_insert, (account_id, "Withdraw", amount))

    conn.commit()
    print("Withdraw successful.")
    cursor.close()
    conn.close()

