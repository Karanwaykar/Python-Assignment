a, b, c = [int(input(f"Enter side {i+1}: ")) for i in range(3)]
if a+b>c and b+c>a and a+c>b:
    if a==b==c: print("Equilateral")
    elif a==b or b==c or a==c: print("Isosceles")
    else: print("Scalene")
else:
    print("Invalid triangle")
