# Python program to display all the prime numbers within an interval
# Loop through numbers from 1 to 10
for num in range(1, 11):
    # A prime number is greater than 1
    if num > 1:
        # Check if the number is divisible by any number from 2 to sqrt(num)
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break  # Not a prime number, exit the loop
        else:
            # If no divisors are found, the number is prime
            print(num, end=" ")
