class Employee:
    def __init__(self, eno, ename, edesig, esalary):
        self.eno = eno
        self.ename = ename
        self.edesig = edesig
        self.esalary = esalary
        
class EmployeeManagement:
    def __init__(self):
        self.employees = {}

    def add_employee(self):
        try:
            eno = int(input("Enter Employee Number: "))
            if eno in self.employees:
                print("Employee number already exists.")
                return

            ename = input("Enter Employee Name: ")
            edesig = input("Enter Employee Designation: ")
            esalary = float(input("Enter Employee Salary: "))

            self.employees[eno] = Employee(eno, ename, edesig, esalary)
            print("Employee added successfully!")
        except ValueError:
            print("Invalid input. Please try again.")

    def get_employee_by_eno(self):
        try:
            eno = int(input("Enter Employee Number: "))
            if eno in self.employees:
                emp = self.employees[eno]
                print(f"\nEmployee Details:\nEno: {emp.eno}\nEname: {emp.ename}\nEdesig: {emp.edesig}\nEsalary: {emp.esalary}")
            else:
                print("Employee not found.")
        except ValueError:
            print("Invalid input. Please try again.")

    def display_all_employees(self):
        if not self.employees:
            print("No employees to display.")
            return

        print("\nAll Employee Details:")
        for emp in self.employees.values():
            print(f"Eno: {emp.eno}, Ename: {emp.ename}, Edesig: {emp.edesig}, Esalary: {emp.esalary}")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Add Employee")
            print("2. Get Employee by Eno")
            print("3. Display All Employees")
            print("4. Exit")

            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.add_employee()
                elif choice == 2:
                    self.get_employee_by_eno()
                elif choice == 3:
                    self.display_all_employees()
                elif choice == 4:
                    print("Exiting program. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
    
emp_mgmt = EmployeeManagement()
emp_mgmt.menu()