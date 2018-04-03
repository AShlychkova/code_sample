#Шлычкова Александра 699


%pylab inline
import numpy as np
import matplotlib.pyplot as plt


def FFT(x):
    N = len(x)
    if N <= 1: return x
    even = FFT(x[0::2])
    odd =  FFT(x[1::2])
    T= [exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
    return [even[k] + T[k] for k in range(N//2)] + \
           [even[k] - T[k] for k in range(N//2)]

def RFFT(x):
    u = np.conj(x)
    u = FFT(u)
    u = np.divide(np.conj(u), len(x))
    return u
    
# Рисует график функции, к которой применены прямое и обратное преобразования Фурье
def RFFTplot(func, xlist, N):
    pylab.plot (xlist[:N], [x.real for x in RFFT(FFT([func(x) for x in xlist]))][:N])
    
# Рисует график функции, к которой применены прямое преобразования Фурье, и последние D коэффициэнтов =0 и обратное преобразования Фурье
def RFFTplotD(func, xlist, N, D):
    pylab.plot (xlist[:N], [x.real for x in RFFT(FFT([func(x) for x in xlist])[:N-D] + [0 for i in range(len(xlist)-N +D)])][:N])
    
    

xlist =  [0.01*i for i in range(1001)]
N = len(xlist)
for i in range (2**(int(math.log2(len(xlist)))+1) - len(xlist)): 
    xlist.append(0)
pylab.subplot (231)
RFFTplot(math.sin, xlist, N)
D = -100
RFFTplotD(math.sin, xlist, N, D)
pylab.subplot (232)
RFFTplot(lambda x:x , xlist, N)
D = -230
RFFTplotD(lambda x:x , xlist, N, D)
pylab.subplot (233)
RFFTplot(lambda x:x*x , xlist, N)
D = -24
RFFTplotD(lambda x:x*x , xlist, N, D)
pylab.subplot (234)
RFFTplot(lambda x:math.sin(x)**2 , xlist, N)
D = 24
RFFTplotD(lambda x:math.sin(x)**2 , xlist, N, D)
pylab.subplot (235)
RFFTplot(lambda x:math.sin(x)/(x+0.0000001) , xlist, N)
D = 200
RFFTplotD(lambda x:math.sin(x)/(x+0.0000001) , xlist, N, D)


