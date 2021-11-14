# Ask the user for salary, portion to save and cost of home

annual_salary = int(input("Enter your annual salary: "))
monthly_salary = annual_salary / 12
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) * monthly_salary
total_cost = int(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04


# Loops through each month, adding portion saved plus investments
# until the savings exceed down payment.
months = 0
while current_savings < portion_down_payment:
    investments = current_savings * (r/12)
    current_savings = current_savings + portion_saved + investments
    months = months + 1
print("Number of months:", months)

