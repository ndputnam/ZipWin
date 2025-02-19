from sys import argv
from PyQt6.QtWidgets import QApplication
from resources.zipper import Zippy

#TODO:
# create windows desktop band object
# https://learn.microsoft.com/en-us/previous-versions/windows/desktop/legacy/cc144099(v=vs.85)?redirectedfrom=MSDN
# add a windows self installer
# https://installforge.net/
# https://www.pythonguis.com/tutorials/packaging-pyside6-applications-windows-pyinstaller-installforge/
#


class PyPackager(QApplication):
    def __init__(self):
        super().__init__(argv)
        Zippy().show()
        exit(self.exec())


if __name__ == "__main__":
    PyPackager()
