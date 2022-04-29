import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy.fftpack
import xarray as xr
import joblib
import pandas as pd



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

def ecg_to_metrics(ecg, srate, show = False):
    ecg = -ecg
    if show:
        plt.figure(figsize=(15,10))
        ecg_signals, info_ecg = nk.ecg_process(ecg, sampling_rate=srate, method='neurokit')
        nk.ecg_plot(ecg_signals, rpeaks=info_ecg, sampling_rate=srate, show_type='default')
    
    clean = nk.ecg_clean(ecg, sampling_rate=srate, method='neurokit')
    peaks, info_ecg = nk.ecg_peaks(clean, sampling_rate=srate,method='neurokit', correct_artifacts=True)
    
    R_peaks = info_ecg['ECG_R_Peaks'] # get R time points
    metrics = nk.hrv(R_peaks, sampling_rate=1000, show=False, **kwargs)
    diff_R_peaks = np.diff(R_peaks) 
    x = vector_time
    xp = R_peaks[1::]/srate
    fp = diff_R_peaks
    interpolated_hrv = np.interp(x, xp, fp, left=None, right=None, period=None) / srate
    fci = 60 / interpolated_hrv
    return metrics