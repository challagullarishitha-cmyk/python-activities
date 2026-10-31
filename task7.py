
# Retail Billing with Multiple Discount Rules

print("========== RETAIL BILLING SYSTEM ==========")

products = []

n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0

for i in range(n):

    print("\nEnter details for Product", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category (food/clothing/electronics): ")

    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    # Input validation
    if price < 0 or quantity <= 0:
        print("Invalid product details!")
        continue

    # Category-specific tax
    if category.lower() == "food":
        tax_rate = 5

    elif category.lower() == "clothing":
        tax_rate = 12

    elif category.lower() == "electronics":
        tax_rate = 18

    else:
        print("Invalid category!")
        continue

    # Calculate product amount
    amount = price * quantity

    # Calculate tax
    tax = amount * tax_rate / 100

    product_total = amount + tax

    subtotal += amount
    total_tax += tax

    products.append({
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "amount": amount,
        "tax": tax,
        "total": product_total
    })


# Threshold discount calculation
print("\n========== DISCOUNT CALCULATION ==========")

if subtotal >= 10000:
    discount_rate = 20

elif subtotal >= 5000:
    discount_rate = 10

elif subtotal >= 2000:
    discount_rate = 5

else:
    discount_rate = 0

discount = subtotal * discount_rate / 100

# Maximum concession limit
max_discount = 2000

if discount > max_discount:
    discount = max_discount

# Final bill calculation
final_bill = subtotal + total_tax - discount

# Display itemized invoice
print("\n========== ITEMIZED INVOICE ==========")

print("Product\tQty\tPrice\tAmount\tTax")

for p in products:
    print(
        p["name"], "\t",
        p["quantity"], "\t",
        p["price"], "\t",
        round(p["amount"], 2), "\t",
        round(p["tax"], 2)
    )

print("--------------------------------------")

print("Subtotal: Rs.", round(subtotal, 2))
print("Total Tax: Rs.", round(total_tax, 2))
print("Discount Rate:", discount_rate, "%")
print("Discount Amount: Rs.", round(discount, 2))
print("Maximum Discount Limit: Rs.", max_discount)

print("--------------------------------------")
print("FINAL BILL: Rs.", round(final_bill, 2))

print("\nThank you for shopping!")
