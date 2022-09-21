#Data input

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))
n4 = float(input("Enter the fourth number:"))
#Processing

numbers = [ n1, n2, n3 ]
numbers.sort()

numbers2 = [ n1, n2, n3, n4]
numbers2.sort(reverse=True)

print(numbers, (n4))
print(numbers2)