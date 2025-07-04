from logic.account import create_customers, create_account, deposit, withdraw

# Create new customer
cid = create_customers("Tushar", "tush@example.com", "tushpass")

if cid:
    # Create account for this customer
    acc_id = create_account(cid, "Savings")
    acc_id = 1

    # Deposit ₹5000
    deposit(acc_id, 5000)

    # Withdraw ₹2000
    withdraw(acc_id, 2000)

else:
    print("❌ Customer creation failed. Skipping account creation and deposit.")
