class Student:

    def __init__(self, first, last, year):
        self.first = first
        self.last = last
        self.year = year

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Student('{}', '{}', {})".format(self.first, self.last, self.year)


class Branch(Student):
    def __init__(self, first, last, year, branch):
        super().__init__(first,last,year)
        self.branch = branch

    def __repr__(self):
        return "Branch('{}', '{}', {}, {})".format(self.first, self.last, self.year, self.branch)


class Teacher(Student):

    def __init__(self, first, last, year, students=None):
        super().__init__(first, last, year)
        if students is None:
            self.students = []
        else:
            self.students = students

    def add_stud(self,stu):
        if stu not in self.students:
            self.students.append(stu)

    def rem_stud(self,stu):
        if stu in self.students:
            self.students.remove(stu)

    def print_studs(self):
        for stu in self.students:
            print('->', stu.fullname())

    def __repr__(self):
        return "Teacher('{}', '{}', {})".format(self.first, self.last, self.year)



st_1 = Branch('Abhilash', 'Prakash', 4, 'IS')
st_2 = Branch('Test', 'Student', 3, 'IS')

teach_1 = Teacher('Steve', 'Jones', 4, [st_1])

teach_1.add_stud(st_2)
print(teach_1.fullname())
teach_1.print_studs()
print(teach_1)
print(st_1)





