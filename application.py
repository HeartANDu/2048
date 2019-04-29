import sys

from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5 import QtCore

from field import Field


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.win = False
        self.fail = False
        self.init_ui()

    def init_ui(self):
        self.resize(500, 500)
        self.setWindowTitle('2048')
        background = QLabel(self)
        background.setGeometry(QtCore.QRect(10, 10, 480, 480))
        background.setStyleSheet('background-color: rgb(187, 173, 160);')
        background.setText('')
        background.setObjectName('background')
        background.raise_()

        self.field = Field(self)
        self.setLayout(self.field)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            sys.exit(0)
        if not self.win and not self.fail:
            if event.key() == QtCore.Qt.Key_Up:
                self.field.move_up()
            elif event.key() == QtCore.Qt.Key_Down:
                self.field.move_down()
            elif event.key() == QtCore.Qt.Key_Right:
                self.field.move_right()
            elif event.key() == QtCore.Qt.Key_Left:
                self.field.move_left()
            self.check_ending()
        event.accept()

    def check_ending(self):
        if self.field.check_for_2048_block():
            self.win = True
            self.show_win_message()
        if self.field.full:
            self.fail = True
            self.show_fail_message()

    def show_win_message(self):
        win_label = QLabel(self)
        win_label.setGeometry(QtCore.QRect(10, 10, 480, 480))
        win_label.setStyleSheet('background-color: rgba(255, 255, 255, 0.7);')
        win_label.setText('You won! Congratulations!')
        win_label.setAlignment(QtCore.Qt.AlignCenter)
        win_label.show()
        win_label.raise_()

    def show_fail_message(self):
        fail_label = QLabel(self)
        fail_label.setGeometry(QtCore.QRect(10, 10, 480, 480))
        fail_label.setStyleSheet('background-color: rgba(255, 255, 255, 0.7);')
        fail_label.setText('You lost. Try again.')
        fail_label.setAlignment(QtCore.Qt.AlignCenter)
        fail_label.show()
        fail_label.raise_()