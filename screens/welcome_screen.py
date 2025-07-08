from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont

class Welcome_screen(QWidget):
    def __init__(self, on_start_callback):
        super().__init__()
        self.on_start_callback = on_start_callback
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Welcome To P.Y. Bank")
        self.setFixedSize(500, 500)

        layout = QVBoxLayout()

        logo_label = QLabel(self)
        pixmap = QPixmap("assets/logo.jpg")
        if not pixmap.isNull():
            pixmap = pixmap.scaled(150,150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            logo_label.setPixmap(pixmap)
        else:
            logo_label.setText("Bank logo")
            logo_label.setFont(QFont("Arial", 14))
        logo_label.setAlignment(Qt.AlignCenter)

        title_label = QLabel("Welcome to P.Y. Bank")
        title_label.setFont(QFont("Arial", 20, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)

        start_button = QPushButton("Get Started")
        start_button.setFixedHeight(40)
        start_button.setFont(QFont("Arial", 14, QFont.Bold))
        start_button.clicked.connect(self.start_clicked)

        layout.addWidget(logo_label)
        layout.addWidget(title_label)
        layout.addStretch()
        layout.addWidget(start_button)

        self.setLayout(layout)

    def start_clicked(self):
        self.on_start_callback()















