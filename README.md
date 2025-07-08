# 🏦 PY BANK — Bank Management System

A Python-based console application for managing a simple bank system with modular design.  
Built with Python (no external database yet), fully modular, and easy to extend.

---

## ✨ Features

- Register new users (Admin, Manager, Customer)
- User login and PIN-based authentication
- Create multiple bank accounts per user
- Deposit and withdraw funds
- View account details and transaction history
- Reset login and transaction PINs
- Interest calculation for savings accounts
- Basic admin and manager modules (structure ready)

---

## 🗂️ Project Structure

```
bank_sys/
│
├── main.py                 # <<<----- Entry point & menu-driven logic
├── user.py                 # <<<----- User class and related methods
├── bank_account.py         # <<<----- BankAccount and FixedDeposit classes
├── admin.py                # <<<----- Admin-related functionalities
├── manager.py              # <<<----- Manager functionalities
├── blacklist.py            # <<<----- Blacklist handling
├── utils.py                # <<<----- Custom exceptions
└── README.md               # <<<----- Project documentation

```
---

## ⚙️ Requirements

- Python 3.8 or higher
- No external libraries (for now)

---

## 🚀 How to Run

1. Clone this repository or copy files into a folder.
2. Open terminal (or VS Code terminal) and navigate to project folder.
3. Run:

```
python main.py
```

- Follow on-screen menu instructions to register, create accounts, and perform transactions.

---

## 💡 Future Enhancements
- MySQL database integration for storing users and transactions permanently
- GUI using Tkinter or PyQt
- Customer support chatbot module
- PDF/CSV statement download options

---

## 📄 License
This project is for educational purposes and free to use.

## 🙌 Author
**Tushar Kumar** | LinkedIn - [https://www.linkedin.com/in/tushar-kumar-developer/]
