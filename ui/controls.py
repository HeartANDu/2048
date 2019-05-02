import qtawesome as qta

from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import QPushButton

from ui.style import TEXT_COLORS, MAIN_BACKGROUND_COLOR as bg


CONTROLS_STYLE = 'border-radius: 5px; background-color: %s;' % bg


class UndoButton(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet(CONTROLS_STYLE)
        self.setAutoFillBackground(True)
        self.setIcon(qta.icon('fa5s.undo-alt', color=TEXT_COLORS['light']))
        self.setIconSize(QSize(30, 30))
        self.setFlat(True)
        self.setGeometry(QRect(385, 40, 40, 40))


class ResetButton(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet(CONTROLS_STYLE)
        self.setAutoFillBackground(True)
        self.setIcon(qta.icon('fa5s.sync-alt', color=TEXT_COLORS['light']))
        self.setIconSize(QSize(30, 30))
        self.setFlat(True)
        self.setGeometry(QRect(435, 40, 40, 40))
