#Display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration 
n = int(input("Enter the value of n:"))
for i in range(1,n + 1):
    if i % 5 == 0:
        print(i)
    if i >= 150:
        break