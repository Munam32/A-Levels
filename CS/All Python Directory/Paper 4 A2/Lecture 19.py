class Member():
    # PRIVATE MemberName,MemberID: String
    # PRIVATE SubscriptionPaid : Boolean

    def __init__(self):
        self.__MemberName =  ""
        self.__MemberID = ""
        self.__SubscriptionPaid = False

    def SetMemberName(self,Name):
        self.__MemberName = Name

    def SetMemberID(self,ID):
        self.__MemberID = ID

    def SetSubscriptionPaid(self,Paid):
        self.__SubscriptionPaid = Paid




class JuniorMember(Member):
    # PRIVATE DateOfBirth : String

    def __init__(self):
        self.__DateOfBirth = ""
        super().__init__()

    def SetDateOfBirth(self,DOB):
        self.__DateOfBirth = DOB


    def SetMemberName(self,Name):
        super().SetMemberName(Name)

    def SetMemberID(self,ID):
        super().SetMemberID(ID)

    def SetSubscriptionPaid(self,Paid):
        super().SetSubscriptionPaid(Paid)


NewMember = JuniorMember()
NewMember.SetMemberID("12347")
NewMember.SetDateOfBirth("12/11/2001")
NewMember.SetSubscriptionPaid(True)


















