# CSC2105 OBJECT-ORIENTED PROGRAMMING USING PYTHON
## Group Project Report

### HR / Payroll System (Group 6)

**Uganda Christian University**

**Faculty of Engineering**

**Department of Computing and Technology**

**Course Unit:** CSC2105 – Object-Oriented Programming Using Python

**Academic Class:** BSDS 2:1

**Group Number:** 6

### Group Members

1. Mugisha Timothy
2. Natuyamba Conrad
3. Mutagamba Jasmine Martha
4. Tana Wasolo
5. Miracle Musiime
6. Harry Ndambiire
---

# Table of Contents

1. Introduction
2. Problem Statement
3. Project Objectives
4. Requirements Analysis
5. Object-Oriented System Design
6. Payroll Algorithms and Calculations
7. Exception Handling and Validation
8. Program Demonstration and Testing
9. GitHub Collaboration Workflow
10. Challenges Encountered
11. Future Improvements
12. Conclusion

---

# 1. Introduction

The Human Resource (HR) Payroll System is a Python application developed as a group project for CSC2105: Object-Oriented Programming Using Python. The project models a real-world payroll scenario using Object-Oriented Programming principles, where employees are represented as objects with their own data and behaviours.

The system calculates weekly salaries for employees based on the number of hours worked and the hourly rate of pay. It also supports overtime calculations, tax deductions, net salary computation, payslip generation, and validation of invalid employee records.

The design follows the assignment requirement of modelling a real-world scenario using classes and objects while leaving room for future expansion into encapsulation, inheritance, polymorphism, persistence, and exception handling.

---

# 2. Problem Statement

A small organisation requires software to calculate the weekly salaries of its employees.

Each employee has:

- Employee name.
- Employee number.
- Weekly hours worked.
- Hourly rate of pay.

The payroll system must:

- Calculate gross pay.
- Pay overtime at 1.5 times the hourly rate for hours above 40.
- Deduct tax according to the assignment rules.
- Calculate net pay.
- Produce a payslip.
- Reject invalid employee information.

---

# 3. Project Objectives

The objectives of this project are to:

- Apply Object-Oriented Programming concepts in Python.
- Represent employees as objects.
- Implement constructors and instance methods.
- Calculate weekly salaries using payroll formulas.
- Handle invalid input using Python exceptions.
- Generate readable payslip summaries for employees.
- Demonstrate interaction between multiple objects through a payroll management class.

---

# 4. Requirements Analysis

## Functional Requirements

The system should be able to:

- Register employees.
- Store employee information.
- Calculate regular pay.
- Calculate overtime pay.
- Calculate gross pay.
- Calculate tax deductions.
- Calculate net pay.
- Search employees.
- Display payslips.
- Display a weekly payroll summary.

## Non-Functional Requirements

The system should:

- Be easy to understand.
- Use Object-Oriented Programming principles.
- Be modular and reusable.
- Validate invalid input.
- Produce clear terminal output.

---

# 5. Object-Oriented System Design

The payroll system is designed using two classes.

## Employee Class

The Employee class represents one employee in the organisation.

### Attributes

| Attribute | Purpose |
|-----------|---------|
| name | Stores employee's full name. |
| employee_number | Stores a unique employee ID. |
| hours_worked | Stores weekly working hours. |
| hourly_rate | Stores hourly payment rate. |

### Methods

| Method | Responsibility |
|--------|----------------|
| validate_inputs() | Validates employee information. |
| calculate_regular_pay() | Calculates pay for up to 40 hours. |
| calculate_overtime_hours() | Calculates overtime hours worked. |
| calculate_overtime_pay() | Calculates overtime payment. |
| calculate_gross_pay() | Calculates total weekly earnings. |
| calculate_tax() | Calculates tax deductions. |
| calculate_net_pay() | Calculates take-home pay. |
| generate_payslip() | Generates formatted payslip output. |
| __str__() | Returns a readable employee summary. |

## PayrollSystem Class

The PayrollSystem class manages multiple Employee objects.

### Attributes

- employees — stores all employee objects in a list.

### Methods

| Method | Responsibility |
|--------|----------------|
| add_employee() | Adds an employee to the payroll. |
| find_employee() | Searches an employee by ID. |
| display_all_payslips() | Displays every employee's payslip. |
| weekly_summary() | Calculates organisation payroll totals. |

## Relationship Between Classes

The PayrollSystem class contains multiple Employee objects. This demonstrates aggregation, where one object manages a collection of other objects.

---

# 6. Payroll Algorithms and Calculations

The payroll calculations follow the assignment specification.

## Step 1 — Regular Pay

Regular hours are limited to 40.

**Formula**

Regular Hours = Minimum(Hours Worked, 40)

Regular Pay = Regular Hours × Hourly Rate

## Step 2 — Overtime Pay

Hours above 40 are overtime.

**Formula**

Overtime Hours = Hours Worked − 40

Overtime Rate = Hourly Rate × 1.5

Overtime Pay = Overtime Hours × Overtime Rate

## Step 3 — Gross Pay

Gross Pay = Regular Pay + Overtime Pay

## Step 4 — Tax Deduction

Tax rules implemented:

- First UGX 100,000 is tax free.
- 10% tax applies to income above UGX 100,000.

**Formula**

Taxable Amount = Gross Pay − 100,000

Tax = Taxable Amount × 10%

## Step 5 — Net Pay

Net Pay = Gross Pay − Tax

## Example Calculation

**Employee:** Sarah Nakato

| Item | Value |
|------|------:|
| Hours Worked | 47 |
| Hourly Rate | UGX 8,000 |
| Regular Pay | UGX 320,000 |
| Overtime Hours | 7 |
| Overtime Pay | UGX 84,000 |
| Gross Pay | UGX 404,000 |
| Tax | UGX 30,400 |
| Net Pay | UGX 373,600 |

---

# 7. Exception Handling and Validation

The project uses Python exceptions to prevent invalid payroll records.

## Validation Rules

| Invalid Input | System Response |
|---------------|----------------|
| Empty employee name | Raises ValueError. |
| Negative hours worked | Raises ValueError. |
| Hourly rate less than or equal to zero | Raises ValueError. |
| Duplicate employee number | Raises ValueError. |

## Why Exception Handling Was Used

Exception handling prevents incorrect payroll calculations and ensures only valid employees are added to the payroll system. The demonstration uses `try` and `except` blocks to catch errors without terminating the entire program.

---

# 8. Program Demonstration and Testing

The program demonstrates both successful and unsuccessful operations.

## Successful Operations

- Employee with no overtime.
- Employee with overtime.
- Employee search by employee number.
- Displaying individual payslips.
- Displaying all payslips.
- Weekly payroll summary.

## Invalid Operations

| Test Case | Expected Behaviour |
|-----------|--------------------|
| Negative hours worked | Employee creation rejected. |
| Negative hourly rate | Employee creation rejected. |
| Duplicate employee number | Employee not added. |

These tests confirm that the system behaves correctly under both normal and invalid conditions.

---

# 9. GitHub Collaboration Workflow

The project was developed collaboratively using GitHub.

## Workflow Used

1. Create shared GitHub repository.
2. Clone repository to local machines.
3. Create feature branches.
4. Commit changes with descriptive commit messages.
5. Push branches to GitHub.
6. Create Pull Requests.
7. Review and merge into the `main` branch.

## Benefits of GitHub Collaboration

- Every member contributed independently.
- Changes were reviewed before merging.
- Version history was maintained.
- Conflicts were resolved through Pull Requests.

---

# 10. Challenges Encountered

During development, the group identified several challenges.

- Setting up Git for members who had never used GitHub before.
- Understanding how constructors initialize objects.
- Preventing duplicate employee numbers.
- Implementing overtime calculations correctly.
- Formatting terminal output into a readable payslip.
- Testing invalid inputs using exception handling.

These challenges improved the group's understanding of collaborative software development and Object-Oriented Programming.

---

# 11. Future Improvements

The current project satisfies Topic 5 requirements but is designed for future expansion.

Possible improvements include:

- Using encapsulation with private attributes and getters/setters.
- Creating subclasses such as FullTimeEmployee and PartTimeEmployee through inheritance.
- Using polymorphism for different salary calculation strategies.
- Saving employee records in a database or file.
- Developing a graphical user interface using Tkinter or a web framework.
- Adding employee departments, allowances, deductions, and NSSF calculations.

---

# 12. Conclusion

The HR / Payroll System successfully models a real-world payroll application using Object-Oriented Programming in Python. The project demonstrates the use of classes, objects, constructors, methods, exception handling, and aggregation while meeting the functional requirements provided in the assignment.

The system calculates weekly salaries accurately, handles overtime and tax deductions, rejects invalid employee records, generates payslips, and provides a payroll summary for the organisation. The project also demonstrates collaborative software development through GitHub, making it scalable for future Object-Oriented Programming topics.
