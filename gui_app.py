# pip install pyqt5
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

        self.__init_ui()
        self.show()

    def __init_ui(self):
        self.setWindowTitle('Test...')

        # main panel init
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)

        # init window geometry
        self.__init_main_window()

        # init button
        self.__init_toggle_button()

        # init window flags (transparent, normal)
        # 한번씩 초기화 안하면 버그 생김 (이유는 모르겠음)
        self.__set_transparent_window()
        self.show()
        self.hide()
        self.__set_normal_window()

    def __init_main_window(self):
        self.posX = 300
        self.posY = 300
        self.window_width = 300
        self.window_height = 300
        self.move(self.posX, self.posY)
        self.resize(self.window_width, self.window_height)

    def __init_toggle_button(self):
        self.button_width = 50
        self.button_height = 50
        self.toggle_buttton = QtWidgets.QPushButton(self)
        self.toggle_buttton.setIcon(QtGui.QIcon('btn.png'))
        self.toggle_buttton.setIconSize(QtCore.QSize(self.button_width, self.button_height))
        self.__set_button_position()
        self.toggle_buttton.clicked.connect(self.__on_toggle_button)

    def __set_button_position(self):
        self.toggle_buttton.move(self.window_width - self.button_width, 0)
        self.toggle_buttton.resize(self.button_width, self.button_height)

    def __on_toggle_button(self):
        self.hide()
        if self.bTransparentFlag:
            self.__set_normal_window()
            self.bTransparentFlag = False
        else:
            self.__set_transparent_window()
            self.bTransparentFlag = True
        self.show()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        super(MyApp, self).resizeEvent(a0)
        self.window_width = self.width()
        self.window_height = self.height()
        self.__set_button_position()

    # show normal window
    def __set_normal_window(self):
        self.move(self.posX, self.posY)
        self.setStyleSheet('background-color: white; border : 2px solid green;')
        self.setWindowFlags(self.window_flag_normal)
        self.setWindowOpacity(0.7)

    # show transparent window
    def __set_transparent_window(self):
        self.posX = self.pos().x().real
        self.posY = self.pos().y().real
        self.setStyleSheet('background-color: transparent; border : 2px solid red;')
        self.setWindowFlags(self.window_flag_transparent)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowOpacity(1.0)

    # left top XY
    # width height
    def get_rect(self) -> []:
        return [self.posX,
                self.posY,
                self.window_width,
                self.window_height]

    # transparent 상태 일 때 action
    def is_available(self) -> bool:
        return self.bTransparentFlag

    @staticmethod
    def run():
        app = QtWidgets.QApplication(sys.argv)
        myApp = MyApp()
        sys.exit(app.exec_())

app = QtWidgets.QApplication(sys.argv)
myApp = MyApp()
sys.exit(app.exec_())
