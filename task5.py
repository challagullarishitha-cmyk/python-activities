
# Multi-Plan Telecommunications Cost Optimization

print("===== MOBILE PLAN OPTIMIZATION SYSTEM =====")

# Customer requirements
data_needed = float(input("Enter required data (GB): "))
calls_needed = int(input("Enter required call minutes: "))
sms_needed = int(input("Enter required SMS: "))
validity_needed = int(input("Enter required validity (days): "))
budget = float(input("Enter your budget (Rs): "))

# Number of plans
n = int(input("\nEnter number of mobile plans: "))

plans = []

for i in range(n):
    print("\nEnter details for Plan", i + 1)

    name = input("Enter plan name: ")
    price = float(input("Enter plan price: "))
    data = float(input("Enter data limit (GB): "))
    calls = int(input("Enter call minutes: "))
    sms = int(input("Enter SMS limit: "))
    validity = int(input("Enter validity days: "))

    extra_data_rate = float(input("Extra data charge per GB: "))
    extra_call_rate = float(input("Extra call charge per minute: "))
    extra_sms_rate = float(input("Extra SMS charge: "))

    # Validate plan details
    if (price < 0 or data < 0 or calls < 0 or
        sms < 0 or validity <= 0 or
        extra_data_rate < 0 or
        extra_call_rate < 0 or extra_sms_rate < 0):

        print("Invalid plan details!")
        continue

    # Calculate excess charges
    extra_data = max(0, data_needed - data)
    extra_calls = max(0, calls_needed - calls)
    extra_sms = max(0, sms_needed - sms)

    excess_charge = (
        extra_data * extra_data_rate +
        extra_calls * extra_call_rate +
        extra_sms * extra_sms_rate
    )

    total_cost = price + excess_charge

    # Check eligibility
    if (validity >= validity_needed and
        total_cost <= budget):

        plans.append({
            "name": name,
            "price": price,
            "excess": excess_charge,
            "total": total_cost,
            "validity": validity
        })

# Find the most economical plan
print("\n===== PLAN COMPARISON RESULTS =====")

if len(plans) == 0:
    print("No eligible plans found within your budget.")

else:
    plans.sort(key=lambda x: (x["total"], x["price"]))

    for i, plan in enumerate(plans, start=1):
        print("\nPlan Ranking:", i)
        print("Plan Name:", plan["name"])
        print("Base Price: Rs.", round(plan["price"], 2))
        print("Excess Charges: Rs.", round(plan["excess"], 2))
        print("Total Cost: Rs.", round(plan["total"], 2))
        print("Validity:", plan["validity"], "days")

    print("\n===== BEST PLAN =====")
    best = plans[0]

    print("Most Economical Plan:", best["name"])
    print("Total Cost: Rs.", round(best["total"], 2))
    print("You save by selecting this plan!")

