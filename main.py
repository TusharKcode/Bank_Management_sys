import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from screens.welcome_screen import Welcome_screen

def main():
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()

    def go_to_login():
        print("Get started Clicked: next is login screen")

    welcome_screen = Welcome_screen(on_start_callback=go_to_login)
    stacked_widget.addWidget(welcome_screen)
    stacked_widget.setFixedSize(500,500)
    stacked_widget.show()

    sys.exit(app.exec_())
if __name__ == "__main__":
    main()