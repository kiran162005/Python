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

