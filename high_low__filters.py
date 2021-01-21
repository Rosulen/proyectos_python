import pyaudio
import scipy.io.wavfile as wavfile
import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import wave

from scipy import signal
from scipy.fft import fft, fftfreq
from playsound import playsound

## Reproducir audio
playsound('/home/angie/Git/python_dsp/alejandro.wav')

## trear, extraer y gráficar los datos de audio
fs, data = wavfile.read("alejandro.wav") 

plt.figure(1)
plt.plot(data)
plt.grid()

## aplicar transformada a la señal

l = len(data)
t = 1/fs

x = np.linspace(0.0, l*t, l)
yf = fft(data)
xf = fftfreq(l, t)[:l//2]

plt.figure(2)
plt.plot(xf, 2.0/l * np.abs(yf[0:l//2]))
plt.grid()

## Filtro pasa bajo

nyq = fs * 0.5

cutoff = 1500
stopfreq = float(cutoff)
cornerfreq = 0.4 * stopfreq # (?)

ws = cornerfreq/nyq
wp = stopfreq/nyq

n, wn =signal.buttord(wp, ws, 3, 40) # (?)
b, a = signal.butter(n, wn, btype='low') # para pasa altos cambia 'low' por 'high'

w,h = signal.freqz(b,a)

plt.figure(3)
plt.plot(w, abs(h)) # Imprimir forma del filtro

sf = signal.lfilter(b, a, data)
l = len(sf)
t = 1.0 / fs
x = np.linspace(0.0, l*t, l)
yf = fft(sf)
xf = fftfreq(l, t)[:l//2]

plt.figure(4)
plt.plot(xf, 2.0/l * np.abs(yf[0:l//2])) # Imprimir la transformada del audio filtrado
plt.grid()

plt.figure(5)
plt.plot(sf) # Imprimir audio filtrado en el dominio del tiempo
plt.show()