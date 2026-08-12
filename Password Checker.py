import sys
import re
from PyQt6.QtWidgets import (
    QLabel, QWidget, QVBoxLayout, QLineEdit, QApplication, QCheckBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

class PasswordChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Check Your Password")
        self.setWindowIcon(QIcon("resources/check.png"))
        self.setFixedSize(400,400)
        self._build_ui()

    def _build_ui(self):
        Vlayout = QVBoxLayout()
        Vlayout.setContentsMargins(20, 20, 20, 20)
        Vlayout.setSpacing(6)

        title = QLabel("Enter Your Password")
        title.setStyleSheet("color: white; font-size: 16pt; font-weight: bold;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        Vlayout.addWidget(title)
        Vlayout.addSpacing(30)

        self.user_password = QLineEdit()
        self.user_password.setPlaceholderText("Password")
        self.user_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.user_password.textChanged.connect(self._on_text_changed)
        Vlayout.addWidget(self.user_password)

        self.toggle_password = QCheckBox("Show Password")
        self.toggle_password.stateChanged.connect(self.password_checkbox_toggled)
        Vlayout.addWidget(self.toggle_password)
        Vlayout.addSpacing(14)

        self.rules_label_n1 = QLabel("At least 10 characters")
        self.rules_label_n2 = QLabel("At least one uppercase letter")
        self.rules_label_n3 = QLabel("At least one lowercase letter")
        self.rules_label_n4 = QLabel("At least one number")
        self.rules_label_n5 = QLabel("At least one special character such as # ! @ $ %")

        for label in (self.rules_label_n1, self.rules_label_n2, self.rules_label_n3, self.rules_label_n4, self.rules_label_n5):
            label.setStyleSheet("color: red")
            Vlayout.addWidget(label)
        Vlayout.addSpacing(45)
        self.final_report = QLabel("\t\t\tATTENTION !\n\nIF ALL RULES ABOVE TURNS INTO GREEN COLLOR, USE\nTHE PASSWORD. IF NOT, YOU ARE RISKING YOUR SECURITY.")
        self.final_report.setStyleSheet("color: orange; font-weight: bold;")
        self.final_report.setAlignment(Qt.AlignmentFlag.AlignCenter)
        Vlayout.addWidget(self.final_report)


        Vlayout.addStretch()
        self.setLayout(Vlayout)

    def password_checkbox_toggled(self, state):
        if self.toggle_password.isChecked():
            self.user_password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.toggle_password.setText("Hide Password")
        else:
            self.user_password.setEchoMode(QLineEdit.EchoMode.Password)
            self.toggle_password.setText("Show Password")

    def _on_text_changed(self, text):
        self._update_requirement(self.rules_label_n1, len(text) >= 10)
        self._update_requirement(self.rules_label_n2, bool(re.search(r"[A-Z]", text)))
        self._update_requirement(self.rules_label_n3, bool(re.search(r"[a-z]", text)))
        self._update_requirement(self.rules_label_n4, bool(re.search(r"[0-9]", text)))
        self._update_requirement(self.rules_label_n5, bool(re.search(r"[!@#$%^&*()?:;,.<>]", text)))


    def _update_requirement(self, label, is_valid):
        if is_valid:
            label.setStyleSheet("color: green;")
        else:
            label.setStyleSheet("color: red;")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordChecker()
    window.show()
    sys.exit(app.exec())

    