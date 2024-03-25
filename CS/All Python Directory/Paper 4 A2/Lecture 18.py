class Lesson():
    # PRIVATE LessonType : String
    # PRIVATE Instructor : String

    def __init__(self,LessonTypeP,InstructorP):
        self.__LessonType = LessonTypeP
        self.__Instructor = InstructorP


    def GetLessonType(self):
        return self.__LessonType

    def GetInstructor(self):
        return self.__Instructor

    def SetLessonType(self,NewLessonType):
        self.__LessonType = NewLessonType

    def SetInstructor(self,NewInstructor):
        self.__Instructor = NewInstructor


    def GetFee(self,Skill_Level):

        if Skill_Level == "B":
            return 45

        elif Skill_Level == "I":
            return 50

        elif Skill_Level == "A":
            return 55

        else:
            return -1

# LessonArray : ARRAY [0:8] OF Lesson
LessonArray=[]

for x in range(9):
    LessonArray[x] = ""

LessonArray[2] = Lesson("Improve Your Serve","David")







