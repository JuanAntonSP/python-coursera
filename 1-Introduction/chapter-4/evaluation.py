def computepay(h, r):
    return h * r


hrsStr = input("Enter Hours:")
rateStr = input("Enter rate:")

hrsNumber = float(hrsStr)
rateNumber = float(rateStr)

if hrsNumber > 40:
    p = computepay(40, rateNumber)
    p = p + computepay(hrsNumber - 40, rateNumber * 1.5)
else:
    p = computepay(40, rateNumber)

print("Pay", p)
