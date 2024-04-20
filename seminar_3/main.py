import matplotlib.pyplot as plt
import numpy as np
import copy
from math import ceil

class Audio_Item():
    def __init__(self,filename:str) -> None:
        fileobj =  open(filename , mode="rb")
        filedata = fileobj.read()
        fileobj.close()

        # размер файла
        file_size_inbytes = filedata[4:8]
        self.file_size = int.from_bytes(file_size_inbytes, byteorder= 'little')

        # колличество каналов
        num_of_channel_in_inbytes = filedata[22:24]
        self.num_of_channel = int.from_bytes(num_of_channel_in_inbytes, byteorder= 'little')

        # значение аудио файла в байтах
        audio_data_size_in_inbytes = filedata[40:44]
        self.audio_data_size = int.from_bytes(audio_data_size_in_inbytes, byteorder= 'little')

        # частота дикретизации
        sampl_rate_in_bytes = filedata[24:28]
        self.sampl_rate = int.from_bytes(sampl_rate_in_bytes, byteorder='little')

        # амплитуды сигнала
        music_amps = []
        for i in range(0,self.audio_data_size, 2):
            amp_in_bytes = filedata[44+i:44+i+2]
            amp = int.from_bytes(amp_in_bytes, byteorder= 'little', signed=True)
            music_amps.append(amp)
        
        # количество отсчётов сигнала
        self.num_of_samples = len(music_amps)

        # осциллограмма сигнала
        self.osc_data = copy.copy(music_amps)
        self.time_scale = np.arange(0,self.num_of_samples/self.sampl_rate, 1/self.sampl_rate)

        # спектр мощности сигнала
        self.spectre_data = abs(np.fft.fft(music_amps))**2
        self.freqs_scale = np.fft.fftfreq(self.time_scale.size, 1/self.sampl_rate)
    
    def __str__(self) -> str:
        return str(self.__dict__)

my_audio = Audio_Item("seminar_3/1kHz_44100Hz_16bit_05sec.wav")


plt.plot(my_audio.time_scale,my_audio.osc_data)
plt.show()

plt.plot(my_audio.freqs_scale[0:ceil(my_audio.num_of_samples/2)], my_audio.spectre_data[0:ceil(my_audio.num_of_samples/2)])
plt.show()

pass