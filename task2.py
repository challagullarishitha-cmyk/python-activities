
# Progressive Electricity Billing System

monthly_bills = []

n = int(input("Enter number of months: "))

for i in range(n):
    print("\nMonth", i + 1)

    month = input("Enter month name: ")
    units = float(input("Enter electricity units consumed: "))

    # Progressive slab calculation
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + (units - 100) * 3
    elif units <= 300:
        bill = (100 * 2) + (100 * 3) + (units - 200) * 5
    else:
        bill = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    # Fixed charge
    fixed_charge = 50

    # Surcharge
    surcharge = bill * 0.05

    # Rebate for low consumption
    if units <= 100:
        rebate = bill * 0.10
    else:
        rebate = 0

    # Final bill
    total_bill = bill + fixed_charge + surcharge - rebate

    monthly_bills.append({
        "month": month,
        "units": units,
        "bill": total_bill
    })

    print("Energy Charge:", round(bill, 2))
    print("Fixed Charge:", fixed_charge)
    print("Surcharge:", round(surcharge, 2))
    print("Rebate:", round(rebate, 2))
    print("Total Bill:", round(total_bill, 2))


# Compare monthly bills
print("\n========== MONTHLY BILL COMPARISON ==========")

for i in range(len(monthly_bills)):
    print(
        monthly_bills[i]["month"],
        "- Units:", monthly_bills[i]["units"],
        "- Bill: Rs.",
        round(monthly_bills[i]["bill"], 2)
    )

# Identify unusual increases
print("\n========== UNUSUAL BILL INCREASES ==========")

found = False

for i in range(1, len(monthly_bills)):
    previous = monthly_bills[i - 1]["bill"]
    current = monthly_bills[i]["bill"]

    if previous > 0:
        increase = ((current - previous) / previous) * 100

        if increase > 30:
            print(
                "Warning:", monthly_bills[i]["month"],
                "bill increased by",
                round(increase, 2), "%"
            )
            found = True

if not found:
    print("No unusual bill increases found.")
