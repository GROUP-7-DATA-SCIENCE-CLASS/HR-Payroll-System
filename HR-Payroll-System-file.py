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
