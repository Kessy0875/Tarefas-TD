

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("enter the third number: "))

message = str()

media = (n1+n2+n3)/3

if media >= 0 and media <= 3:
   message = "Reprovar"

elif media > 3 and media <= 7:
    message = "Exame"

elif media >=7 and media <= 10:
    message = "Aprovado"

print(f"Your average is: {round(media,2)} your state is: {message}")