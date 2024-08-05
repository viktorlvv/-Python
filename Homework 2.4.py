numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 51]
primes = []
not_primes = []
num = numbers[0]
for i in range(len(numbers)):
    is_prime = False
    num = numbers[i]
    if num == 1:
        continue
    for j in range(2, num):
        if num % j == 0:
            is_prime = True
            break
    if is_prime:
        not_primes.append(num)
    else:
        primes.append(num)
print("Простые числа: ", primes)
print("Составные числа: ", not_primes)
