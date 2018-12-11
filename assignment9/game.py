#-*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QMessageBox
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton

from hangman import Hangman
from guess import Guess
from word import Word


class HangmanGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize word database        
        self.word = Word('words.txt')

        # Hangman display window
        self.hangmanWindow = QTextEdit()
        self.hangmanWindow.setReadOnly(True)
        self.hangmanWindow.setAlignment(Qt.AlignLeft)
        font = self.hangmanWindow.font()
        font.setFamily('Courier New')
        self.hangmanWindow.setFont(font)

        # Layout
        hangmanLayout = QGridLayout()
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        # Status Layout creation
        statusLayout = QGridLayout()

        # Display widget for current status
        self.currentWord = QLineEdit()
        self.currentWord.setReadOnly(True)
        self.currentWord.setAlignment(Qt.AlignCenter)
        font = self.currentWord.font()
        font.setPointSize(font.pointSize() + 8)
        self.currentWord.setFont(font)
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)

        # Display widget for already used characters
        self.guessedChars = QLineEdit()
        self.guessedChars.setReadOnly(True)
        self.guessedChars.setAlignment(Qt.AlignLeft)
        self.guessedChars.setMaxLength(52)
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)

        # Display widget for message output
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)
        self.message.setMaxLength(52)
        statusLayout.addWidget(self.message, 2, 0, 1, 2)

        # Input widget for user selected characters
        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1)
        statusLayout.addWidget(self.charInput, 3, 0)

        # Button for submitting a character
        self.guessButton = QToolButton()
        self.guessButton.setText('Guess!')
        self.guessButton.clicked.connect(self.guessClicked)
        statusLayout.addWidget(self.guessButton, 3, 1)

        # Button for a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.startGame)
        statusLayout.addWidget(self.newGameButton, 4, 0)



        # Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle('Hangman Game')

        # Start a new game on application launch!
        self.startGame()


    def startGame(self):
        self.hangman = Hangman()
        self.guess = Guess(self.word.randFromDB())
        if len(self.guess.secretWord) < 10:
            self.guess = Guess(self.word.randFromDB())



        self.gameOver = False

        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        self.currentWord.setText(self.guess.displayCurrent())
        self.guessedChars.setText(self.guess.displayGuessed())
        self.message.clear()


    def guessClicked(self):
        guessedChar = self.charInput.text()
        self.charInput.clear()
        self.message.clear()

        if self.gameOver == True:
            # 메시지 출력하고 - message.setText() - 리턴
            return self.message.setText("GameOver! Click the New Game")



        # 입력의 길이가 1 인지를 판단하고, 아닌 경우 메시지 출력, 리턴
        #ord('a'), ord('z')로 수정
        if len(guessedChar) != 1 or ord(guessedChar) > ord('z') or ord(guessedChar) < ord('a'):

            return self.message.setText('Only One Alphabet Please!')




        # 이미 사용한 글자인지를 판단하고, 아닌 경우 메시지 출력, 리턴
        if guessedChar in self.guess.guessedChars:

            return self.message.setText('You already guessed \"' + guessedChar + '\"')

        success = self.guess.guess(guessedChar)
        if success == False:
            # 남아 있는 목숨을 1 만큼 감소
            self.hangman.decreaseLife()
            if self.hangman.getRemainingLives() == 0:
                self.gameOver = True
                return self.message.setText('Fail! Answer is ' + self.guess.secretWord)
            self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
            self.guessedChars.setText(self.guess.displayGuessed())
            # 메시지 출력

            return self.message.setText('Extra Life: ' + str(self.hangman.remainingLives))

        elif success == True:
            self.message.setText('\"' + guessedChar + ' \"is Correct!')

        # hangmanWindow 에 현재 hangman 상태 그림을 출력
        # currentWord 에 현재까지 부분적으로 맞추어진 단어 상태를 출력
        self.currentWord.setText(self.guess.displayCurrent())
        # guessedChars 에 지금까지 이용한 글자들의 집합을 출력
        self.guessedChars.setText(self.guess.displayGuessed())

        if self.guess.finished():
            # 메시지 ("Success!") 출력하고, self.gameOver 는 True 로
            self.message.setText("Success!")
            self.gameOver = True




if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = HangmanGame()
    game.show()
    sys.exit(app.exec_())

