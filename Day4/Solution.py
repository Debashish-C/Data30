def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [num for num in range(1, 101) if is_prime(num)]

with open("numbers.txt", "w") as file:
    for prime in primes:
        file.write(str(prime) + "\n")

print("Prime numbers between 1 and 100 have been saved to numbers.txt")