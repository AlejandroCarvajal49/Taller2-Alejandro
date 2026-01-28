def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_primes(limit):
    """Return a list of all prime numbers up to the given limit."""
    return [n for n in range(2, limit + 1) if is_prime(n)]


# Example usage
if __name__ == "__main__":
    print(get_primes(25))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print("Hola")