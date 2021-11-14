# Ask the user for salary, portion to save and cost of home

annual_salary = float(input("Enter your annual salary: "))
monthly_salary = annual_salary / 12
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04


# Loops through each month, adding portion saved plus investments
# until the savings exceed down payment.
months = 0
while current_savings < portion_down_payment:
    investments = current_savings * (r/12)
    current_savings = current_savings + portion_saved*monthly_salary + investments
    months = months + 1
    # Checks to see if 6 months have passed and gives semi annual raise
    if months%6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
print("Number of months:", months)

