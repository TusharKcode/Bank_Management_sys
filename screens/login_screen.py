
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Loginscreen(QWidget):
    def __init__(self, on_login_callback, on_signup_callback):
        super().__init__()
        self.on_login_callback = on_login_callback
        self.on_signup_callback = on_signup_callback

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Login- P.Y. Bank")
        self.setFixedSize(500, 500)

        layout = QVBoxLayout()
        title = QLabel("Login To Your Account")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont('Arial', 18, QFont.Bold))

        # ------------------------------------------------------------------------>>>>>> Username Field

        self.username_input.setPlaceholderText("Username")

        # ------------------------------------------------------------------------>>>>>> Password Field

        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        # ------------------------------------------------------------------------>>>>>> Login Button
        login_button = QPushButton("Login")
        login_button.setFixedHeight(40)
        login_button.clicked.connect(self.login_clicked)

        # ------------------------------------------------------------------------>>>>>> Sign up button
        signup_button = QPushButton("Create an Account")
        signup_button.setFixedHeight(30)
        signup_button.clicked.connect(self.signup_clicked)

        #------------------------------------------------------------------------>>>>>> Add widgets to layout
        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addSpacing(20)
        layout.addWidget(login_button)
        layout.addSpacing(10)
        layout.addWidget(signup_button)

        self.setLayout(layout)

    def login_clicked(self):
        username = self.username_input.text()
        password = self.password_input.text()

        #------------------------------------------------------------------------>>>>>> Here we'll validate using database later
        print(f"Login clicked! Username: {username}, Password: {password}")
        self.on_login_callback(username, password)

    def signup_clicked(self):
        self.on_signup_callback()





