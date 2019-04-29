from random import randrange, choices

from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QGridLayout

from style import style


INIT_VALUES = [2, 4]
VALUES_WEIGHTS = [0.85, 0.15]


class Block(QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setAutoFillBackground(False)
        self.setStyleSheet(style.get_style(0))
        self.setText("")
        self.setScaledContents(False)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.value = 0

    def set_value(self, value: int):
        self.value = value
        self.setStyleSheet(style.get_style(value))
        if value > 0:
            self.setText(str(value))
        else:
            self.setText('')

    def init_value(self):
        self.set_value(choices(INIT_VALUES, VALUES_WEIGHTS)[0])

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()


class Field(QGridLayout):
    def __init__(self, parent):
        super().__init__(parent)
        self.blocks = [[Block() for j in range(4)] for i in range(4)]
        self.full = False
        self.init_layout()
        self.init_blocks()

    def init_layout(self):
        self.setContentsMargins(20, 20, 20, 20)
        self.setSpacing(10)

    def init_blocks(self):
        self.assign_blocks()
        for i in range(2):
            self.blocks[randrange(4)][randrange(4)].init_value()

    def assign_blocks(self):
        positions = [(i, j) for i in range(4) for j in range(4)]
        for i, j in positions:
            self.addWidget(self.blocks[i][j], i, j)

    def add_block(self, is_changed: bool):
        flat_list = [block for row in self.blocks for block in row]
        blocks = list(filter(lambda block: block.value == 0, flat_list))
        if len(blocks) == 0:
            self.full = True
        elif is_changed:
            blocks[randrange(len(blocks))].init_value()

    def check_for_2048_block(self):
        flat_list = [block for row in self.blocks for block in row]
        result = next((x.value for x in flat_list if x.value == 2048), False)
        return bool(result)

    def move_left(self):
        changed = False
        for i in range(4):
            for j in range(3):
                for k in range(j + 1, 4):
                    if self.blocks[i][j].value == self.blocks[i][k].value and self.blocks[i][j].value != 0:
                        new_value = self.blocks[i][j].value + self.blocks[i][k].value
                        self.blocks[i][j].set_value(new_value)
                        self.blocks[i][k].set_value(0)
                        changed = True
                        break
                    elif self.blocks[i][k].value != 0:
                        break
            for j in range(3):
                if self.blocks[i][j].value == 0:
                    for k in range(j + 1, 4):
                        if self.blocks[i][k].value != 0:
                            self.blocks[i][j], self.blocks[i][k] = self.blocks[i][k], self.blocks[i][j]
                            changed = True
                            break
        self.add_block(changed)
        self.assign_blocks()

    def move_right(self):
        self.rotate_field()
        self.rotate_field()
        self.move_left()
        self.rotate_field()
        self.rotate_field()
        self.assign_blocks()


    def move_up(self):
        self.rotate_field()
        self.rotate_field()
        self.rotate_field()
        self.move_left()
        self.rotate_field()
        self.assign_blocks()

    def move_down(self):
        self.rotate_field()
        self.move_left()
        self.rotate_field()
        self.rotate_field()
        self.rotate_field()
        self.assign_blocks()

    def rotate_field(self):
        blocks = [[None for j in range(4)] for i in range(4)]
        for i in range(4):
            for j in range(4):
                blocks[j][3 - i] = self.blocks[i][j]
        self.blocks = blocks
