usage = float(input("Enter monthly data usage in GB: "))
if usage <= 10:
    bill = usage * 50
elif usage <= 30:
    bill = 10*50 + (usage-10)*40
else:
    bill = 10*50 + 20*40 + (usage-30)*30
print("Total bill:", bill)
