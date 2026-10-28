#multi - level student performance mark
class academic:
    def accept(self):
        self.regno = input("Enter Registration Number: ")
        self.name = input("Enter Student Name: ")
        self.acdmark = float(input("Enter Academic Marks: "))
class research(academic):
    def accept_research(self):
        self.researchmark = float(input("Enter Research Work Marks: "))
class curricular_activities(research):
    def accept_curricular(self):
        self.curricularmark = float(input("Enter Curricular Activities Marks: "))
class student(curricular_activities):
    def display(self):
        self.total = self.acdmark + self.researchmark + self.curricularmark
        self.average = self.total / 3
        print("\n----- Student Performance Report -----")
        print("Registration Number:", self.regno)
        print("Student Name:", self.name)
        print("Academic Marks:", self.acdmark)
        print("Research Work Marks:", self.researchmark)
        print("Curricular Activities Marks:", self.curricularmark)
        print("Total Marks:", self.total)
        print("Average Marks:", self.average)
s = student()
s.accept()
s.accept_research()
s.accept_curricular()
s.display()
