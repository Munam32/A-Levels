class Sword():
    # PRIVATE xvalue : Integer
    # PRIVATE yvalue : Integer
    # PRIVATE Type : String

    def __init__(self,xvaluep,yvaluep,Typep):
        self.xvalue = xvaluep
        self.yvalue = yvaluep
        self.Type = Typep

    def displaytype(self):
        return self.Type


darksword = Sword(35,46,"Katana")
temp = darksword.displaytype()
print(temp)