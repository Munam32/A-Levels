class Balloon():
    #PRIVATE Health: Integer
    #PRIVATE DefenceItem,Colour: String

    def __init__(self,defenceitemp,colourp):
        self.DefenceItem = defenceitemp
        self.Colour = colourp
        self.Health = 100


    def GetDefenceItem(self):
        return self.DefenceItem

    def ChangeHealth(self,health_addition):
        self.Health = self.Health + health_addition


    def CheckHealth(self):
        if self.Health<=0 :
            return True
        else:
            return False

def Defend(object):
    # Strength : Integer

    Strength = int(input("Enter Strength Of Opponent: "))

    object.ChangeHealth(-Strength)
    print(object.GetDefenceItem())
    if object.CheckHealth() == True:
        print("Your Balloon is dead")
    else:
        print("Your Balloon is still in the air")
    return object


defence_item = input("Enter Defence Item: ")
colour = input("Enter Colour: ")
Balloon1 = Balloon(defence_item,colour)
Balloon1 = Defend(Balloon1) # Always store the result of a function even when not mentioned in the question








