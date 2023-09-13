# Weight Convertor (lb <-> kb)
unit = input("Enter the unit that you want to convert (lb & kg) : ")

if (unit == "lb") :
    weight = float(input(f"Enter the weight (kg) : "))
    result = weight * 2.205
    print(f"{weight}kg = {result}lb")
elif (unit == "kg") :
    weight = float(input(f"Enter the weight (lb) : "))
    result = round(weight / 2.205,4)
    print(f"{weight}lb = {result}kg")
else :
    print("Invalid Unit")