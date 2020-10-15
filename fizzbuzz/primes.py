import math


def primes():
    yield 2
    known_primes = [2]
    iterator = 3
    while True:
        for p in known_primes:
            if not iterator % p:
                # not a prime:
                break
            if p > math.sqrt(iterator):
                'We have a prime'
                known_primes.append(iterator)
                yield iterator
                break
        iterator += 2

            
if __name__ == "__main__":
    my_primes = primes()
    for p in my_primes:
        print(p)
        if p > 3000:
            break
        
