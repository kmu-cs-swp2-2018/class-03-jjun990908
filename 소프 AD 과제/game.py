import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget , QLabel
from PyQt5.QtWidgets import QLayout, QGridLayout, QMessageBox
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from PyQt5.QtGui import QPixmap

from Bang import Bomb

class BombGame(QWidget):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.img = QPixmap('IMG.png')
        self.lbImg = QLabel()
        self.lbImg.setPixmap((self.img))
        self.current = 0
        self.box = QMessageBox()
        self.box.setWindowTitle("")
        self.box.setStandardButtons(QMessageBox.Ok)
        self.btnNewGame = QToolButton()
        self.btnCounter = QToolButton()
        self.lbInform = QLabel('버튼을 클릭하세요 >>>')
        self.btnNewGame.clicked.connect(self.startGame)
        self.btnCounter.clicked.connect(self.btnCounterClicked)
        self.btnCounter.setFixedSize(200,200)
        self.btnCounter.setText("PLUS")
        self.btnNewGame.setText("New Game")
        self.btnNewGame.setFixedWidth(460)
        self.range = QLineEdit("0")
        self.lbRange = QLabel("")
        self.lbCurrent = QLabel("")
        labelLayout = QGridLayout()
        labelLayout.addWidget(self.lbInform,0,0)
        labelLayout.addWidget(self.lbRange,1,0)
        labelLayout.addWidget(self.lbCurrent,2,0)
        mainLayout = QGridLayout()
        mainLayout.addWidget(self.range,0,0,1,2)
        mainLayout.addWidget(self.btnNewGame,1,0,1,2)
        mainLayout.addLayout(labelLayout,2,0)
        mainLayout.addWidget(self.btnCounter,2,1)
        mainLayout.addWidget(self.lbImg,3,0,1,2)
        self.setLayout(mainLayout)
        self.setWindowTitle("BANG")



    def startGame(self):
        try:
            self.current = 0
            self.bang = Bomb(int(self.range.text()))
            self.lbRange.setText("수의 범위는 0 부터" + str(self.range.text()) + " 입니다.")
            self.lbCurrent.setText("현재 숫자는 "+ str(self.current) + "입니다.")
            self.btnCounter.setEnabled(True)
        except:
            pass

    def btnCounterClicked(self):
        self.current += 1
        self.lbCurrent.setText("현재 숫자는 " + str(self.current) + " 입니다.")
        if self.bang.checkBomb(self.current) == False:
            pass
        else:
            self.btnCounter.setEnabled(False)
            self.box.setText("BANG")
            self.box.show()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    game = BombGame()
    game.show()
    sys.exit(app.exec_())