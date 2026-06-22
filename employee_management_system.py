
# ---------------- Person ----------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Person created with Name : {self.name} \t Age : {self.age}")

    def display(self):
        print(f"Person Name : {self.name}")
        print(f"Person Age  : {self.age}")

    def __del__(self):
        print(f"Person deleted {self.name}")


# ---------------- Employee ----------------
class Employee(Person):
    def __init__(self, emp_id, name, age, salary):
        super().__init__(name, age)
        self._emp_id = emp_id        # protected (fixed)
        self._salary = salary

    def get_employee_id(self):
        return self._emp_id

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary

    def show(self):
        print(
            f"Employee created with ID : {self._emp_id}, "
            f"Name : {self.name}, Age : {self.age}, Salary : {self._salary}"
        )

    def display(self):
        print(f"Employee ID : {self._emp_id}")
        super().display()
        print(f"Salary : {self._salary}")


# ---------------- Manager ----------------
class Manager(Employee):
    def __init__(self, emp_id, name, age, salary, department):
        super().__init__(emp_id, name, age, salary)
        self.department = department

    def show(self):
        print(
            f"Manager created with ID : {self._emp_id}, "
            f"Name : {self.name}, Age : {self.age}, "
            f"Salary : {self._salary}, Department : {self.department}"
        )

    def display(self):
        super().display()
        print(f"Department : {self.department}")


# ---------------- Developer ----------------
class Developer(Employee):
    def __init__(self, emp_id, name, age, salary, language):
        super().__init__(emp_id, name, age, salary)
        self.language = language

    def show(self):
        print(
            f"Developer created with ID : {self._emp_id}, "
            f"Name : {self.name}, Age : {self.age}, "
            f"Salary : {self._salary}, Language : {self.language}"
        )

    def display(self):
        super().display()
        print(f"Programming Language : {self.language}")


# ---------------- Lists ----------------
person = []
employee = []
manager = []
developer = []


# ---------------- Main ----------------
def main():
    print("\n--- Employee Management System ---\n")

    while True:
        print("\n1.Person  2.Employee  3.Manager  4.Developer  5.Show  6.Exit")
        choice = int(input("Enter choice : "))

        # Person
        if choice == 1:
            p = Person(input("Name : "), int(input("Age : ")))
            person.append(p)
            p.show()

        # Employee
        elif choice == 2:
            emp_id = int(input("Employee ID : "))
            if all(e.get_employee_id() != emp_id for e in employee):
                e = Employee(emp_id, input("Name : "), int(input("Age : ")), int(input("Salary : ")))
                employee.append(e)
                e.show()
            else:
                print("Employee ID already exists!")

        # Manager
        elif choice == 3:
            emp_id = int(input("Manager ID : "))
            if all(m.get_employee_id() != emp_id for m in manager):
                m = Manager(
                    emp_id,
                    input("Name : "),
                    int(input("Age : ")),
                    int(input("Salary : ")),
                    input("Department : ")
                )
                manager.append(m)
                m.show()
            else:
                print("Manager ID already exists!")

        # Developer
        elif choice == 4:
            emp_id = int(input("Developer ID : "))
            if all(d.get_employee_id() != emp_id for d in developer):
                d = Developer(
                    emp_id,
                    input("Name : "),
                    int(input("Age : ")),
                    int(input("Salary : ")),
                    input("Language : ")
                )
                developer.append(d)
                d.show()
            else:
                print("Developer ID already exists!")

        # Show
        elif choice == 5:
            print("\n--- SHOW DATA ---")
            print("\nPersons:")
            for p in person:
                p.display()

            print("\nEmployees:")
            for e in employee:
                e.display()

            print("\nManagers:")
            for m in manager:
                m.display()

            print("\nDevelopers:")
            for d in developer:
                d.display()

        # Exit
        elif choice == 6:
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


main()
