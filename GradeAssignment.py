perc = float(input("Enter percentage: "))
if 0 <= perc <= 100:
    if perc >= 90: grade = "A+"
    elif perc >= 75: grade = "A"
    elif perc >= 60: grade = "B"
    elif perc >= 40: grade = "C"
    else: grade = "Fail"
    print("Grade:", grade)
else:
    print("Invalid percentage")
