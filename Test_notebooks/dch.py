#%%
# Importing numpy and creating two arrays
import numpy as np


#%%
# Creating two numpy arrays
a = np.array([1, 2, 3])  # First array with values 1, 2, 3
b = np.array([4, 5, 6])  # Second array with values 4, 5, 6


# %% [markdown]
# # Adding the Two Arrays
#
# This operation performs element-wise addition. In mathematical terms, this can be expressed as:
#
# $$c = a + b$$
#
# where:
# - \( a = [1, 2, 3] \)
# - \( b = [4, 5, 6] \)
#
# The resulting array \( c \) is computed as follows:
#
# $$c = [a_1 + b_1, a_2 + b_2, a_3 + b_3]$$
#
# Substituting the values:
#
# $$c = [1 + 4, 2 + 5, 3 + 6] = [5, 7, 9]$$
#
# This result can also be interpreted in terms of vector addition, where each corresponding element of the vectors \( a \) and \( b \) is added together.

#%%
# Example of a simple arithmetic operation
1 + 1  # This will return 2
