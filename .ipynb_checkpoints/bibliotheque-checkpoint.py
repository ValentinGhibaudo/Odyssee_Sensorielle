import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy.fftpack
import xarray as xr
import joblib
import pandas as pd
import mne



def norm(data):
    data = (data - np.mean(data)) / np.std(data)
    return data

def detrend(sig):
    dentrended = signal.detrend(sig)
    return dentrended

def center(sig):
    sig_centered = sig - np.mean(sig)
    return sig_centered

def time_vector(sig, srate):
    time = np.arange(0, sig.size / srate , 1 / srate)
    return time

def down_sample(sig, factor): 
    sig_down = signal.decimate(sig, q=factor, n=None, ftype='iir', axis=- 1, zero_phase=True)
    return sig_down

def spectre(sig, srate, wsize):
    nperseg = int(wsize * srate)
    nfft = nperseg * 2
    f, Pxx = signal.welch(sig, fs=srate, nperseg = nperseg , nfft = nfft, scaling='spectrum')
    # print(f.size)
    return f, Pxx

def coherence(sig1,sig2, srate, wsize):
    nperseg = int(wsize * srate)
    nfft = nperseg * 2
    f, Cxy = signal.coherence(sig1,sig2, fs=srate, nperseg = nperseg , nfft = nfft )
    # print(f.size)
    return f, Cxy

def init_da(coords, name = None):
    dims = list(coords.keys())
    coords = coords

    def size_of(element):
        element = np.array(element)
        size = element.size
        return size

    shape = tuple([size_of(element) for element in list(coords.values())])
    data = np.zeros(shape)
    da = xr.DataArray(data=data, dims=dims, coords=coords, name = name)
    return da

def parallelize(iterator, function, n_jobs):
    result = joblib.Parallel(n_jobs = n_jobs, prefer = 'threads')(joblib.delayed(function)(i) for i in iterator)
    return result

def filter_sig(sig,fs, low, high , order=1, btype = 'mne', show = False):
    
    if btype == 'bandpass':
        # Paramètres de notre filtre :
        fe = fs
        f_lowcut = low
        f_hicut = high
        nyq = 0.5 * fe
        N = order                # Ordre du filtre
        Wn = [f_lowcut/nyq,f_hicut/nyq]  # Nyquist frequency fraction

        # Création du filtre :
        b, a = signal.butter(N, Wn, btype)

        # Calcul de la reponse en fréquence du filtre
        w, h = signal.freqz(b, a)

        if show:
            # Tracé de la réponse en fréquence du filtre
            fig, ax = plt.subplots(figsize=(8,5)) 
            # ax.plot(0.5*fe*w/np.pi, np.abs(h), 'b')
            ax.semilogy(0.5*fe*w/np.pi, np.abs(h), 'b')
            ax.set_xlabel('frequency [Hz]')
            ax.set_ylabel('Amplitude [dB]')
            ax.grid(which='both', axis='both')
            plt.show()

        # Applique le filtre au signal :
        filtered_sig = signal.filtfilt(b, a, sig)
        
    elif btype == 'lowpass':
        
        # Paramètres de notre filtre :
        fe = fs
        f_hicut = high
        nyq = 0.5 * fe
        N = order                  # Ordre du filtre
        Wn = f_hicut/nyq  # Nyquist frequency fraction

        # Création du filtre :
        b, a = signal.butter(N, Wn, btype)

        # Calcul de la reponse en fréquence du filtre
        w, h = signal.freqz(b, a)

        if show:
            # Tracé de la réponse en fréquence du filtre
            fig, ax = plt.subplots(figsize=(8,5)) 
            ax.plot(0.5*fe*w/np.pi, np.abs(h), 'b')
            ax.set_xlabel('frequency [Hz]')
            ax.set_ylabel('Amplitude [dB]')
            ax.grid(which='both', axis='both')
            plt.show()

        # Applique le filtre au signal :
        filtered_sig = signal.filtfilt(b, a, sig)
        
    elif btype == 'highpass':
        
        # Paramètres de notre filtre :
        fe = fs
        f_lowcut = low
        nyq = 0.5 * fe
        N = order                  # Ordre du filtre
        Wn = f_lowcut/nyq  # Nyquist frequency fraction

        # Création du filtre :
        b, a = signal.butter(N, Wn, btype)

        # Calcul de la reponse en fréquence du filtre
        w, h = signal.freqz(b, a)

        if show:
            # Tracé de la réponse en fréquence du filtre
            fig, ax = plt.subplots(figsize=(8,5)) 
            ax.plot(0.5*fe*w/np.pi, np.abs(h), 'b')
            ax.set_xlabel('frequency [Hz]')
            ax.set_ylabel('Amplitude [dB]')
            ax.grid(which='both', axis='both')
            plt.show()

        # Applique le filtre au signal :
        filtered_sig = signal.filtfilt(b, a, sig)
        
    elif btype == 'mne':
        filtered_sig = mne.filter.filter_data(sig, sfreq=fs, l_freq = low, h_freq = high, verbose = False)
        
    elif btype == 'fir':
        
        n = order + 1
        a = signal.firwin(n=n, cutoff = low)
        
    return filtered_sig
