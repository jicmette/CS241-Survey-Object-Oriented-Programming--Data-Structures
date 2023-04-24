from abc import ABC
from abc import abstractmethod

class Employee():

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

    @abstractmethod
    def get_paycheck():
        return 0.00

class HourlyEmployee(Employee):

    def __init__(self, name, wage, hours):
        super().__init__(name)
        self.hourly_wage = wage
        self.hours = hours

    def display(self):
        print("{} - ${:.2f}/hour - Pay Check Amount: ${:.2f}".format(self.name, self.hourly_wage, self.get_paycheck()))

    def get_paycheck(self):
        return self.hours * self.hourly_wage

class SalaryEmployee(Employee):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display(self):
        print("{} / ${:.2f}/year - Pay Check Amount: ${:.2f}".format(self.name, self.salary, self.get_paycheck()))

    def get_paycheck(self):
        return self.salary / 24

def main():

    employees = []

    command = ""

    while command != "q":
        command = input("Enter 'h' (hourly employee), 's', (salary employee) or 'q': ")

        if command == "h":
            name = input("Enter name: ")
            wage = float(input("Enter wage: "))
            hours = int(input("Enter hours: "))
            emp1 = HourlyEmployee(name, wage, hours)
            employees.append(emp1)

        if command == "s":
            name = input("Enter name: ")
            salary = float(input("Enter salary: "))
            emp1 = SalaryEmployee(name, salary)
            employees.append(emp1)

    for employee in employees:
        employee.display()
        

if __name__ == "__main__":
    main()
