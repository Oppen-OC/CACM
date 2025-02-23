import sys
import math

for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        break
    print("yes" if math.isqrt(n) ** 2 == n else "no")