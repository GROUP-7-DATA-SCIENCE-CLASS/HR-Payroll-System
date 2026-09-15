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

==================================================
             WEEKLY EMPLOYEE PAYSLIP
==================================================

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

==================================================
"""
    return payslip

# ---------------------------------------------
    
# String Representation
# ---------------------------------------------
def _str_(self):
    return (f"{self.employee_number} | "
        f"{self.name} | "
        f"Net Pay: UGX {self.calculate_net_pay():,.0f}")





