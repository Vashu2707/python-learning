#code to get bmi of a human

mass = float(input("Your weight in kg : ")) 
height = float(input("Your height in m : "))
bmi = mass / (height * height)
print(str("Your body mass index : " + str(bmi)))
