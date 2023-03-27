# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display

# Global variables.
size = 1000

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

def optimize(df, size):
    # Grab values from the input DataFrame.
    recyclability = np.array(df['Recyclability'])
    cost = np.array(df['Cost'])
    value = np.array(df['Market Value'])
    
    # Create fractional make-up arrays.
    polyester_makeup = np.linspace(0, 1, size)
    polypropelene_makeup = 1 - np.linspace(0, 1, size)
    
    # Initial values.
    max_recycle = 0
    min_cost = 0
    amount_of_polyester = 0
    amount_of_polypropelene = 0
    
    # Iterate to optimize.
    for i in range(size):
        temp_recycle = polyester_makeup[i]*recyclability[0] + polypropelene_makeup[i]*recyclability[1]
        temp_cost = (polyester_makeup[i]*cost[0] + polypropelene_makeup[i]*cost[1]) - (polyester_makeup[i]*value[0] + polypropelene_makeup[i]*value[1])
        
        if i == 1:
            max_recycle = temp_recycle
            min_cost = temp_cost
            amount_of_polyester = polyester_makeup[i] 
            amount_of_polypropelene = polypropelene_makeup[i] 
        
        elif temp_recycle > max_recycle and temp_cost < min_cost:
            max_recycle = temp_recycle
            min_cost = temp_cost
            amount_of_polyester = polyester_makeup[i] 
            amount_of_polypropelene = polypropelene_makeup[i] 
      
    # Print out optimized values.
    print('The maximum recylability that can be achieved for the carpet backing when using the mechanical separation method of beating is {}.\n'.format(max_recycle))
    print('The associated minimum cost that can be achieved for the carpet backing when using the mechanical separation method of beating is {}.\n'.format(min_cost))
    print('The make-up of this carpet backing is {} of polyester and {} of polypropelene.\n'.format(amount_of_polyester, amount_of_polypropelene))

    return [max_recycle, min_cost, amount_of_polyester, amount_of_polypropelene]

beating_backing_optimized = optimize(df_beating_backing, size)
