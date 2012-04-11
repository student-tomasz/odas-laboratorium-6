#!./env/bin/python

from bitarray import bitarray

def inverse(target, modulo):
    if not are_coprime(target, modulo):
        return None
    else:
        return __inverse_by_eratostenes(target, modulo)

def __inverse_by_internets(target, modulo):
    u, w, x, z = 1, target, 0, modulo
    while w:
        if w < z:
            u, x = x, u
            w, z = z, w
        q = w / z
        u -= q * x
        w -= q * z
    if z == 1:
        if x < 0:
            x += modulo
    return x

def __inverse_by_eratostenes(target, modulo):
    a, b = target, modulo
    u, u1 = 1, 0
    v, v1 = 0, 1
    while b:
        q = a // b
        u, u1 = u1, u - q * u1
        v, v1 = v1, v - q * v1
        a, b = b, a - q * b
    return u % modulo

def power(base, exponent, modulus):
    return __power_by_python(base, exponent, modulus)

def __power_by_python(base, exponent, modulus):
    return pow(base, exponent, modulus)

def __power_by_euler(base, exponent, modulus):
    result = 1
    base %= modulus
    i = 0
    while i < exponent:
        result *= base
        result %= modulus
        i += 1
    return result

def are_coprime(a, b):
    return __gcd(a, b) == 1

def is_prime(number):
    return __is_prime_by_eratostenes(number)

def __gcd(a, b):
    a, b = (b, a) if a < b else (a,     b)
    while b != 0:
       a, b = b, a % b
    return a

def __is_prime_by_eratostenes(number):
    prime_numbers = bitarray(number+1)
    prime_numbers.setall(True)
    i = 2
    while i <= number / 2:
        if prime_numbers[i]:
            j = 2*i
            while j <= number:
                prime_numbers[j] = False
                j += i
        i += 1

    return prime_numbers[number]



if __name__ == '__main__':
    assertions = [
        is_prime(3),
        is_prime(2),
        is_prime(7),
        not is_prime(16),

        are_coprime(3, 5),

        __gcd(9, 6) == 3,
        __gcd(18, 24) != 3,
        __gcd(12, 24) == 12,
        __gcd(24, 12) == 12,
        __gcd(3, 5) == 1,
        __gcd(6, 7) == 1
    ]

    for assertion in assertions:
        if assertion:
            print 'passed'
        else:
            print 'failed'

    assertions = [
        inverse(2, 5) == 3,
        inverse(12767, 256) == 31,
        inverse(12768, 256) == None,
        power(12, 4, 7) == 2,
        power(2, 42, 43) == 1,
        power(8, 13, 5) == 3
    ]
    for assertion in assertions:
        if assertion:
            print 'passed'
        else:
            print 'failed'
