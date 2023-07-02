"""Run notes for class."""


class Class:
    """University class, i.e. an instance of a course."""

    def __init__(self, students):
        """Initialize."""
        self.__students = students
        self.annotations: dict[str, str] = dict()

    @property
    def students(self):
        """Get students."""
        return self.__students

    @students.setter
    def students(self, value):
        raise RuntimeError("Thou shall not do this. Try using add_students()")
        self.__students = value

    def add_student(self, student: str):
        """Add one student."""
        self.__students.append(student)

    def add_students(self, *students: str, front: bool = False) -> None:
        """Add multiple students."""
        if front:
            self.__students = list(students) + self.__students
        else:
            for student in students:
                self.add_student(student)

    def add_annotations(self, **kwargs) -> None:

        for key, value in kwargs.items():
            self.annotations[key] = value



if __name__ == '__main__':
    biostat821 = Class([])
    biostat821.add_student("Heather")
    #biostat821.__students.append("Bob")
    biostat821.add_students("Sam", front=True)
    biostat821.add_students("Eric", "Nick")
    assert biostat821.students == ["Sam", "Heather", "Eric", "Nick"]
    print(biostat821.students)
    biostat821.students = []
    print(biostat821.students)
    biostat821.add_annotations(hello="world", foo="bar")
    biostat821.add_annotations(patrick="Wang")
    print(biostat821.annotations)
