# class variables = Shared among all instances of a class
# Defined outside the constructur
# Allow you to share the data among all objects created from that class

class Student:

    class_year = 2026
    num_students = 0


    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Sandy", 32)
student4 = Student("Alice", 27)


# print(student1.name, student1.age)
# print(student2.name, student2.age)
# print(Student.class_year)

# print(Student.num_students)


