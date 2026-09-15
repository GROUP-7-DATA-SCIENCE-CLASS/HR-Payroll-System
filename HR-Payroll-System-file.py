# ---------------------------------------------
# Gross Pay
# ---------------------------------------------
def calculate_gross_pay(self):
    return self.calculate_regular_pay() + self.calculate_overtime_pay()