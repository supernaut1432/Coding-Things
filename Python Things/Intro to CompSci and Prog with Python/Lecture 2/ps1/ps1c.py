starting_salary = int(input("Enter the starting salary: "))
semi_annual_rise = 0.07
annual_return = 0.04
total_cost = 1000000
portion_down_payment = total_cost * 0.25
months = 36

low = 0        # 0%
high = 10000    # 100%
increment = 100

guess = int((high + low) / 2)
steps = 0
found = False

while abs(low - high) > 1:
    steps += 1
    annual_salary = starting_salary
    monthly_saved = (annual_salary / 12.0) * (guess / 10000)
    current_savings = 0.0

    for i in range(1, months + 1):
        monthly_return = current_savings * (annual_return / 12)
        current_savings += monthly_return + monthly_saved

        if abs(current_savings - portion_down_payment) < increment:
            low = high
            found = True
            break
        elif current_savings > portion_down_payment + increment:
            break

        if i % 6 == 0:
            annual_salary += annual_salary * semi_annual_rise
            monthly_saved = (annual_salary / 12.0) * (guess / 10000)

    if current_savings < portion_down_payment - increment:
        low = guess
    elif current_savings > portion_down_payment + increment:
        high = guess

    guess = int((high + low) / 2)

if found:
    print("Best savings rate:", guess / 10000)
    print("Steps in bisection search", steps)
else:
    print("Is is not possible to pay the down payment in three years")