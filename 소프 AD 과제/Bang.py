import random

class Bomb:
    def __init__(self,num):
        self.randNum = random.randint(0, num+1)

    def checkBomb(self,num):
        if num < self.randNum:
            return False
        else:
            return True


if __name__ == "__main__":
    bang = Bomb(100)