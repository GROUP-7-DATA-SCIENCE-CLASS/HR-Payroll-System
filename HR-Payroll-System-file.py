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

