#Program to take user input in kg and give it in quintals and tons 

k = float(input("Write the value in Kilograms : "))
t = float(k/100)
q = float(k/1000)
print(str("Value in Tones : ") + str(t))
print(str("Value in Quintals") + str(q))

