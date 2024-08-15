class College:
    def __init__(self, name, dept):
        self.Name = name
        self.Dept = dept


class Teacher(College):
    def __init__(self, name, dept, subj, salary):
        self.Subj = subj
        self.Salary = salary
        super().__init__(name, dept)

    def display(self):
        print("Name:", self.Name)
        print("Dept:", self.Dept)
        print("Subj", self.Subj)
        print("Salary:", self.Salary)


class Student(College):
    def __init__(self, name, dept):
        super().__init__(name, dept)

    def display(self):
        print("Name:", self.Name)
        print("Dept:", self.Dept)


class Principal(Teacher):
    def __init__(self, name, dept, subj, salary):
        super().__init__(name, dept, subj, salary)


class Peon(Principal, Student):
    def __init__(self, name, salary):
        self.Name = name
        self.Salary = salary

    def display(self):
        print("Name:", self.Name)
        print("Salary:", self.Salary)


Education = Teacher("Malar", "CSE", "English", 20000)
Education.display()

Education = Student("Kavya", "ECE")
Education.display()

Education = Principal("Narmatha", "EEE", "Electronics", 20000)
Education.display()

Education = Peon("Shree", 15000)
Education.display()
