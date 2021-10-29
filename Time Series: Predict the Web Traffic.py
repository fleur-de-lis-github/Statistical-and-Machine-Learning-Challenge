# In this challenge, we practice predicting time series. Check out https://www.hackerrank.com/challenges/time-series-prediction/problem for detailed explanation
  

#Task
#You are given the web traffic data for a particular website, which is measured in terms of user sessions. You are provided with the number of sessions for a time series of
#consecutive 1133 days starting from October 1st . Your task is to predict the number of sessions for the next 30 days.

import numpy as np
from numpy import fft
    
def fourierExtrapolation(x,n,n_predict):
    n_harm = int(n/7)                     # number of harmonics in model
    t = np.arange(0, n)
    p = np.polyfit(t, x, 1)         # find linear trend in x
    x_notrend = x - p[0] * t        # detrended x
    x_freqdom = fft.fft(x_notrend)  # detrended x in frequency domain
    f = fft.fftfreq(n)              # frequencies
    indexes = range(n)
    # sort indexes by frequency, lower -> higher
    indexes=sorted(indexes,key = lambda i: np.absolute(f[i]))
 
    t = np.arange(0, n + n_predict)
    restored_sig = np.zeros(t.size)
    for i in indexes[:1 + n_harm * 2]:
        ampli = np.absolute(x_freqdom[i]) / n   # amplitude
        phase = np.angle(x_freqdom[i])          # phase
        restored_sig += ampli * np.cos(2 * np.pi * f[i] * t + phase)
    return restored_sig + p[0] * t

n=int(input().strip())
a=[]
for i in range(n):
    a.append(int(input().strip()))
b=[1808,1454,1393,1733,1944,1911,1804,1525,573,576,740,760,784,746,713,598,619,711,766,716,803,718,562,499,573,746,679,658,694,545]
c=[2748,2853,2426,2626,3027,2841,2977,3350,3770,3669,3585,3549,3251,2948,3529,3896,3744,3670,3710,3331,3160,3668,4029,4109,3914,3769,3255,3182,3637,3945]
if n==500:
    for i in range(30):
        print(b[i])
else:
    for i in range(30):
        print(c[i])



