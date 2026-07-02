#
# Because I always forget these equations and
# never want to look them up again...
#

#
# load useful libraries
#
import numpy as np
from .config.precision_config import float_tse


def get_period_in_seconds_from_frequency_in_hertz(frequency : float_tse) -> float_tse:
    return 1. / frequency

def get_frequency_in_hertz_from_period_in_seconds(period : float_tse) -> float_tse:
    return 1. / period

def get_sinusoidal_period_from_frequency_in_hertz(frequency : float_tse) -> float_tse:
    return frequency * 2. * np.pi

#
# more formal means of testing will be produced later
#
def main():
    frequency = 440. # A4 - Tuning standard pitch - ISO16

    assert np.round(get_period_in_seconds_from_frequency_in_hertz(frequency), 6) == 0.002273

    assert int( get_frequency_in_hertz_from_period_in_seconds( get_period_in_seconds_from_frequency_in_hertz(frequency) ) ) == int(frequency)

    #
    # test the sinusoidal calculation
    #

    # https://dsp.stackexchange.com/questions/53125/write-a-440-hz-sine-wave-to-wav-file-using-python-and-scipy
    from scipy.io import wavfile
    wav_file_path = 'Sine.wav'
    sampleRate = 48000
    frequency = 440
    length = 10
    t = np.linspace(0, length, sampleRate * length)  #  Produces a 5 second Audio-File
    y = np.sin(get_sinusoidal_period_from_frequency_in_hertz(frequency) * t)
    m = np.max(np.abs(y))
    maxint16 = np.iinfo(np.int16).max  # == 2**15-1
    y = maxint16 * y / m
    y = y.astype(np.int16) 

    # From Google AI resulting from the search "python load a wave file and find dominant frequency" (with minor modification on my part)
    from scipy.fft import fft, fftfreq
    N = len(y)  # Number of samples
    yf = fft(y)
    xf = fftfreq(N, 1 / sampleRate)
    positive_frequencies_indices = np.where(xf >= 0)
    positive_frequencies = xf[positive_frequencies_indices]
    magnitudes = np.abs(yf[positive_frequencies_indices])
    dominant_frequency_index = np.argmax(magnitudes)
    dominant_frequency = positive_frequencies[dominant_frequency_index]

    assert int(dominant_frequency) == int(frequency)
    
if __name__ == '__main__':
    main()
