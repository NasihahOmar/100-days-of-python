weight = 53
height = 1.60
bmi = weight / (height ** 2)
print (bmi)

if bmi < 18.5:
    print ("underweight")

elif bmi >=18.5 and bmi < 25:
    print("normal weight") 

else:
    print("overweight")