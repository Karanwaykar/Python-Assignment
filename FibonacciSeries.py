terms = int(input("Enter number of terms: "))
a, b = 0, 1
s = 0
for i in range(terms):
    print(a, end=" ")
    s += a
    a, b = b, a+b
print("\nSum of terms:", s)
