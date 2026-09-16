"""
CSC2105: Object-Oriented Programming Using Python
Topic 5 Group Project – HR / Payroll System

Group 6 Members
1. Timothy Mugisha - S25B38/041
2.  Ndambire Harry Bosco - M25B38/030
3. Mutagamba Jasmine Martha - S25B38/28
4. Natuyamba Conrad - S25B38/027
5. Musiime Miracle Ephraim - M25B38/012
6. Tana Micheal Wasolo - M25B38/035
"""
# =====================================================
# CONSTANTS
# =====================================================

REGULAR_HOURS = 40
OVERTIME_RATE_MULTIPLIER = 1.5
TAX_THRESHOLD = 100000
TAX_RATE = 0.10

# =======================================================
# EMPLOYEE CLASS
# =====================================================

class Employee:
    """
    Represents one employee in the payroll system.
    Stores employee information and performs salary calculations.
    """

    def __init__(self, name, employee_number, hours_worked, hourly_rate):
        self.name = name
        self.employee_number = employee_number
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

        # Validate immediately when object is created.
        self.validate_inputs()

# ---------------------------------------------
# Validation Method
# ---------------------------------------------
    def validate_inputs(self):
            if not self.name.strip():
                raise ValueError("Employee name cannot be empty.")

            if self.hours_worked < 0:
                raise ValueError("Hours worked cannot be negative.")

            if self.hourly_rate <= 0:
                raise ValueError("Hourly rate must be greater than zero.")

# ---------------------------------------------
# Regular Pay
# ---------------------------------------------
    def calculate_regular_pay(self):
            regular_hours = min(self.hours_worked, REGULAR_HOURS)
            return regular_hours * self.hourly_rate
      
# ---------------------------------------------
# Overtime Hours
# ---------------------------------------------
    def calculate_overtime_hours(self):
            return max(0, self.hours_worked - REGULAR_HOURS)

# ---------------------------------------------
# Overtime Pay
# ---------------------------------------------
    def calculate_overtime_pay(self):
            overtime_hours = self.calculate_overtime_hours()
            overtime_rate = self.hourly_rate * OVERTIME_RATE_MULTIPLIER
            return overtime_hours * overtime_rate
      
      
# ---------------------------------------------
# Gross Pay
# ---------------------------------------------
def calculate_gross_pay(self):
    return self.calculate_regular_pay() + self.calculate_overtime_pay()

# ---------------------------------------------
# Tax
# ---------------------------------------------
def calculate_tax(self):
    gross_pay = self.calculate_gross_pay()

    if gross_pay <= TAX_THRESHOLD:
        return 0

    taxable_amount = gross_pay - TAX_THRESHOLD
    return taxable_amount * TAX_RATE

# ---------------------------------------------
# Net Pay
# ---------------------------------------------
def calculate_net_pay(self):
    return self.calculate_gross_pay() - self.calculate_tax()

# ---------------------------------------------
# Payslip Generator
# ---------------------------------------------
def generate_payslip(self):
    gross = self.calculate_gross_pay()
    tax = self.calculate_tax()
    net = self.calculate_net_pay()

    payslip = f"""

             WEEKLY EMPLOYEE PAYSLIP

Employee Name    : {self.name}
Employee Number  : {self.employee_number}

Hours Worked     : {self.hours_worked}
Hourly Rate      : UGX {self.hourly_rate:,.0f}

Regular Pay      : UGX {self.calculate_regular_pay():,.0f}
Overtime Hours   : {self.calculate_overtime_hours()}
Overtime Pay     : UGX {self.calculate_overtime_pay():,.0f}

Gross Pay        : UGX {gross:,.0f}
Tax Deducted     : UGX {tax:,.0f}

NET PAY          : UGX {net:,.0f}

"""
    return payslip

# ---------------------------------------------
    
# String Representation
# ---------------------------------------------
def _str_(self):
    return (f"{self.employee_number} | "
        f"{self.name} | "
        f"Net Pay: UGX {self.calculate_net_pay():,.0f}")



