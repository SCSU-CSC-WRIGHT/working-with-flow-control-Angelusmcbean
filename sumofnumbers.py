# Calculate sum of all numbers
total = 0
num = int(input("Enter a number"))
for num in range(1,num+1):
    total += num
    print(f"The sum of all numbers from 1 to {num} is: {total}")

