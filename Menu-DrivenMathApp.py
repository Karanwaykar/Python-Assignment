def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_armstrong(n):
    return sum(int(d)**len(str(n)) for d in str(n)) == n

def factorial(n):
    f = 1
    for i in range(1, n+1): f *= i
    return f

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a+b
    print()

while True:
    print("\nMenu:\n1. Prime\n2. Palindrome\n3. Armstrong\n4. Factorial\n5. Fibonacci\n6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 6: break
    num = int(input("Enter number: "))
    if choice == 1: print("Prime" if is_prime(num) else "Not Prime")
    elif choice == 2: print("Palindrome" if is_palindrome(num) else "Not Palindrome")
    elif choice == 3: print("Armstrong" if is_armstrong(num) else "Not Armstrong")
    elif choice == 4: print("Factorial:", factorial(num))
    elif choice == 5: fibonacci(num)
