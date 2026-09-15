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

