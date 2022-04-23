#To find average and grade of given marks
phy = float(input("Enter your Physics marks here : "))
maths = float(input("Enter your Maths marks here : "))
chem = float(input("Enter your Chemistry marks here : "))
eng = float(input("Enter your English marks here : "))
ip = float(input("Enter your I.P. marks here : "))
avg = float(phy+maths+chem+eng+ip)/5
print("Average : ", avg)
if (avg>=80):
    print("Grade : A")
else : 
    print("Grade : B") 

