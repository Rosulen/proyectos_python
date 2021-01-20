import sounddevice as sd
import matplotlib.pylab as plt
import scipy.io.wavfile as wavfile 
import wavio
import wave


fs = 44100  # Sample rate
seconds = 5  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
wavio.write('sin_titulo.wav', myrecording, fs, sampwidth=3)  # Save as WAV file



