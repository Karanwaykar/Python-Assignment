n = int(input("Enter integer: "))
temp, s = n, 0
digits = len(str(n))
while temp > 0:
    s += (temp % 10) ** digits
    temp //= 10
print("Armstrong" if s == n else "Not Armstrong")
