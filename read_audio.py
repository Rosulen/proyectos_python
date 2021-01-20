# Para reproducir audio

import pyaudio
import scipy.io.wavfile as wavfile
import matplotlib.pylab as plt
import wave

from playsound import playsound

playsound('/home/angie/Git/python_dsp/alejandro.wav')

## para gráficarlo

rate, data = wavfile.read("alejandro.wav") # donde rate es la frecuencia de muestreo y data son los datos del sonido

print(rate) 

plt.figure(1)
plt.plot(data)

## Recortar audio e imprimir

a = data[500:15000]

plt.figure(2)
plt.plot(a)
plt.show() # Siempre al final de las gráficas

print("ok") 