import sys

from PyQt5.QtWidgets import QWidget, QLabel, QMainWindow
from PyQt5 import QtCore

from field import Field


END_OVERLAY_STYLE = 'background-color: rgba(255, 255, 255, 0.7); ' \
                    'font-size: 30pt; font-weight: bold; color: #776e65;'


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win = False
        self.fail = False
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(500, 500)
        self.setWindowTitle('2048')
        central = QWidget(self)
        self.setCentralWidget(central)
        background = QWidget(central)
        background.setStyleSheet('background-color: rgb(187, 173, 160);')
        background.setGeometry(10, 10, 480, 480)
        background.raise_()

        self.win_label = QLabel(central)
        self.win_label.resize(500, 500)
        self.win_label.setStyleSheet(END_OVERLAY_STYLE)
        self.win_label.setText('You won!\nCongratulations!')
        self.win_label.setAlignment(QtCore.Qt.AlignCenter)
        self.win_label.hide()

        self.fail_label = QLabel(central)
        self.fail_label.resize(500, 500)
        self.fail_label.setStyleSheet(END_OVERLAY_STYLE)
        self.fail_label.setText('You lost.\nTry again.')
        self.fail_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fail_label.hide()

        self.field = Field(self)
        background.setLayout(self.field)


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            sys.exit(0)
        elif event.key() == QtCore.Qt.Key_R:
            self.reset()
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
        self.win_label.show()
        self.win_label.raise_()

    def show_fail_message(self):
        self.fail_label.show()
        self.fail_label.raise_()

    def reset(self):
        self.win = False
        self.fail = False
        self.win_label.hide()
        self.fail_label.hide()
        self.field.reset()
