import sounddevice as sd
import matplotlib.pylab as plt
import scipy.io.wavfile as wavfile
import numpy as np
import scipy as sp
import itertools
import os
import pyaudio
import wavio
import wave

from tkinter import *
from playsound import playsound 
from scipy import signal
from scipy.fft import fft, fftfreq

# Creación de la ventana
def grabar():

    global y, fs

    fs = 8000  # Sample rate
    seconds = 10  # Duration of recording
    lblgrabando = Label(ventana, text="Grabando...",font=("Consolas", 14)).place(x=150, y=550)
    print("grabando")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    wavio.write('audio.wav', myrecording, fs, sampwidth=3)  # Save as WAV file

    # Traer datos de audio
    fs, y = wavfile.read("audio.wav")

    # normailizar la señal (dejar la amplitud entre 1 y -1)
    amax = max(y)
    amin = min(y)
    n = np.array([amax, amin*-1])
    amax = max(n)
    y = y/amax

    ## aplicar transformada a la señal
    l = len(y)
    t = 1/fs

    x = np.linspace(0.0, l*t, l)
    yf = fft(y)
    xf = fftfreq(l, t)[:l//2]

    ## Filtro pasa bajo
    nyq = fs * 0.5

    cutoff = 1000
    stopfreq = float(cutoff)
    cornerfreq = 0.4 * stopfreq # (?)

    ws = cornerfreq/nyq
    wp = stopfreq/nyq

    n, wn =signal.buttord(wp, ws, 3, 40) # (?)
    b, a = signal.butter(n, wn, btype='low') # para pasa altos cambia 'low' por 'high'

    w,h = signal.freqz(b,a)

    sf = signal.lfilter(b, a, y)
    l = len(sf)
    t = 1.0 / fs
    x = np.linspace(0.0, l*t, l)
    yf = fft(sf)
    xf = fftfreq(l, t)[:l//2]

    plt.figure(1)
    plt.plot(sf) # Imprimir audio filtrado en el dominio del tiempo
    plt.title("Señal obtenida")
    
    plt.savefig("senal_data.png") # Guardar como imagen

    plt.show()

    return y, fs


def procesar():

    global y, fs

    n = 0
    l = len(y)
    contador = 0

    vec_energia = []

    # calcular energía
    while contador < l:
        x = y[contador:contador+499]
        energia = 0
        
        if contador+999 > l:
            x = y[contador:]

        for i in x:
            energia = energia + i**2

        vec_energia.append(energia)
        print(energia)
        contador += 500

    senal_cuadrada = []

    # Pasar señal cuadrada
    for p in vec_energia:
        if p < 30:
            senal_cuadrada.append(0)

        else:
            senal_cuadrada.append(1)

    vec_energia = np.array(vec_energia)
    senal_cuadrada = np.array(senal_cuadrada)

    plt.figure(2)
    plt.plot(senal_cuadrada)


    j = 0
    pos = []
    contador = 0

    # reemplazar valores que no deben estas, falta revisión
    for j in senal_cuadrada:

        if j != senal_cuadrada[contador-1]:
            if j == senal_cuadrada[contador+1]:
                pos.append(contador)
            else:
                senal_cuadrada[contador] = senal_cuadrada[contador-1]

        if j == 1 and j != senal_cuadrada[contador+1] and j == senal_cuadrada[contador+5]:
            
            senal_cuadrada[contador+1] = 1
            senal_cuadrada[contador+2] = 1
            senal_cuadrada[contador+3] = 1
            senal_cuadrada[contador+4] = 1


        contador += 1

    n_palabras = len(pos)
    n_palabras = n_palabras/2
    print(f'{n_palabras} palabras fueron detectadas')

    plt.figure(3)
    plt.plot(senal_cuadrada)
    plt.show()

    n_nombre = 1
    pos = np.array(pos)
    pos = pos*500

    contador = 0

    name = 'resultado'
    ext = 'wav'
    i = 0

    while i < n_palabras:

        l = len(pos)
        
        if l > 2:
            # cortar = y[pos[contador]:pos[contador+1]]
            actualname = "%s.%s" % (name, ext)
            c = itertools.count()
            while os.path.exists(actualname):
                actualname = "%s (%d).%s" % (name, next(c), ext)

            wavio.write(actualname, y[pos[contador]:pos[contador+1]], fs, sampwidth=3)
            
        else:
            actualname = "%s.%s" % (name, ext)
            c = itertools.count()
            while os.path.exists(actualname):
                actualname = "%s (%d).%s" % (name, next(c), ext)

            wavio.write(actualname, y[pos[contador]:pos[contador+1]], fs, sampwidth=3)

        i += 1
        contador += 2        
 
ventana = Tk()

ventana.geometry("600x600+100+200") # Geometria de la ventana
ventana.title("Nombre del formulario") # Nombre de la interface

img = PhotoImage(file="senal_data.png")
widget = Label(ventana, image=img).pack()

# creación bontones
btngrabar = Button(ventana,text="Grabar",command = grabar,font=("Consolas",14)).place(x=100,y=500) # Creación del boton saludar 
btnprocesar = Button(ventana,text="Procesar",command = procesar,font=("Consolas",14)).place(x=300,y=500) # Creación del boton saludar 

ventana.mainloop() # Mostrar ventana