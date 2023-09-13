# Discount Program
# price > 1000 | 10% discount
# price > 5000 | 20% discount
# price > 10000 | 30% discount
# price > 15000 | 40% discount
# price > 20000 | 50% discount

price = float(input("Enter the price : "))

if (price >= 20000) :
    discount = price * 0.5
    print(f"Discount Price : {discount}")
elif (price >= 15000) :
    discount = price * 0.6
    print(f"Discount Price : {discount}")
elif (price >= 10000) :
    discount = price * 0.7
    print(f"Discount Price : {discount}")
elif (price >= 5000) :
    discount = price * 0.8
    print(f"Discount Price : {discount}")
elif (price >= 1000) :
    discount = price * 0.9
    print(f"Discount Price : {discount}")
else : 
    print(f"No Discount : {price}")
