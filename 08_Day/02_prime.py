


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
