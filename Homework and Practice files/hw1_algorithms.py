# Check if the number is divisible by 3 and print 'Bar'
def foo_bar(n: int):
    for i in range(1, 101):
        if i % 3 == 0:
            print('Bar')
        else:
            print(i)
#
#
foo_bar(3)

# Task 1. There is a program that prints the numbers from 1 to 100.
# If the number is divisible of 3, print “Bin”
# If the number is divisible of 7, print “Go”
# For numbers which are divisible of 3 and 7, print “BinGo”

def bingo():
    for numbers in range(1,101):
        if numbers % 3 == 0 and numbers % 7 == 0:
            print('Bingo')
        elif numbers % 3 == 0:
            print('Bin')
        elif numbers % 7 == 0:
            print('Go')
        else:
            print(numbers)


bingo()


# Task 2. Compute the sum of digits in all numbers from 1 to n. When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

def sum_numbers(n: int):
    final_sum = 0
    for i in range(n + 1):
        final_sum = final_sum + i
    return final_sum


print(sum_numbers(5))

# Find the max number from 3 values.
def find_max(a: int, b: int, c: int):
    if c > b and a:
        print(c)
    elif a > b and c:
        print(a)
    elif b > a and c:
        print(b)


find_max(50, 100, 200)


# 2. Leap year. When a function gets a year, the code detects if it is a leap year or not.

def leap_year(year: int):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(True)
    else:
        print(False)


leap_year(5)

# Level 3
# Fibonacci. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. Print out the Fibonacci sequence until the given n-th in the sequence.
# Example: n = 7, print out the sequence: 0, 1, 1, 2, 3, 5, 8


def generate_fibonacci_sequence(n: int):
    #     # Initialize the list with the first two Fibonacci numbers
    fib_sequence = [0, 1]
    #
    #     # Use a for loop to generate the remaining Fibonacci numbers after the first two
    for i in range(2, n):
        new_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(new_number)
    #         fib_sequence = fib_sequence[-1] + fib_sequence[-2]
    #
    return fib_sequence


#
print(generate_fibonacci_sequence(20))

# Calculate the next Fibonacci number using the formula fib_sequence[-1] + fib_sequence[-2]

# Append the new Fibonacci number to the list using the append() function
#
# return fib_sequence
