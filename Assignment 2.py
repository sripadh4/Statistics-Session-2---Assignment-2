
# coding: utf-8

# In[5]:

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

