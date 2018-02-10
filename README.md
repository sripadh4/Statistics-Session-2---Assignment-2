# Statistics-Session-2---Assignment-2
A die marked A to E is rolled 50 times. Find the probability of getting a “D” exactly 5
times.

N = 1
X = 1
PNX = (1/5) ** 5
PN = (4/5) ** 45
NFactorial = range(46, 51)
for i in NFactorial:
    N *= i
XFactorial = range(1, 6)
for j in XFactorial:
    X *= j
Probability = ((N/X)*(PNX)*(PN))
print (Probability)
