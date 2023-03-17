# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Different DataFrames for each recycling process.

# Fiber Materials
# Mechanical Recycling - Beating
df_beating_fiber = pd.DataFrame({'Material': ['Polyester', 'Polypropelene', 'Nylon 6', 'Nylon 66'], 'Recyclability': [1, 2, 3, 4], 'Cost': [1, 2, 3, 4], 'Market Value': [1, 2, 3, 4]})

# Mechanical Recycling - Shearing
df_shearing_fiber = pd.DataFrame({'Material': ['Polyester', 'Polypropelene', 'Nylon 6', 'Nylon 66'], 'Recyclability': [1, 2, 3, 4], 'Cost': [1, 2, 3, 4], 'Market Value': [1, 2, 3, 4]})

# Mechanical Recycling - Separation
df_separation_fiber = pd.DataFrame({'Material': ['Polyester', 'Polypropelene', 'Nylon 6', 'Nylon 66'], 'Recyclability': [1, 2, 3, 4], 'Cost': [1, 2, 3, 4], 'Market Value': [1, 2, 3, 4]})

# Chemical Recycling - Nylon Depolymerization
df_ndpoly_fiber = pd.DataFrame({'Material': ['Polyester', 'Polypropelene', 'Nylon 6', 'Nylon 66'], 'Recyclability': [1, 2, 3, 4], 'Cost': [1, 2, 3, 4], 'Market Value': [1, 2, 3, 4]})

# Chemical Recycling - Formic Acid Dissolution
df_fadiss_fiber = pd.DataFrame({'Material': ['Polyester', 'Polypropelene', 'Nylon 6', 'Nylon 66'], 'Recyclability': [1, 2, 3, 4], 'Cost': [1, 2, 3, 4], 'Market Value': [1, 2, 3, 4]})

# Backing Materials
# Mechanical Recycling - Beating
df_beating_backing = pd.DataFrame({'Material': ['Polyester', 'Polypropelene'], 'Recyclability': [1, 2], 'Cost': [1, 2], 'Market Value': [1, 2]})

# Mechanical Recycling - Shearing
df_shearing_backing = pd.DataFrame({'Material': ['Polyester', 'Polypropelene'], 'Recyclability': [1, 2], 'Cost': [1, 2], 'Market Value': [1, 2]})

# Mechanical Recycling - Separation
df_separation_backing = pd.DataFrame({'Material': ['Polyester', 'Polypropelene'], 'Recyclability': [1, 2], 'Cost': [1, 2], 'Market Value': [1, 2]})

# Chemical Recycling - Nylon Depolymerization
df_ndpoly_backing = pd.DataFrame({'Material': ['Polyester', 'Polypropelene'], 'Recyclability': [1, 2], 'Cost': [1, 2], 'Market Value': [1, 2]})

# Chemical Recycling - Formic Acid Dissolution
df_fadiss_backing = pd.DataFrame({'Material': ['Polyester', 'Polypropelene'], 'Recyclability': [1, 2], 'Cost': [1, 2], 'Market Value': [1, 2]})

# Functions

def optimize(fiber_length, loop_type):
    return 0