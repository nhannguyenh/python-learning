def all_primes_up_to(num):
    primeNumbers = [2]
    for number in range(3, num):
        sqrtNumber = number ** 0.5
        for factor in primeNumbers:
            if number % factor == 0:
                break
            if factor > sqrtNumber:
                primeNumbers.append(number)
                break
    return primeNumbers

print(all_primes_up_to(53))