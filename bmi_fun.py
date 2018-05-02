name = "dhruv"
height = 6
weight = 57

name = "df"
height = 43
weight = 56

def bmi_calculator(name , height , weight):
    bmi = weight/(height ** 2)
    print("BMI:")
    print(bmi)
    if bmi<25:
        return name + "not overweight"
    else:
        return name + "is overweight"
result = bmi_calculator(name,height,weight)
result1 = bmi_calculator(name,height,weight)
print(result)
print(result1)
