subtotal = 0
for i in range(3):
    price = float(input(f"Enter price of product {i+1}: "))
    qty = int(input(f"Enter quantity of product {i+1}: "))
    subtotal += price * qty
discount = 0.1 * subtotal
gst = 0.18 * (subtotal - discount)
final = subtotal - discount + gst
print("Subtotal:", subtotal, "Discount:", discount, "GST:", gst, "Final:", final)
