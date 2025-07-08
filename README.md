# Bank Management System

A cross-platform Python-based desktop application to simulate a basic bank management system.
Built with PyQt5 for modern GUI and SQLite (later steps) for data handling.


---

## Features

**Step 1**: Welcome Screen
- Displays bank logo and welcome message.
- "Get Started" button to enter the app.
- Uses PyQt5 vertical layout with image scaling and fallback text.

**Step 2**: Login Screen
- Username and password input fields.
- "Login" button for existing users.
- "Create an Account" button to navigate to Signup screen (coming next).
- Fields declared properly to avoid warnings.
- Transition handled via QStackedWidget.

---

## Tech Stack

- **Language**: Python 3.x
- **PyQt5** — GUI
- **Database**: MySQL
- **Libraries**: mysql-connector-python

---

## 📂 Project Structure
```
bank_management_system/
│
├── main.py
├── screens/
│   ├── welcome_screen.py
│   ├── login_screen.py
│   ├── signup_screen.py         ← placeholder (next step)
│   └── dashboard_screen.py      ← placeholder (future)
│
├── database/
│   └── db_handler.py            ← placeholder (to implement in next step)
│
├── assets/
│   └── logo.png
│
└── utils/
    └── helpers.py               ← (optional for validations/utilities)
```

## Future Enhancements
- Add a user interface (Tkinter or PyQt)
- Add authentication and login system
- Show transaction history and account statements
- Admin panel for managing all users

## Contributing
Pull requests and suggestions are welcome! Feel free to fork this repo and improve it.

# License
This project is open-source. Feel free to use and modify.

# Contact
Tushar Kumar — [https://www.linkedin.com/in/tushar-kumar-developer/] — [tkgoyal104@gmail.com]
