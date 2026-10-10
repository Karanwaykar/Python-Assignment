n = int(input("Enter integer: "))
count = 0
largest, smallest = -1, 9
while n > 0:
    d = n % 10
    count += 1
    if d > largest: largest = d
    if d < smallest: smallest = d
    n //= 10
print("Digits:", count, "Largest:", largest, "Smallest:", smallest)
