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


