marks = [int(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]
total = sum(marks)
average = total / 5
percentage = (total / 500) * 100
print("Total:", total, "Average:", average, "Percentage:", percentage)
