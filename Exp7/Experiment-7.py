# classobj
class university:
    def issue(self):
        student_name = input("Enter student name: ")
        student_marks = input("Enter marks: ")
        print("student", student_name, "scored", student_marks, "in her python exam")

obj = university()
obj.issue()

# Inheritance
class Animal:
    def speak(self):
        print("The animal makes sound")

class Dog(Animal):
    def speak(self):
        print("The Dog barks: woof! woof!")

class Cat(Animal):
    def speak(self):
        print("The cat meows: meow! meow!")

C = Cat()
D = Dog()
A = Animal()

C.speak()
D.speak()
A.speak()

# polymorphism

class Kingdom:
    def speak (self):
        print ("The animal makes sound ")
class Dog (Kingdom):
    def speak (self):
        super().speak()
        print(" the Dog barks! woof !")
D = Dog()
D.speak()