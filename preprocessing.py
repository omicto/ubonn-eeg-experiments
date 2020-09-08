import numpy as np
import matplotlib.pyplot as plt
import reading
import random
import math
from scipy.signal import butter, lfilter, freqz, firwin
from scipy.fft import fft, fftfreq

def reshape_signal(raw_signal):
    return reading.segment_data(raw_signal[0:data_length], timesteps, data_dim)

data_length = 4096 # d
timesteps = 2048
data_dim = data_length//timesteps # L
srate = 173.61

# Leer los datitos
#  Aplicarles lo de los ojos
#  Aplicarles lo de los musculos
#  Aplicarle ruido shoper
# guardar cada una de esas cosas

def gaussian_noise(length, strength = 1):
    return np.random.normal(0,1,length) * strength

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def pos_gen(window_shape, blanc_shape, max_pos, start=0):
    min_window, max_window = window_shape
    min_blanc, max_blanc = blanc_shape
    end = 0
    while end < max_pos:
        h = random.randint(min_window, max_window)
        final = start + h
        end = final if final < max_pos else max_pos
        res = (start, end)
        blanc = random.randint(min_blanc,max_blanc)
        start = end + blanc
        yield res

def apply_window(signal, window_shape, blanc_shape, drop=0):
    zeroes = np.zeros(signal.shape)
    min_window, max_window = window_shape
    start = -random.randint(min_window, max_window) # Ojo con la negacion
    gen = pos_gen(window_shape, blanc_shape, signal.shape[0]-1, start)
    for start, end in gen:
        if drop and decide(drop/100):
            continue
        zeroes[start:end] = signal[start:end]
    return zeroes

def filtered_noise(length, lowcut, highcut, noise_strength):
    noise = gaussian_noise(length, strength=noise_strength)
    filtered = butter_bandpass_filter(noise, lowcut, highcut, srate)
    return filtered

second = math.floor(srate)
hundred_ms = second//10

def eyes(signal, noise_strength=50):
    noise = filtered_noise(len(signal), 1, 3, noise_strength)
    window = (7*hundred_ms, 14*hundred_ms)
    blanc = (second, 4*second)
    noise = apply_window(noise, window, blanc)
    return signal + noise

def muscles(signal, noise_strength=30):
    noise = filtered_noise(len(signal), 20, 60, noise_strength)
    window = (7*hundred_ms, 7*hundred_ms)
    blanc = (second, 4*second)
    noise = apply_window(noise, window, blanc, drop=75)
    return signal + noise

def white_noise(signal, noise_strength=50):
    noise = gaussian_noise(len(signal), strength=noise_strength)
    return signal + noise

def decide(probability):
    return random.random() < probability
