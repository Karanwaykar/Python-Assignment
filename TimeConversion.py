seconds = int(input("Enter time in seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60
print(f"{hours}h:{minutes}m:{secs}s")
