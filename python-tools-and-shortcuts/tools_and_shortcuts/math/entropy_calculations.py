#
# Load useful libraries
#
from collections import Counter
from scipy.stats import entropy
import numpy as np

#
# Given a list of strings, calculate the entropy of the list
# based on list item frequency.
#
def calculate_list_entropy(
    str_list: list,
    base : float = 2.,  # base 2 reports the units in bits
) -> np.float64 | None:

    """Given a list of strings, calculates the entropy of the list
    based on the frequency of the strings contained in the list."""
    
    ent = None
    
    if not isinstance(str_list, list):  return None
    if len(str_list) == 0:  return None
    
    counts = Counter(str_list)
    frequencies = list(counts.values())
    ent = entropy(frequencies, base = 2)
    
    return ent
