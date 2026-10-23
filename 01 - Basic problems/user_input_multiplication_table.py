#Print multiplication table of a user-given number.
#prompting user for a number
n = int(input("Enter the value of n:"))
for i in range(1,11):
    print(i , " x ", n, " = ", i * n )
