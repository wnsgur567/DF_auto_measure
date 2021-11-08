import sys
from PyQt5 import QtCore, QtWidgets, QtGui


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        # toggle
        self.toggle_buttton: QtWidgets.QPushButton

        # member variables
        # window geometry
        self.posX = 0
        self.posY = 0
        self.window_width = 0
        self.window_height = 0

        # window flags
        self.bTransparentFlag = False
        self.window_flag_normal = self.windowFlags()
        self.window_flag_transparent = QtCore.Qt.WindowFlags(
            QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        # init button variable
        self.button_width = 0
        self.button_height = 0

        self.init_ui()
        self.show()

    def init_ui(self):
        # main panel init
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)

        # init window geometry
        self.init_main_window()

        # init button
        self.init_toggle_button()

        # init window flags (transparent, normal)
        # 한번씩 초기화 안하면 버그 생김 (이유는 모르겠음)
        self.set_transparent_window()
        self.show()
        self.hide()
        self.set_normal_window()

    def init_main_window(self):
        self.posX = 300
        self.posY = 300
        self.window_width = 300
        self.window_height = 300
        self.move(self.posX, self.posY)
        self.resize(self.window_width, self.window_height)

    def init_toggle_button(self):
        self.button_width = 50
        self.button_height = 50
        self.toggle_buttton = QtWidgets.QPushButton(self)
        self.toggle_buttton.setIcon(QtGui.QIcon('btn.png'))
        self.toggle_buttton.setIconSize(QtCore.QSize(self.button_width, self.button_height))
        self.set_button_position()
        self.toggle_buttton.clicked.connect(self.on_toggle_button)

    def set_button_position(self):
        self.toggle_buttton.move(self.window_width - self.button_width, 0)
        self.toggle_buttton.resize(self.button_width, self.button_height)

    def on_toggle_button(self):
        self.hide()
        if self.bTransparentFlag:
            self.set_normal_window()
            self.bTransparentFlag = False
        else:
            self.set_transparent_window()
            self.bTransparentFlag = True
        self.show()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        super(MyApp, self).resizeEvent(a0)
        self.window_width = self.width()
        self.window_heigt = self.height()
        self.set_button_position()

    # show normal window
    def set_normal_window(self):
        self.move(self.posX, self.posY)
        self.setStyleSheet('background-color: white; border : 2px solid green;')
        self.setWindowFlags(self.window_flag_normal)
        self.setWindowOpacity(0.5)

    # show transparent window
    def set_transparent_window(self):
        self.posX = self.pos().x().real
        self.posY = self.pos().y().real
        self.setStyleSheet('background-color: transparent; border : 2px solid red;')
        self.setWindowFlags(self.window_flag_transparent)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowOpacity(1.0)


app = QtWidgets.QApplication(sys.argv)
myApp = MyApp()
sys.exit(app.exec_())
