# =====================================================
# PAYROLL SYSTEM CLASS
# =====================================================

class PayrollSystem:
    """
    Stores and manages multiple employees.
    """

    def _init_(self):
        self.employees = []
# ---------------------------------------------
    # Add Employee
    # ---------------------------------------------
    def add_employee(self, employee):

        # Check duplicate employee number
        for emp in self.employees:
            if emp.employee_number == employee.employee_number:
                raise ValueError(
                    f"Employee number {employee.employee_number} already exists."
                )

        self.employees.append(employee)
        print(f"Employee '{employee.name}' added successfully.")
