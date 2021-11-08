import sys
from PyQt5 import QtCore, QtWidgets, QtGui


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        # member variables
        # window geometry
        self.posX = 0
        self.posY = 0
        self.window_width = 0
        self.window_height = 0
        # window flags
        self.window_flag_normal = self.windowFlags()
        self.window_flag_transparent = QtCore.Qt.WindowFlags(
            QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        self.init_ui()

    def init_ui(self):
        # main panel init
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)

        # window opacity
        self.setWindowOpacity(0.5)

        # set init geometry
        self.posX = 300
        self.posY = 300
        self.window_width = 300
        self.window_height = 300
        self.move(self.posX, self.posY)
        self.resize(self.window_width,self.window_height)



    def show_normal_window(self):
        self.setWindowFlags(self.window_flag_normal)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.show()

    def show_transparent_window(self):
        self.setWindowFlags(self.window_flag_transparent)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, False)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, False)
        self.show()
