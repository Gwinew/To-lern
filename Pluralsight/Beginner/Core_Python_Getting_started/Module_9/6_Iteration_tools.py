# Iteration Tools
#
#
#################
# itertools.islice()
#
# - Perform lazy slicing of any iterator.
# - from itertools import islice
#   islice(all_primes, 1000)
#################
# itertools.count()
#
# - An unbounded arithmetic sequence of integers.
#
from math import sqrt
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x))+1):      # Pierwiastek
        if x % i == 0:
            return False
    return True
from itertools import count, islice
thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
print(thousand_primes)
print(list(thousand_primes)[-10:])

sum(islice((x for x in count() if is_prime(x)),1000))
######################
#
# any():
#
# - Determines if any elements in a series are true
#
# all():
#
# - Determines if all elements in a series are true
#
print(any([False, False, True]))
print(all([False, False, True]))
print(any(is_prime(x) for x in range(1328,1361)))
#
#
# zip():
#
# - Synchronize iteration across two or more iterables.
sunday = [12,14,15,15,17,21,22,22,23,22,20,18]
monday = [13,14,14,14,16,20,21,22,22,21,19,17]
for item in zip(sunday,monday):
    print(item)

for sun, mon in zip(sunday, monday):
    print('avarage=',(sun + mon)/2)


tuesday = [2,2,3,7,9,10,11,12,10,9,8,8]
for temps in zip(sunday, monday, tuesday):
    print(f'min= {min(temps):4.1f}, max= {max(temps):4.1f}, average = {sum(temps)/len(temps):4.1f}')

    from itertools import chain
    temperatures = chain(sunday, monday, tuesday)
    print(all(t>0 for t in temperatures))


