# Python Program to Check if a Number is Even or Odd

This simple Python program prompts the user to enter a number and checks whether it is even or odd.

## Usage

1. **Enter a Number:**
   - Run the program and enter a numerical value when prompted.

2. **Even or Odd:**
   - The program will determine whether the entered number is even or odd.

## [Python Code](https://github.com/itskuldipsingh/Math/blob/main/Odd%20or%20even%20number/script.py)

```python
# Prompt the user to enter a number
a = int(input("Enter a number: "))

# Check if the number is even by checking if the remainder of 'a' divided by 2 is 0
if a % 2 == 0:
    # If the condition is true, print that the number is even
    print(f"{a} is an even number.")
else:
    # If the condition is not true, print that the number is odd
    print(f"{a} is an odd number.")
