a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# GCD
x, y = a, b
while y:
    x, y = y, x % y
gcd = x
lcm = (a*b)//gcd
print("GCD:", gcd, "LCM:", lcm)
