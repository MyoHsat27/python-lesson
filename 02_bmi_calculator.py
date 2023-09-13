# BMI Calculator
weight = float(input("Enter your weight (kg) : "))
height = float(input("Enter your height (cm) : "))
bmi_result = round(weight / (height / 100)**2,2)

if (bmi_result <= 18.5) :
    print(f"BMI Result : {bmi_result}")
    print("Your are underweight.")
elif (bmi_result <= 24.9) :
    print(f"BMI Result : {bmi_result}")
    print("Your are normal weight.")
elif (bmi_result >= 25) :
    print(f"BMI Result : {bmi_result}")
    print("Your are overweight.")
else :
    print(f"BMI Result : {bmi_result}")
    print("Your are obesity.")