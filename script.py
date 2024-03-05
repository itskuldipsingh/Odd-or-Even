# Prompt the user to enter a number
a = int(input("Enter a number: "))

# Check if the number is even by checking if the remainder of 'a' divided by 2 is 0
if a % 2 == 0:
    # If the condition is true, print that the number is even
    print(f"{a} is an even number.")
else:
    # If the condition is not true, print that the number is odd
    print(f"{a} is an odd number.")
