import pyaudio
import scipy.io.wavfile as wavfile
import matplotlib.pylab as plt
import numpy as np
import wave

from scipy.fft import fft, fftfreq
from playsound import playsound

## Reproducir audio
playsound('/home/angie/Git/python_dsp/alejandro.wav')

## trear, extraer y gráficar los datos de audio
fs, data = wavfile.read("alejandro.wav") 

plt.figure(1)
plt.plot(data)
plt.grid()

## aplicar transformada a la señalgir
l = len(data)
t = 1/fs

x = np.linspace(0.0, l*t, l)
yf = fft(data)
xf = fftfreq(l, t)[:l//2]

plt.figure(2)
plt.plot(xf, 2.0/l * np.abs(yf[0:l//2]))
plt.grid()
plt.show()