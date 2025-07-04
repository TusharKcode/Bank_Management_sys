from logic.utils import get_connection

def create_customers(name, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers WHERE email = %s", (email,))
    if cursor.fetchone():
        print("⚠️ Customer with this email already exists.")
        cursor.close()
        conn.close()
        return None

    sql = "INSERT INTO customers (name, email, password) VALUES (%s, %s, %s)"
    val = (name, email, password)
    cursor.execute(sql, val)
    conn.commit()

    customer_id = cursor.lastrowid  # Get new ID
    print("Customer created successfully, ID:", customer_id)
    cursor.close()
    conn.close()
    return customer_id


def create_account(customer_id, account_type):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO accounts (customer_id, balance, account_type) VALUES (%s, %s, %s)"
    val = (customer_id, 0.00, account_type)
    cursor.execute(sql, val)
    conn.commit()
    account_id = cursor.lastrowid  # ✅ Get new account ID
    print("Account created successfully, ID:", account_id)
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

    #Check current balance
    cursor.execute("SELECT balance FROM accounts WHERE account_id = %s ", (account_id,))
    result = cursor.fetchone()
    if result is None:
        print("Account does not exist")
        cursor.close()
        conn.close()
        return

    current_balance = result[0]
    if amount > current_balance:
        print("Insufficient balance")
        cursor.close()
        conn.close()
        return

    #Update balance
    sql_update = "UPDATE accounts SET balance = balance - %s WHERE account_id = %s"
    cursor.execute(sql_update, (amount, account_id))

    #Insert transaction record
    sql_insert = "INSERT INTO transactions (account_id, transaction_type, amount) VALUES (%s, %s, %s)"
    cursor.execute(sql_insert, (account_id, "Withdraw", amount))

    conn.commit()
    print("Withdraw successful.")
    cursor.close()
    conn.close()

