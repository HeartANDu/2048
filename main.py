from PyQt5 import QtWidgets

import sys
import application


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = application.Window()
    window.show()
    sys.exit(app.exec_())


# TODO make scoreboard
# TODO make clickable menu
# TODO make unlimited mode
# TODO make some visual adjustments
# TODO add undo
if __name__ == '__main__':
    main()
