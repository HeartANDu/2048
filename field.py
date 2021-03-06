from random import randrange, choices
from copy import deepcopy
from itertools import product

from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QGridLayout

from ui.style import get_block_style
from utils import make_matrix


INIT_VALUES = [2, 4]
VALUES_WEIGHTS = [0.85, 0.15]
FIELD_SIZE = 4


class Block:
    def __init__(self):
        self.value = 0

    def make_label(self) -> QLabel:
        label = QLabel()
        label.setAutoFillBackground(False)
        label.setStyleSheet(get_block_style(self.value))
        label.setText(str(self.value) if self.value > 0 else "")
        label.setScaledContents(False)
        label.setAlignment(QtCore.Qt.AlignCenter)
        return label

    def set_value(self, value: int):
        self.value = value

    def init_value(self):
        self.set_value(choices(INIT_VALUES, VALUES_WEIGHTS)[0])

    def add_value_from(self, value: 'Block'):
        self.set_value(value.value + self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Block):
            return self.value == other.value

        if isinstance(other, int):
            return self.value == other

        return NotImplemented


class Field(QGridLayout):
    def __init__(self, parent):
        super().__init__(parent)
        self.blocks = make_matrix(FIELD_SIZE, Block)
        self.previous_blocks = make_matrix(FIELD_SIZE)
        self.buffered_blocks = make_matrix(FIELD_SIZE)
        self.score = 0
        self.previous_score = 0
        self.buffered_score = 0
        self.full = False
        self.is_undone = True
        self.is_changed = False
        self.init_layout()
        self.init_blocks()

    def init_layout(self):
        self.setGeometry(QtCore.QRect(40, 40, 420, 420))
        self.setContentsMargins(10, 10, 10, 10)
        self.setSpacing(10)
        self.setObjectName('field')

    def init_blocks(self):
        for i in range(2):
            self.blocks[randrange(4)][randrange(4)].init_value()
        self.assign_blocks()

    def reset(self):
        self.blocks = make_matrix(FIELD_SIZE, Block)
        self.previous_blocks = make_matrix(FIELD_SIZE)
        self.score = 0
        self.previous_score = 0
        self.full = False
        self.is_undone = True
        self.init_blocks()

    def assign_blocks(self):
        while self.count():
            child = self.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        for i, j in list(product(range(FIELD_SIZE), range(FIELD_SIZE))):
            self.addWidget(self.blocks[i][j].make_label(), i, j)

    def add_block(self):
        flat_list = [block for row in self.blocks for block in row]
        blocks = list(filter(lambda block: block == 0, flat_list))
        if len(blocks) == 0:
            self.full = True
        elif self.is_changed:
            blocks[randrange(len(blocks))].init_value()

    def check_for_2048_block(self) -> bool:
        flat_list = [block for row in self.blocks for block in row]
        result = next((x for x in flat_list if x == 2048), False)
        return bool(result)

    def move(self):
        self.is_changed = False
        for i in range(FIELD_SIZE):
            for j in range(FIELD_SIZE - 1):
                for k in range(j + 1, FIELD_SIZE):
                    if self.blocks[i][j] == self.blocks[i][k] and \
                            self.blocks[i][j] != 0:
                        self.blocks[i][j].add_value_from(self.blocks[i][k])
                        self.blocks[i][k].set_value(0)
                        self.score += self.blocks[i][j].value
                        self.is_changed = True
                        break
                    elif self.blocks[i][k] != 0:
                        break
            for j in range(FIELD_SIZE - 1):
                if self.blocks[i][j] == 0:
                    for k in range(j + 1, FIELD_SIZE):
                        if self.blocks[i][k] != 0:
                            self.blocks[i][j], self.blocks[i][k] = \
                                self.blocks[i][k], self.blocks[i][j]
                            self.is_changed = True
                            break
        self.add_block()

    def move_left(self):
        self.buffer_current_state()
        self.move()
        self.remember_state()
        self.assign_blocks()

    def move_right(self):
        self.buffer_current_state()
        self.rotate_field()
        self.rotate_field()
        self.move()
        self.rotate_field()
        self.rotate_field()
        self.remember_state()
        self.assign_blocks()

    def move_up(self):
        self.buffer_current_state()
        self.rotate_field()
        self.rotate_field()
        self.rotate_field()
        self.move()
        self.rotate_field()
        self.remember_state()
        self.assign_blocks()

    def move_down(self):
        self.buffer_current_state()
        self.rotate_field()
        self.move()
        self.rotate_field()
        self.rotate_field()
        self.rotate_field()
        self.remember_state()
        self.assign_blocks()

    def rotate_field(self):
        blocks = make_matrix(FIELD_SIZE)
        for i, j in list(product(range(FIELD_SIZE), range(FIELD_SIZE))):
            blocks[j][FIELD_SIZE - 1 - i] = self.blocks[i][j]
        self.blocks = blocks

    def remember_state(self):
        if self.is_changed:
            self.previous_blocks = deepcopy(self.buffered_blocks)
            self.previous_score = self.buffered_score
            self.is_undone = False

    def buffer_current_state(self):
        self.buffered_blocks = deepcopy(self.blocks)
        self.buffered_score = self.score

    def undo(self):
        if not self.is_undone:
            self.blocks = self.previous_blocks
            self.score = self.previous_score
            self.is_undone = True
            self.assign_blocks()
