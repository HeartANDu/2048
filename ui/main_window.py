from PyQt5 import QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget, QLabel

from ui import UndoButton, ResetButton
from ui.style import MAIN_BACKGROUND_COLOR, TEXT_COLORS
from field import Field

END_OVERLAY_STYLE = 'background-color: rgba(255, 255, 255, 0.7); ' \
                    'font-size: 30pt; font-weight: bold; color: #776e65;'


class UiMainWindow:
    def init_ui(self, main_window):
        main_window.setFixedSize(500, 600)
        main_window.setWindowTitle('2048')
        central = QWidget(main_window)
        central.setObjectName('central')
        main_window.setCentralWidget(central)

        background = QWidget(central)
        background.setObjectName('background')
        background.setStyleSheet('background-color: %s;' %
                                 MAIN_BACKGROUND_COLOR)
        background.setGeometry(10, 110, 480, 480)
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

        self.field = Field(background)
        background.setLayout(self.field)

        self.undo_button = UndoButton(central)
        self.reset_button = ResetButton(central)
        self.logo = UiLogo(central)
        self.score = UiScore(central)


class UiLogo(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText('2048')
        self.setStyleSheet('color: %s; font-size: 48pt; '
                           'font-weight: bold;' % (TEXT_COLORS['dark']))
        self.setGeometry(QRect(35, 20, 200, 80))
        self.setAlignment(QtCore.Qt.AlignCenter)


class UiScore(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.text = 'Score:\n%s'
        self.update_score(0)
        self.setStyleSheet('background-color: %s; color: %s; font-size: 14pt; '
                           'font-weight: bold; border-radius: 5px;' %
                           (MAIN_BACKGROUND_COLOR, TEXT_COLORS['light']))
        self.setGeometry(QRect(260, 35, 100, 50))
        self.setAlignment(QtCore.Qt.AlignCenter)

    def update_score(self, score: int):
        self.setText(self.text % score)
