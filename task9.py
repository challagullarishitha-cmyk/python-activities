
# Multi-Currency Travel Budget Analysis

print("===== TRAVEL BUDGET ANALYSIS SYSTEM =====")

base_currency = input("Enter base currency (example: INR): ").upper()

budget = float(input("Enter total travel budget: "))

fee_percent = float(input("Enter currency conversion fee (%): "))

n = int(input("Enter number of expense categories: "))

expenses = []
total_expense = 0

# Process multiple travel expenses
for i in range(n):

    print("\nEnter Expense Details", i + 1)

    category = input("Enter expense category: ")

    amount = float(input("Enter expense amount: "))

    currency = input("Enter currency code: ").upper()

    exchange_rate = float(
        input("Enter exchange rate to base currency: ")
    )

    # Input validation
    if amount < 0 or exchange_rate <= 0:
        print("Invalid expense details!")
        continue

    # Currency conversion
    converted_amount = amount * exchange_rate

    # Conversion fee
    conversion_fee = converted_amount * fee_percent / 100

    # Final expense
    final_amount = converted_amount + conversion_fee

    total_expense += final_amount

    expenses.append({
        "category": category,
        "currency": currency,
        "amount": amount,
        "converted": converted_amount,
        "fee": conversion_fee,
        "total": final_amount
    })


# Display expense report
print("\n========== TRAVEL EXPENSE REPORT ==========")

for expense in expenses:

    print("\nCategory:", expense["category"])
    print("Original Amount:", expense["amount"],
          expense["currency"])

    print("Converted Amount:", round(expense["converted"], 2),
          base_currency)

    print("Conversion Fee:", round(expense["fee"], 2),
          base_currency)

    print("Final Expense:", round(expense["total"], 2),
          base_currency)


# Calculate budget status
print("\n========== BUDGET ANALYSIS ==========")

print("Travel Budget:", budget, base_currency)

print("Total Expenses:", round(total_expense, 2),
      base_currency)

remaining = budget - total_expense

if remaining >= 0:
    print("Remaining Budget:", round(remaining, 2),
          base_currency)
    print("Status: WITHIN BUDGET")

else:
    print("Budget Exceeded:", round(abs(remaining), 2),
          base_currency)
    print("Status: OVER BUDGET")


# Find largest expense category
if expenses:

    largest = max(expenses, key=lambda x: x["total"])

    print("\n========== LARGEST EXPENSE ==========")

    print("Largest Expense Category:", largest["category"])

    print("Expense Amount:",
          round(largest["total"], 2), base_currency)

else:
    print("\nNo valid expenses available.")

print("\nTravel budget analysis completed!")
