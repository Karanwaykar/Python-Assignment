N = int(input("Enter number of students: "))
marks = [int(input(f"Enter marks of student {i+1}: ")) for i in range(N)]
avg = sum(marks)/N
high = max(marks)
low = min(marks)
passed = sum(1 for m in marks if m >= 40)
failed = N - passed
above75 = sum(1 for m in marks if m > 75)
print("Average:", avg)
print("Highest:", high, "Lowest:", low)
print("Passed:", passed, "Failed:", failed)
print("Above 75%:", above75)
