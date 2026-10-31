
# Railway Fare and Reservation Calculator

print("===== RAILWAY RESERVATION SYSTEM =====")

passengers = []

n = int(input("Enter number of passengers: "))

for i in range(n):

    print("\nEnter details for Passenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))

    distance = float(input("Enter travel distance (KM): "))

    print("\nTravel Classes:")
    print("1. Sleeper")
    print("2. AC 3 Tier")
    print("3. AC 2 Tier")
    print("4. AC First Class")

    choice = int(input("Select travel class (1-4): "))

    # Class-wise fare per KM
    if choice == 1:
        travel_class = "Sleeper"
        rate = 1.0
        reservation_fee = 20

    elif choice == 2:
        travel_class = "AC 3 Tier"
        rate = 2.0
        reservation_fee = 40

    elif choice == 3:
        travel_class = "AC 2 Tier"
        rate = 3.0
        reservation_fee = 50

    elif choice == 4:
        travel_class = "AC First Class"
        rate = 4.0
        reservation_fee = 60

    else:
        print("Invalid class selection!")
        continue

    # Validate passenger details
    if age <= 0 or distance <= 0:
        print("Invalid passenger details!")
        continue

    # Distance-based fare slabs
    if distance <= 100:
        slab_charge = 0
    elif distance <= 300:
        slab_charge = 50
    elif distance <= 500:
        slab_charge = 100
    else:
        slab_charge = 200

    # Basic fare
    basic_fare = distance * rate + slab_charge

    # Age-based concession
    concession = 0

    if age < 5:
        concession = basic_fare
        print("Child concession: 100%")

    elif age >= 60:
        concession = basic_fare * 0.40
        print("Senior citizen concession: 40%")

    elif age <= 12:
        concession = basic_fare * 0.50
        print("Child concession: 50%")

    # Final fare
    final_fare = basic_fare - concession + reservation_fee

    passengers.append({
        "name": name,
        "age": age,
        "class": travel_class,
        "distance": distance,
        "basic": basic_fare,
        "concession": concession,
        "fee": reservation_fee,
        "fare": final_fare
    })


# Display passenger fare details
print("\n========== PASSENGER FARE DETAILS ==========")

total_amount = 0

for i, p in enumerate(passengers, start=1):

    print("\nPassenger:", i)
    print("Name:", p["name"])
    print("Age:", p["age"])
    print("Travel Class:", p["class"])
    print("Distance:", p["distance"], "KM")
    print("Basic Fare: Rs.", round(p["basic"], 2))
    print("Concession: Rs.", round(p["concession"], 2))
    print("Reservation Fee: Rs.", p["fee"])
    print("Final Fare: Rs.", round(p["fare"], 2))

    total_amount += p["fare"]

print("\nTotal Reservation Amount: Rs.",
      round(total_amount, 2))


# Cancellation calculation
if passengers:
    print("\n===== CANCELLATION DETAILS =====")

    cancel = input("Do you want to cancel tickets? (yes/no): ")

    if cancel.lower() == "yes":

        cancel_count = int(input(
            "Enter number of tickets to cancel: "
        ))

        if cancel_count < 1 or cancel_count > len(passengers):
            print("Invalid cancellation count!")

        else:
            penalty = 0
            refund = 0

            for i in range(cancel_count):
                p = passengers[i]

                # Cancellation penalty
                if p["fare"] <= 100:
                    charge = p["fare"] * 0.10
                elif p["fare"] <= 500:
                    charge = p["fare"] * 0.20
                else:
                    charge = p["fare"] * 0.30

                penalty += charge
                refund += p["fare"] - charge

            print("Total Cancellation Penalty: Rs.",
                  round(penalty, 2))
            print("Total Refund Amount: Rs.",
                  round(refund, 2))

    else:
        print("Tickets confirmed successfully!")
else:
    print("No valid passenger reservations found.")
