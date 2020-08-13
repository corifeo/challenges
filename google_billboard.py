"""
https://www.npr.org/templates/story/story.php?storyId=3916173?storyId=3916173&t=1597359482890
TLDR; I was bored, read an article about google billboard ads and decided to hunt for domains
that were 10 digits prime numbers in the consecutive digits of e and pi.
"""

import math
import socket
import numpy as np
PRIME_SIZE = 10
# Got bored of messing with arbitrary precision floats,
# so I've prepackaged 1000 digits of pi and euler from file
digits_raw = np.load('1000-e-digits.npy')
# digits_raw = np.load('1000-pi-digits.npy')
# broadcast array into all possible combination of PRIME_SIZE
digits_expand = digits_raw[np.arange(digits_raw.size-PRIME_SIZE+1)[:, None] +np.arange(PRIME_SIZE)[None, :]]
#  join all combinations into PRIME_SIZE digits ints
digits_master = np.array([np.int(''.join(i)) for i in digits_expand.astype(np.str)])
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
vis_prime = np.vectorize(is_prime)
# return list of primes
digits_primes = digits_master[vis_prime(digits_master)]
def hostname_resolves(n):
    try:
        socket.gethostbyname(''.join([np.str(n), '.com']))
        return True
    except socket.error:
        return False
vis_hostname_resolves = np.vectorize(hostname_resolves)
digits_domains = digits_primes[vis_hostname_resolves(digits_primes)]
# let's see what we've got!
print(digits_domains)