
# Employee Payroll and Deduction Analysis

print("===== EMPLOYEE PAYROLL SYSTEM =====")

# Employee details
name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

basic = float(input("Enter basic salary: "))
hra = float(input("Enter HRA allowance: "))
da = float(input("Enter DA allowance: "))
other = float(input("Enter other allowances: "))

overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: "))

incentive = float(input("Enter incentives: "))

# Input validation
if (basic < 0 or hra < 0 or da < 0 or other < 0
    or overtime_hours < 0 or overtime_rate < 0
    or incentive < 0):

    print("\nInvalid salary details!")

else:
    # Calculate overtime payment
    overtime_pay = overtime_hours * overtime_rate

    # Calculate gross salary
    gross_salary = (
        basic + hra + da + other +
        overtime_pay + incentive
    )

    # Progressive deductions
    if gross_salary <= 20000:
        deduction = gross_salary * 0.05

    elif gross_salary <= 40000:
        deduction = (20000 * 0.05) + (
            (gross_salary - 20000) * 0.10
        )

    else:
        deduction = (
            (20000 * 0.05) +
            (20000 * 0.10) +
            ((gross_salary - 40000) * 0.15)
        )

    # Net salary
    net_salary = gross_salary - deduction

    # Display salary statement
    print("\n========== SALARY STATEMENT ==========")

    print("Employee Name:", name)
    print("Employee ID:", emp_id)

    print("\n----- EARNINGS -----")
    print("Basic Salary: Rs.", basic)
    print("HRA Allowance: Rs.", hra)
    print("DA Allowance: Rs.", da)
    print("Other Allowances: Rs.", other)
    print("Overtime Payment: Rs.", overtime_pay)
    print("Incentives: Rs.", incentive)

    print("-------------------------------------")
    print("Gross Salary: Rs.", round(gross_salary, 2))

    print("\n----- DEDUCTIONS -----")
    print("Total Deduction: Rs.", round(deduction, 2))

    print("-------------------------------------")
    print("Net Salary: Rs.", round(net_salary, 2))

    print("\nSalary calculation completed!")
