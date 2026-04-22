class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)

# Creating object
e1 = Employee("Ram", 26, 6000)
e1.show()