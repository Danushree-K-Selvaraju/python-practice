#Find sum of all even numbers between 1 to n.
n = int(input("Enter the value of n:"))
sum = 0
for i in range (1, n + 1):
    if n % 2 == 0:
        sum += i

print(sum)