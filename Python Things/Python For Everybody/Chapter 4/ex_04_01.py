def computepay(hours, rate):
    if hours > 40:
        pay = 40 * rate
        ot = (hours - 40.0) * (rate * 1.5)
        tpay = pay + ot
    else:
        pay = hours * rate
        tpay = pay
    return tpay


hrs = input('Enter hours: ')
rate = input('Enter rate: ')
h = float(hrs)
r = float(rate)
p = computepay(h, r)

print("Pay", p)
