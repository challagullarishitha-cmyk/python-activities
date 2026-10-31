
print("===== CAMPUS EVENT FINANCIAL PLANNING =====")

# Input event expenses
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per participant: "))
transport = float(input("Enter transport cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))

# Input participant and financial details
participants = int(input("Enter expected number of participants: "))
registration_fee = float(input("Enter registration fee per participant: "))
sponsorship = float(input("Enter sponsorship amount: "))

# Calculate fixed and variable costs
fixed_cost = venue + equipment
variable_cost = catering + transport + certificate

total_variable_cost = variable_cost * participants
total_cost = fixed_cost + total_variable_cost

# Calculate participant contributions
participant_contribution = registration_fee * participants

# Calculate total available funds
total_funds = participant_contribution + sponsorship

# Calculate sponsorship shortfall
shortfall = max(0, total_cost - total_funds)

# Calculate break-even registration count
if registration_fee > variable_cost:
    break_even = (fixed_cost - sponsorship) / (registration_fee - variable_cost)
    break_even = max(0, int(break_even) if break_even == int(break_even)
                     else int(break_even) + 1)
else:
    break_even = None

# Display results
print("\n===== EVENT FINANCIAL REPORT =====")
print("Fixed Costs:", fixed_cost)
print("Variable Cost per Participant:", variable_cost)
print("Total Event Cost:", total_cost)
print("Participant Contributions:", participant_contribution)
print("Sponsorship Amount:", sponsorship)
print("Total Available Funds:", total_funds)
print("Sponsorship Shortfall:", shortfall)

if break_even is not None:
    print("Minimum Registrations to Break Even:", break_even)
else:
    print("Break-even is not possible with the current registration fee.")

if total_funds >= total_cost:
    print("Event Status: Budget is sufficient")
else:
    print("Event Status: Additional funding is required")
