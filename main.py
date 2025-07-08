import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget

from screens.login_screen import Loginscreen
from screens.welcome_screen import Welcomescreen


def main():
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()

    def go_to_login():
        stacked_widget.setCurrentIndex(1)

    def handle_login(username, password):
        print(f"Trying to login...{username} - {password}")

    def go_to_signup():
        print("Signup button clicked")

    welcome_screen = Welcomescreen(on_start_callback=go_to_login)
    login_screen = Loginscreen(on_login_callback=handle_login, on_signup_callback=go_to_signup)
    stacked_widget.addWidget(welcome_screen)
    stacked_widget.addWidget(login_screen)
    stacked_widget.setFixedSize(500,500)
    stacked_widget.show()

    sys.exit(app.exec_())
if __name__ == "__main__":
    main()