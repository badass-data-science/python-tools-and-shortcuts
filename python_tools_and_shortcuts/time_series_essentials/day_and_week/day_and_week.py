import numpy as np

from time_series_essentials.time_conversions import seconds_in_one_day
from time_series_essentials.time_conversions import seconds_in_one_week
from time_series_essentials.freq_and_period import get_frequency_in_hertz_from_period_in_seconds
from time_series_essentials.freq_and_period import get_sinusoidal_period_from_frequency_in_hertz

def day_sin(t):
    freq_day = get_frequency_in_hertz_from_period_in_seconds(seconds_in_one_day)
    omega_day = get_sinusoidal_period_from_frequency_in_hertz(freq_day)
    return np.sin(omega_day * t)

def day_cos(t):
    freq_day = get_frequency_in_hertz_from_period_in_seconds(seconds_in_one_day)
    omega_day = get_sinusoidal_period_from_frequency_in_hertz(freq_day)
    return np.cos(omega_day * t)

def week_sin(t):
    freq_week = get_frequency_in_hertz_from_period_in_seconds(seconds_in_one_week)
    omega_week = get_sinusoidal_period_from_frequency_in_hertz(freq_week)
    return np.sin(omega_week * t)

def week_cos(t):
    freq_week = get_frequency_in_hertz_from_period_in_seconds(seconds_in_one_week)
    omega_week = get_sinusoidal_period_from_frequency_in_hertz(freq_week)
    return np.cos(omega_week * t)
