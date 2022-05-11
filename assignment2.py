# I William Habsburg, 000869622, certify that this work is my
#own effort and that I have not allowed anyone else to copy from it.
#
# Assignment 4, Question 2

# This function initializes the array from 1 to the number the user entered
def initArray(upTo):
    for num in range(1, upTo + 1):
        primeNumbers.append(num)

# This function checks to see if any number in the primeNumber array is
# by the parameter.  If it is, that number is deleted.
# There are some interesting things going on here, that I chose to speed
# up the process.  First, if the number to check is greater than or equal to
# the prime number we are checking, nothing happens, as we will always get
# a number less than zero.  This takes advantage of short-circuiting
# in the if statement.  Second, since we are checking starting at two,
# if a number is deleted, we skip ahead two numbers in the count, since
# there is no way two sequential numbers will be divisable by the same number.
# I chose a while loop for this reason.  The speed up is modest, but noticable
# for large numbers
def checkMultiples(num2Check):
    count = 2
    while(count < len(primeNumbers)):
        if num2Check < primeNumbers[count] and primeNumbers[count] % num2Check == 0:
            primeNumbers.remove(primeNumbers[count])
        count = count + 1

# This holds our list of potential prime numbers
primeNumbers = []

# Get a number from the user, assume it is an integer
numIn = int(input("Enter a number greater than 100: "))
# Initialize the array using the input number
initArray(numIn)

# loop through all of the numbers from 1 to the input number
for x in range(2, numIn + 1):
    # Call checkMultiples for each number
    checkMultiples(x)

# Output how many prime numbers we have, and a list on one line
print("\nWe found", len(primeNumbers), "prime numbers in that range:")
for num in primeNumbers:
    print(num, end=" ")
print("\n")
