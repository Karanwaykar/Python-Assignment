n = int(input("Enter integer: "))
temp, rev = n, 0
while temp > 0:
    rev = rev*10 + temp%10
    temp //= 10
print("Palindrome" if rev == n else "Not Palindrome")
