#!/user/bin/env python3

#Daniel Espitia
#Cuyamaca College CS-119
#Lab 3 , Exercise 2 BMI Calculator


#Declare Variables
#message = ""
#bmi = 0


#input
inches = float(input("Height in inches: "))
pounds = float(input("Weight pounds: "))



#Process
meters = inches / 39.36
kilograms = pounds / 2.2


#calculate BMI
bmi = kilograms / meters**2
 


#Conditions
if bmi <= 18.5:
    print("You are Underweight.")
elif bmi >= 18.5 and bmi <= 24.99:
    print("You are Normalweight.")
elif bmi >= 25 and bmi <= 29.99:
    print("You are Overweight.")
elif bmi >= 30 and bmi <= 39.99:
    print("You are Obese.")
else:
    bmi >= 40
    pass
    print("You are Morbid Obese.")


    
#output
print("Your BMI is:", round(bmi))


