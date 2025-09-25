class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 

    def average(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Dev", [85, 90, 78])

print(f"{s1.name}'s average marks: {s1.average():.2f}")