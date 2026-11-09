#imports
import sys
import pyautogui
import time

#importing the required modules from PySide6
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainterPath, QBrush, QColor, QRegion, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QVBoxLayout,
    QWidget
)
from qfluentwidgets import (
    BodyLabel,
    TextEdit,
    PushButton,
    LineEdit,
    setTheme,
    setThemeColor,
    Theme
)
#importing os module to handle file paths
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#main window class
class Window(QMainWindow):
    def __init__(self):
        #Initializing the main window
        super().__init__()
        self.setWindowIcon(QIcon(resource_path("autowriter_icon.ico")))
        self.setWindowTitle("AutoWriter")
        self.resize(450, 400)

        #Widget and layout setup
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(25, 25, 25, 25)

        #Adding the title label
        TitleLabel = BodyLabel("AutoWriter")
        TitleLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(TitleLabel)

        #Styling the title label
        TitleLabel.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: white;
        """)

        #Styling the window and central widget
        self.setStyleSheet("""
            fluentWindow {
                background-color: #141414;
            }
        """)

        central_widget.setStyleSheet("""
                background-color: #141414;
                color: white;
        """)

        #Adding text label
        subtitleLabel = BodyLabel("Paste your text that u want to write below")
        layout.addWidget(subtitleLabel)
        
        #Styling the subtitle label
        subtitleLabel.setStyleSheet("""
            font-size: 14px;
            color: #A0A0A0;
        """)

        #Adding the text edit box
        self.text = TextEdit()
        self.text.setPlaceholderText("Paste your text here...")
        layout.addWidget(self.text)

        #Adding Button
        self.start_button = PushButton("Start Writing")
        self.start_button.clicked.connect(self.start)
        layout.addWidget(self.start_button)

        #Styling the button
        self.start_button.setStyleSheet("""
            background-color: #4585ff;
            padding: 10px 20px;
            color: White;
            font-size: 14px;
            font-weight: bold;
            border-radius: 10px;
            border: none;
        """)

        #Adding the delay label
        self.speed = BodyLabel("Delay before writing (seconds):")
        self.speed.setStyleSheet("""
            font-size: 14px;
            color: #A0A0A0;
        """)

        layout.addWidget(self.speed)

        #Seconds
        self.Seconds = LineEdit()
        self.Seconds.setPlaceholderText("Enter delay in seconds")
        layout.addWidget(self.Seconds)

    #Start function to start the writing process
    def start(self):
        text = self.text.toPlainText()
        try:
            seconds = int(self.Seconds.text())
            if seconds < 1:
                QMessageBox.warning(self, "Error","Delay cannot be negative")
                return
        except ValueError:
            QMessageBox.warning(self, "Error","Please enter a valid number for delay")
            return
        
        time.sleep(seconds)  # Delay to switch to the target application
        pyautogui.write(text, interval=0.05)  # U can adjust the interval if u want
        print(text)

if __name__ == "__main__":
    #Creating the application and window
    app = QApplication(sys.argv)
    setTheme(Theme.DARK)
    setThemeColor("#4585ff")
    window = Window()
    window.show()

    sys.exit(app.exec())