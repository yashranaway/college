# Inheritance
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def get_salary(self):
        return self.salary

    def display_info(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Salary: ${self.salary}"

    def apply_raise(self, percentage):
        self.salary += int(self.salary * percentage / 100)


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.subordinates = []

    def add_subordinate(self, employee):
        if isinstance(employee, Employee) and employee not in self.subordinates:
            self.subordinates.append(employee)

    def remove_subordinate(self, employee):
        if employee in self.subordinates:
            self.subordinates.remove(employee)

    def list_subordinates(self):
        return [emp.name for emp in self.subordinates]

    def display_info(self):
        return f"{super().display_info()}, Department: {self.department}, Subordinates: {len(self.subordinates)}"


class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def code(self):
        return f"{self.name} is coding in {self.programming_language}"

    def display_info(self):
        return f"{super().display_info()}, Language: {self.programming_language}"


# Create instances
emp1 = Employee("John Doe", "E001", 50000)
manager1 = Manager("Jane Smith", "M001", 80000, "IT")
dev1 = Developer("Alice Johnson", "D001", 65000, "Python")
dev2 = Developer("Bob Williams", "D002", 67000, "Java")

# Demonstrate inheritance and polymorphism
employees = [emp1, manager1, dev1, dev2]
for emp in employees:
    print(emp.display_info())

# Use specific methods
manager1.add_subordinate(dev1)
manager1.add_subordinate(dev2)
print(f"\nManager's subordinates: {manager1.list_subordinates()}")

print(dev1.code())
print(dev2.code())

# Apply raise
emp1.apply_raise(5)
print(f"\nAfter 5% raise: {emp1.display_info()}")

# Demonstrate isinstance
print(f"\nIs dev1 an instance of Employee? {isinstance(dev1, Employee)}")
print(f"Is manager1 an instance of Developer? {isinstance(manager1, Developer)}")
