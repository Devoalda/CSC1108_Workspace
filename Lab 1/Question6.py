class Student:
    def __init__(self, name, student_number, examDict):
        self.name = name
        self.student_number = student_number
        self.examDict = examDict

    def getBestExamScore(self):
        return max(self.examDict, key=self.examDict.get)

    def getFaileModules(self):
        listOfFailedModules = []
        for key, value in self.examDict.items():
            if value < 40:
                listOfFailedModules.append(key)

        print(listOfFailedModules)
    # return [key for key, value in self.examDict.items() if value < 40]

    def addScore(self, subjectCode, examScore):
        self.examDict[subjectCode] = examScore

    def printScore(self):
        print(self.name)
        print(self.examDict)


if __name__ == '__main__':
    examDict = {"ICT1008": 96, "ICT1002": 78, "ICT1005": 30}
    student = Student("Cristal", "123456", examDict)
    student.addScore("ICT1010", 70)
    student.printScore()
    print(student.getBestExamScore())
    student.getFaileModules()
