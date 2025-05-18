Q#1: Write a Python program that takes a person's age and categorizes it as:

#Child (<13)

#Teen (13-19)

#Adult (20-59)

#Senior (60+)

age = int(input("Enter your age: "))

if age < 13:
    print("Category: Child")
elif age <= 19:
    print("Category: Teen")
elif age <= 59:
    print("Category: Adult")
else:
    print("Category: Senior")



Q#2: Write a Python program to check if a given number is positive, negative or zero.

num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



Q#3: Write a Python program to:

Print the nth item of a number list

Print all the numbers in the list

numbers = [10, 20, 30, 40, 50]
n = int(input("Enter the index (0-4) of the number to print: "))

# Print nth item
if 0 <= n < len(numbers):
    print("The item at index", n, "is", numbers[n])
else:
    print("Invalid index")

# Print all numbers
print("All numbers in the list:")
for number in numbers:
    print(number)



Q#4: Write a Python program to create a dictionary and then update its value.

# Create dictionary
person = {
    "name": "Ali",
    "age": 25,
    "city": "Lahore"
}

print("Original dictionary:", person)

# Update a value
person["age"] = 26
print("Updated dictionary:", person)