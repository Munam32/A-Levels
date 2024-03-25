class TreasureChest():
    # PRIVATE question : String
    # PRIVATE answer,points : Integer

    def __init__(self,Questionp,Answerp,Pointsp):
        self.question = Questionp
        self.answer = Answerp
        self.points = Pointsp

    def getQuestion(self):
        return self.question

    def checkAnswer(self, useranswer):
        if useranswer == self.answer:
            return True
        else:
            return False

    def getPoints(self, attempts):
        if attempts == 1:
            return self.points

        elif(attempts == 2):
            return int(self.points//2)

        elif(attempts == 3 or attempts == 4):
            return int(self.points // 4)

        else:
            return 0


