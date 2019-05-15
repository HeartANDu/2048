import sys

from PyQt5.QtWidgets import QMainWindow, qApp
from PyQt5 import QtCore

from ui import UiMainWindow


class MainWindow(QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()
        self.win = False
        self.fail = False
        self.init_ui(self)
        qApp.installEventFilter(self)
        self.undo_button.clicked.connect(self.undo)
        self.reset_button.clicked.connect(self.reset)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress:
            self.keyPressEvent(event)
            return True
        return super(MainWindow, self).eventFilter(source, event)

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
            elif event.key() == QtCore.Qt.Key_U:
                self.undo(is_key=True)
            self.update_score()
            self.check_ending()
        event.accept()

    def check_ending(self):
        if self.field.check_for_2048_block():
            self.win = True
            self.show_win_message()
        if self.field.full:
            self.fail = True
            self.show_fail_message()

    def update_score(self):
        self.score.update_score(self.field.score)

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

    def undo(self, **kwargs):
        is_key = False if 'is_key' not in kwargs else kwargs['is_key']
        self.field.undo()
        if not is_key:
            self.update_score()
            self.check_ending()
