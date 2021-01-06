import matplotlib.pyplot as plt
def getpi(n):
    x=0.0
    y=0.0
    res=0
    z=1
    count=0
    for i in range(1, n*2+1, 2):
        res+=z*4/i
        z*=-1
    return res

counts=[i for i in range(1, 100)]
pis=[getpi(i) for i in counts]
plt.plot(counts, pis)
plt.show()
