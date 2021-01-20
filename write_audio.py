import sounddevice as sd
import scipy.io.wavfile as wavfile 
import wavio

fs = 44100  # Sample rate
seconds = 5  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
wavio.write('saludo.wav', myrecording, fs, sampwidth=3)  # Save as WAV file

## sumar dos audios
""" 
rate, data = wavfile.read("alejandro.wav")
print(rate) 

plt.figure(1)
plt.plot(data) """
