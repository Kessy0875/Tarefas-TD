#Entrada de dados

Lab = float(input("Enter the lab work grade: "))
pes1 = 2
avSem = float(input("Enter the semester assessment grade: "))
pes2 = 3
exfinal = float(input("Enter a final exam grade: "))
pes3 = 5
conceito = str()
#Processamento

average = ((Lab*pes1)+(avSem*pes2)+(exfinal*pes3))/10

if average >=8 and average <=10: 
    conceito = "A"

elif average >=7 and average <=8:
    conceito = "B"

elif average <= 7 and average >=6:
    conceito = "C"

elif average <=6 and average >=5:
    conceito = "D"

elif average <=5 and average >=0:
    conceito = "E"

print(f"Your media is: {round(average,1)} and your concept is {conceito}")