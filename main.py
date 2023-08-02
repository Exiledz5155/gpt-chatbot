from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
from backend import Chatbot

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)

        # Add chat area
        self.chat_area = QTextEdit(self)
        # 10 pixels from left border 10 pixels from top border, width and height
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add input area
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)

        # Add button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        #user_input = self.input_field.text().strip()
        user_input = "tell me a story about a frog"
        self.chat_area.append(f"<p style='color:#212121'>User: {user_input}</p>")
        self.input_field.clear()

        response = self.chatbot.get_response(user_input)
        #response = "test"

        self.chat_area.append(f"<p style='color:#212121; background-color: #E9E9E9'>Bot: {response}</p>")

app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())