#Finiding largest of three numbers:
numbers = []
for i in range(3):
    n = int(input("Enter the number :"))
    numbers.append(n)
greatest_number = numbers[0]
for number in numbers:
    if number > greatest_number:
        greatest_number = number

print("The greatest number of 3 enetered numbers is ", greatest_number)
