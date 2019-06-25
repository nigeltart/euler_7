def prime (number):
    for divisor in range (2, int(number**0.5)+1):
        #print (divisor)     #debug
        if number%divisor==0:   #no remainder
            return False
    return True

primes = [2, 3, 5, 7, 11]
candidate = primes[-1]
while len(primes) < 10001:
    candidate += 2
    while not prime(candidate):
        candidate += 2
    primes.append(candidate)
print (primes[-1])


