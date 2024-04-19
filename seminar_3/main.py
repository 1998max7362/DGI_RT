import matplotlib.pyplot as plt
import numpy as np

fileobj =  open("seminar_3/1kHz_44100Hz_16bit_05sec.wav" , mode="rb")

data = fileobj.read()

# число бит в сигнале
file_size_inbytes = data[4:8]
print(file_size_inbytes)

# число байт в сигнале
file_size = int.from_bytes(file_size_inbytes, byteorder= 'little')
print(file_size)

# колличество каналов
num_of_channel_in_inbytes = data[22:24]
num_of_channel = int.from_bytes(num_of_channel_in_inbytes, byteorder= 'little')
print(num_of_channel)

# значение аудио файла в байтах
audio_data_size_in_inbytes = data[40:44]
audio_data_size = int.from_bytes(audio_data_size_in_inbytes, byteorder= 'little')
print(audio_data_size)


# частота дикретизации
sampl_rate_in_bytes = data[24:28]
sampl_rate = int.from_bytes(sampl_rate_in_bytes, byteorder='little')

# амплитуда сигнала в разные моменты времени
music_amps = []

for i in range(0,audio_data_size, 2):
    amp_in_bytes = data[44+i:44+i+2]
    amp = int.from_bytes(amp_in_bytes, byteorder= 'little', signed=True)
    music_amps.append(amp)

# xdata = range(0, len(music_amps)/sampl_rate, len(music_amps))
xdata = np.linspace(0, len(music_amps)/sampl_rate, len(music_amps))

spectre = np.fft.fft(music_amps)
abs_spectre = abs(spectre)

# plt.plot(xdata, music_amps)
# plt.show()

plt.plot(xdata, abs_spectre)
plt.show()

pass