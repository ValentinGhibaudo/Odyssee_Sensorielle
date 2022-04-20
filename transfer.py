"""Transfer functions"""

# Working voltage
VCC = 3.3


def ECG(signal, resolution=10):
    """ECG value in millivolt [-1.5𝑚𝑉, 1.5𝑚𝑉]"""
    return (((signal / 2 ** resolution) - 0.5) * VCC) / 1100 * 1000


def EMG(signal, resolution=10):
    """EMG value in millivolt [-1.64𝑚𝑉, 1.64𝑚𝑉]"""
    return (((signal / 2 ** resolution) - 0.5) * VCC) / 1009 * 1000


def EDA(signal, resolution=10):
    """EDA value in microsiemens [0𝜇𝑆, 25𝜇𝑆]"""
    return ((signal / 2 ** resolution) * VCC) / 0.132


def EEG(signal, resolution=10):
    """EEG value in microvolts [-39.49𝜇𝑉, 39.49𝜇𝑉]"""
    return (((signal / 2 ** resolution) - 0.5) * VCC) / 41782 * 1e6


def PZT(signal, resolution=10):
    """EEG value in percents [-50%, 50%]"""
    return ((signal / 2 ** resolution) - 0.5) * 100
