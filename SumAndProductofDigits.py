n = int(input("Enter integer: "))
s, p = 0, 1
while n > 0:
    d = n % 10
    s += d
    p *= d
    n //= 10
print("Sum:", s, "Product:", p)
