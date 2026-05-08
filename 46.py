# Multiple inheritance = inherit from more than one parent class 
#                        C(A,B)
# multilevel inheritance = inherit from a parent which inherits from another parent 
#                           C(B) <- B(A) <- A

class Animal:

    def __init__(self, name):
        self.name = name
