
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("enter the third number: "))

message = str()

average = (n1+n2+n3)/3

if average >= 0 and average <= 3:
   message = "Reprovado"

elif average > 3 and average <= 7:
    message = "Exame"

elif average >=7 and average <= 10:
    message = "Aprovado"

print(f"Your average is: {round(average,2)} your state is: {message}")