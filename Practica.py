def computepay(h, r):
    total = 0
    if(h<=40):
        total = h*r
    else:
        total = r*(40+(h-40)*1.5)
    return total

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
p = computepay(h, r)
print("Pay: ", p)