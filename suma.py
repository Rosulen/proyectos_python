import sounddevice as sd
import matplotlib.pylab as plt
import scipy.io.wavfile as wavfile 
import wavio
import wave

from playsound import playsound

fs, nombre = wavfile.read("nombre.wav")
fs, saludo = wavfile.read("saludo.wav")

suma = nombre + saludo

wavio.write('suma.wav', suma, fs, sampwidth=3)
playsound('/home/angie/Git/python_dsp/suma.wav')

plt.figure(1)
plt.plot(nombre)
plt.figure(2)
plt.plot(saludo)
plt.figure(3)
plt.plot(suma)
plt.show()