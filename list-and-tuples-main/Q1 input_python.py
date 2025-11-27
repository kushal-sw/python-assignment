# Input 10 numbers into a list
numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Sort the list in descending order
numbers.sort(reverse=True)

# Print the second largest number
print("Second largest number is:", numbers[1])
