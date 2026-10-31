
# Manufacturing Cost and Profitability Analysis

print("===== MANUFACTURING COST ANALYSIS =====")

# Product details
product = input("Enter product name: ")

quantity = int(input("Enter number of units produced: "))

material_cost = float(input("Enter raw material cost per unit: "))
labour_cost = float(input("Enter labour charge per unit: "))
machine_cost = float(input("Enter machine cost per unit: "))

wastage_percent = float(input("Enter wastage percentage: "))

selling_price = float(input("Enter selling price per unit: "))

profit_target = float(input("Enter required profit percentage: "))

# Input validation
if (quantity <= 0 or material_cost < 0 or
    labour_cost < 0 or machine_cost < 0 or
    wastage_percent < 0 or wastage_percent > 100 or
    selling_price < 0 or profit_target < 0):

    print("\nInvalid production details!")

else:

    # Material cost calculation
    total_material = material_cost * quantity

    # Wastage cost
    wastage_cost = total_material * wastage_percent / 100

    # Labour cost
    total_labour = labour_cost * quantity

    # Machine cost
    total_machine = machine_cost * quantity

    # Total production cost
    total_cost = (
        total_material + wastage_cost +
        total_labour + total_machine
    )

    # Cost per unit
    cost_per_unit = total_cost / quantity

    # Total sales revenue
    total_revenue = selling_price * quantity

    # Profit or loss
    profit = total_revenue - total_cost

    # Profit percentage
    if total_cost > 0:
        profit_percent = (profit / total_cost) * 100
    else:
        profit_percent = 0

    # Profit target calculation
    target_profit = total_cost * profit_target / 100

    # Display production report
    print("\n========== PRODUCTION REPORT ==========")

    print("Product Name:", product)
    print("Quantity Produced:", quantity)

    print("\n----- COST DETAILS -----")

    print("Material Cost: Rs.", round(total_material, 2))
    print("Wastage Cost: Rs.", round(wastage_cost, 2))
    print("Labour Cost: Rs.", round(total_labour, 2))
    print("Machine Cost: Rs.", round(total_machine, 2))

    print("--------------------------------------")

    print("Total Production Cost: Rs.", round(total_cost, 2))
    print("Production Cost Per Unit: Rs.", round(cost_per_unit, 2))

    print("\n----- PROFIT ANALYSIS -----")

    print("Selling Price Per Unit: Rs.", selling_price)
    print("Total Sales Revenue: Rs.", round(total_revenue, 2))
    print("Profit / Loss: Rs.", round(profit, 2))
    print("Profit Percentage:", round(profit_percent, 2), "%")

    print("Required Profit: Rs.", round(target_profit, 2))

    print("\n----- FINAL RESULT -----")

    if profit >= target_profit:
        print("PRODUCTION MEETS THE PROFIT TARGET!")
    else:
        print("PRODUCTION DOES NOT MEET THE PROFIT TARGET.")

        shortfall = target_profit - profit
        print("Profit Shortfall: Rs.", round(shortfall, 2))

