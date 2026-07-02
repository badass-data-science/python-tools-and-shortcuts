import numpy as np
from scipy.fft import fft, fftfreq
from config.precision_config import float_tse

#
# From Google AI resulting from the search "python load a wave file and find dominant frequency" (with minor modification on my part)
#
def calculate_dominant_frequency(y : np.array, sample_rate_in_hertz : float_tse = 48000.) -> float_tse:

    # need some way to ensure each element of y is of type "float_tse"
    
    N = len(y)  # Number of samples
    yf = fft(y)
    xf = fftfreq(N, 1 / sample_rate_in_hertz)
    positive_frequencies_indices = np.where(xf >= 0)
    positive_frequencies = xf[positive_frequencies_indices]
    magnitudes = np.abs(yf[positive_frequencies_indices])
    dominant_frequency_index = np.argmax(magnitudes)
    dominant_frequency = positive_frequencies[dominant_frequency_index]
    return float_tse(dominant_frequency)

