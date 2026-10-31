
# Hospital Billing and Patient Classification System

print("===== HOSPITAL BILLING SYSTEM =====")

name = input("Enter patient name: ")
patient_id = input("Enter patient ID: ")

age = int(input("Enter patient age: "))

consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

paid_amount = float(input("Enter amount paid: "))

# Validate billing constraints
if (age <= 0 or consultation < 0 or
    diagnostic < 0 or treatment < 0 or paid_amount < 0):
    print("\nInvalid billing details!")

else:
    # Calculate total charges
    total = consultation + diagnostic + treatment

    # Apply conditional concessions
    concession = 0

    if age >= 60:
        concession = total * 0.20
        print("\nSenior citizen concession: 20%")

    elif total >= 10000:
        concession = total * 0.10
        print("\nHigh bill concession: 10%")

    else:
        print("\nNo concession applicable")

    # Final bill calculation
    final_bill = total - concession

    # Payment validation
    if paid_amount > final_bill:
        print("\nPayment exceeds final bill!")
    else:
        balance = final_bill - paid_amount

        # Patient classification
        if balance == 0:
            status = "Fully Paid"
        elif paid_amount > 0:
            status = "Partially Paid"
        else:
            status = "Unpaid"

        # Display bill
        print("\n========== PATIENT BILL ==========")
        print("Patient Name:", name)
        print("Patient ID:", patient_id)
        print("Age:", age)

        print("\nConsultation Charges: Rs.", consultation)
        print("Diagnostic Charges: Rs.", diagnostic)
        print("Treatment Charges: Rs.", treatment)

        print("Total Charges: Rs.", total)
        print("Concession: Rs.", concession)
        print("Final Bill: Rs.", final_bill)
        print("Amount Paid: Rs.", paid_amount)
        print("Remaining Balance: Rs.", balance)

        print("\nPatient Payment Classification:", status)

        if balance > 0:
            print("Please pay the remaining amount.")
        else:
            print("Payment completed successfully!")
