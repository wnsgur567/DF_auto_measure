import sys

from PyQt5 import QtCore, QtWidgets, QtGui


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        self.bTransparentFlag = False
        # 투명 아닌 window flag
        self.before_flags = self.windowFlags()
        # 투명 window flag
        self.transform_flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        self.window_width = 0
        self.window_height = 0
        self.__pos = self.pos

        self.init_ui()
        self.show()

    def init_ui(self):
        # main panel
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)

        self.setWindowFlags(self.transform_flags)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, False)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, False)
        self.setStyleSheet('border : 2px solid red')
        self.show()
        self.hide()

        self.setWindowFlags(self.before_flags)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowOpacity(0.3)
        self.setStyleSheet('background-color: white; border : 2px solid green;')

        # pos
        self.move(300, 300)
        self.__pos = self.pos()

        self.window_width = 300
        self.window_height = 400

        # size
        self.resize(self.window_width, self.window_height)

        # exit_button = QtWidgets.QPushButton(central_widget)
        # exit_button.resize(20, 20)
        # exit_button.setStyleSheet('Color : green')

        # exit button
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setIcon(QtGui.QIcon('btn.png'))
        self.btn.setIconSize(QtCore.QSize(50, 50))
        self.btn.move(self.window_width - 50, 0)
        self.btn.resize(50, 50)
        self.btn.clicked.connect(self.toggle_transparent)

    # 어플리케이션 종료
    @staticmethod
    def exit_button_clicked(self):
        QtWidgets.qApp.exit()

    def toggle_transparent(self):
        self.hide()
        if self.bTransparentFlag:
            self.setWindowFlags(self.before_flags)
            self.setAttribute(QtCore.Qt.WA_NoSystemBackground, not self.bTransparentFlag)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground, not self.bTransparentFlag)
            self.move(self.__pos)
            self.setStyleSheet('border : 2px solid green')
        else:
            self.__pos = self.pos()
            self.setWindowFlags(self.transform_flags)
            self.setAttribute(QtCore.Qt.WA_NoSystemBackground, not self.bTransparentFlag)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground, not self.bTransparentFlag)
            self.setStyleSheet('border : 2px solid red')

        self.bTransparentFlag = not self.bTransparentFlag
        self.resize(self.window_width, self.window_height)
        self.show()


app = QtWidgets.QApplication(sys.argv)

myApp = MyApp()

sys.exit(app.exec_())
