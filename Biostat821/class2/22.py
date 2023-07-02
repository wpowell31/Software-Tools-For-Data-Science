class Person:
    def __init__(self, name: str, height: float):
        self.name = name
        self.height = height


class Student(Person):
    def __init__(self, name: str, height: float, school: str):
        super().__init__(name, height)
        self.school = school


if __name__ == "main":
    s = Student("Bob", 5.8, "Duke")
    print(s.name)
    # Studen.school = "UNC"
    print(s.school)
    #print(Student.school)