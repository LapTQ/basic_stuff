

class Student():
    def __init__(self, ID, name, scores):
        
        self.ID = ID
        self.name = name
        self.scores = scores
        self.progress = round(0.4*scores[0] + 0.2*scores[1] + 0.4*scores[2], 1)
        self.final = round(0.5*self.progress + 0.5*scores[3], 1)
        if 10 >= self.final >= 8.5:
            self.gpa = "A"
        elif 8.4 >= self.final >= 7.0:
            self.gpa = "B"
        elif 6.9 >= self.final >= 5.5:
            self.gpa = "C"
        elif 5.4 >= self.final >= 4.0:
            self.gpa = "D"
        else:
            self.gpa = "F"

    def __str__(self):
        return "{:<8}   {:<6}   {:>3}   {:>9}   {:>8}   {:>8}   {:>8}   {:>5}   {:<4}".format(self.ID, self.name, *self.scores[:3], self.progress, self.scores[3], self.final, self.gpa)

def report(outfile):
    while True:
        data = input("Student info (<Enter> to quit): ")
        if data == "":
            break
        info = data.split()
        print(str(Student(info[0], info[1], [float(i) for i in info[2:]])), file=outfile)

outfile = open("report.txt", "w")
print("{:<8}   {:<6}   {:<3}   {:<9}   {:<8}   {:<8}   {:<8}   {:<5}   {:<4}".format("ID", "Name","Lab", "Exercises", "Mid-test", "Progress", "Fin-test", "Final", "GPA"), file=outfile)
report(outfile)
outfile.close()


