
# University Scholarship Allocation System

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    m1 = float(input("Enter subject 1 marks: "))
    m2 = float(input("Enter subject 2 marks: "))
    m3 = float(input("Enter subject 3 marks: "))

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter family annual income: "))

    total = m1 + m2 + m3
    aggregate = total / 3

    # Eligibility conditions
    if (aggregate >= 75 and
        m1 >= 50 and m2 >= 50 and m3 >= 50 and
        attendance >= 75 and income <= 250000):

        students.append({
            "name": name,
            "roll": roll_no,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

    else:
        print(name, "is NOT eligible for scholarship")

# Ranking eligible students
students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"]
    )
)

# Display results
print("\n========== SCHOLARSHIP RESULTS ==========")

if len(students) == 0:
    print("No eligible students found.")

else:
    print("\nEligible Students Ranking:")

    for rank, student in enumerate(students, start=1):
        print("\nRank:", rank)
        print("Name:", student["name"])
        print("Roll Number:", student["roll"])
        print("Aggregate Marks:", round(student["aggregate"], 2))
        print("Attendance:", student["attendance"], "%")
        print("Family Income:", student["income"])

    print("\nTotal Eligible Students:", len(students))
