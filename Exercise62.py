prices = [4.95, 9.95, 14.95, 19.95, 24.95]
print("Original Price| Discount Amount| New Price")
for price in prices:
    discount = round(price * 0.60, 2)
    new_price = round(price - discount, 2)
    print(price,"\t\t",discount,"\t\t",new_price)