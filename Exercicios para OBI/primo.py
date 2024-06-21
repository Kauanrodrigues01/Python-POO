import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    sqrt_n = n-1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    
    return True

# Exemplos de uso
print(is_prime(7))   # True
print(is_prime(11))  # True
print(is_prime(12))  # False
print(is_prime(23))  # True
print(is_prime(1))   # False
print(is_prime(2))   # True
