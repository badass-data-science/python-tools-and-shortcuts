import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

class FuzzyInterpolator():

    #
    # Constructor
    #
    def __init__(
        self,
        list_increasingly_ordered_set_names : list,
        dict_ranges : dict,
        step = 0.001,
    ):
        # initialize instance variables from the arguments
        self.list_ordered_set_names = list_increasingly_ordered_set_names
        self.dict_ranges = dict_ranges

        # used to get the minimum and maximum values of dict_ranges
        def get_min_and_max(dict_of_lists):
            the_min = np.nan
            the_max = np.nan
            for key in dict_of_lists.keys():
                key_min = np.nanmin(dict_of_lists[key])
                key_max = np.nanmax(dict_of_lists[key])
                the_min = np.nanmin([the_min, key_min])
                the_max = np.nanmax([the_max, key_max])
            return float(the_min), float(the_max)

        # calculate the domain
        self.min_to_use, self.max_to_use = get_min_and_max(self.dict_ranges)
        self.domain = np.arange(self.min_to_use, self.max_to_use + step, step)

        # generate the membership functions
        self.create_membership_functions()

    #
    # Create membership functions from the content of self.dict_ranges
    #
    def create_membership_functions(self):

        self.dict_mf = {}
        for set_name in self.list_ordered_set_names:
            range_x = self.dict_ranges[set_name]

            if len(range_x) == 2:
                if set_name == self.list_ordered_set_names[0]:
                    self.dict_mf[set_name] = fuzz.zmf(self.domain, range_x[0], range_x[1])
                elif set_name == self.list_ordered_set_names[-1]:
                    self.dict_mf[set_name] = fuzz.smf(self.domain, range_x[0], range_x[1])
                else:
                    # deal with this error later
                    assert 0 == 1
        
            elif len(range_x) == 3:
                self.dict_mf[set_name] = fuzz.trimf(self.domain, range_x)

            else:
                # deal with this error later
                assert 0 == 1

    #
    # Given a value, interpolate its membership in each set
    #
    def interpolate_membership(self, value_to_interpolate):

        #
        # calculate the range to return
        #
        report_range_min = np.min([value_to_interpolate, self.min_to_use])
        report_range_max = np.max([value_to_interpolate, self.max_to_use])
        
        #
        # deal with extreme values
        #
        if value_to_interpolate < self.min_to_use:
            value_to_interpolate = self.min_to_use
        if value_to_interpolate > self.max_to_use:
            value_to_interpolate = self.max_to_use

        #
        # initialize return object
        #
        dict_interpolated_membership = {
            'fuzzy set membership' : {},
            'value range' : {
                'minimum' : float(report_range_min),
                'maximum' : float(report_range_max),
            },
        }
            
        #
        # compute degree of set membership
        #
        for set_name in self.list_ordered_set_names:
            dict_interpolated_membership['fuzzy set membership'][set_name] = float(
                fuzz.interp_membership(self.domain, self.dict_mf[set_name], value_to_interpolate)
            )
            
        return dict_interpolated_membership

    #
    # create a plot of the membership functions
    #
    def plot_membership_functions(self, title = 'Membership Functions', xlabel = 'Domain'):
        plt.figure()
        for set_name in self.list_ordered_set_names:
            x = self.dict_ranges[set_name]

            if len(x) == 2:
                if set_name == self.list_ordered_set_names[0]:
                    y = np.array([1., 0.])
                elif set_name == self.list_ordered_set_names[-1]:
                    y = np.array([0., 1.])
                else:
                    # deal with this error later
                    assert 0 == 1
        
            if len(x) == 3:
                y = np.array([0., 1., 0.])

            plt.plot(x, y, label = set_name)

        plt.legend()
        plt.xlabel(xlabel)
        plt.ylabel('Membership')
        plt.title(title)
        plt.show()
        plt.close()
