def primeFactors(n):
    #primes = gen_primes()
    #print(primes)
    factors = factorise(n,[])
    print(factors)
    #print(factors)

    #print(set(factors))

    factor_set = list(set(factors))
    factor_set.sort()
    #print(factor_set)
    _str = ""

    for factor in factor_set:
        _count = factors.count(factor)
        if _count > 1:
            _s = "({}**{})".format(factor,_count) 
        else :
            _s = "({})".format(factor)
        
        _str = _str + _s

    return _str
    
def factorise(n, factors):
    #print(n)
    #print(factors)
    if n == 1:
        return factors
        
    #primes = [2,3,5,7,11,13,17]
    #print(primes)
    primes = gen_primes()
    #print(primes)
    while True:
        prime = next(primes)
        #print(prime)
        if n % prime == 0:
            #print("{} / {}".format(n,prime))
            new_n = n / prime
            factors.append(prime)
            return factorise(int(new_n), factors)
    #for prime in next(primes):
          

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
            q = q + 1
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
            q = q + 1
            
        