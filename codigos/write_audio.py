import sounddevice as sd
import matplotlib.pylab as plt
import scipy.io.wavfile as wavfile 
import wavio
import wave

fs = 8000  # Sample rate
seconds = 4  # Duration of recording
print("grabando")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=5)
sd.wait()  # Wait until recording is finished
wavio.write('/home/angie/Documents/git/python_dsp/codigos/abcd_1.wav', myrecording, fs, sampwidth=3)  # Save as WAV file