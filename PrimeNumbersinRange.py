start = int(input("Enter start: "))
end = int(input("Enter end: "))
count = 0
for n in range(start, end+1):
    if n > 1:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                break
        else:
            print(n, end=" ")
            count += 1
print("\nTotal primes:", count)
