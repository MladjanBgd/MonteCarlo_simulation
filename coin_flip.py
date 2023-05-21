#simulating coin flip

import random

N = 100
epoches = 5

for _ in range(epoches):
    N *= 10
    vals = []
    for _ in range(N):
        vals.append(random.choice([0,1]))
    one = vals.count(1)
    zero = vals.count(0)

    print(f"N={N}, one's={one};{one/N}, zero's={zero};{zero/N}")

print('finished')