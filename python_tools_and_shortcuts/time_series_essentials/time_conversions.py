import numpy as np

seconds_in_one_hour = np.float64(60. * 60.)

# we ignore the rare case of leap seconds
seconds_in_one_day = seconds_in_one_hour * 24.

seconds_in_one_week = seconds_in_one_day * 7.

#
# more formal means of testing will be produced later
#
def main():
    assert int(seconds_in_one_hour) == 3600
    assert int(seconds_in_one_day) == 86400
    assert int(seconds_in_one_week) == 604800
    assert type(seconds_in_one_day) == np.float64
    assert type(seconds_in_one_week) == np.float64

if __name__ == '__main__':
    main()
