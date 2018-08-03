# has error 'power' is not defined
from functools import partial

# square = partial(power, exponent=2)
# print(square(2))

powers = []
for x in range(2,1001):
    powers.append(partial(power,exponent = x))

print(powers[2](2))