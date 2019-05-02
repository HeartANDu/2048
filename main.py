import sys

from PyQt5.QtWidgets import QApplication
from application import MainWindow


# TODO make clickable menu (buttons implemented)
# TODO make unlimited mode
# TODO make settings
# TODO maybe animations?
# TODO debug mode
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
