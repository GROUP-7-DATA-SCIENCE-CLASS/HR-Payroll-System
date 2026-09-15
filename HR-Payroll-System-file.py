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