 def is_prime(num):
    """Checks if a number is prime."""

    if num <= 1:
        return False

    # Check for divisibility up to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
