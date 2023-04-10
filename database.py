# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
import sqlite3

# Global variables.
size = 1000

# Different DataFrames for each recycling process.

# Fiber Materials
# Mechanical Recycling - Beating
df_beating_fiber = pd.DataFrame({'Material': ['Polyester', 'Polypropelene', 'Nylon 6', 'Nylon 66'], 
                                 'Recyclability': [1, 2, 3, 4], 
                                 'Cost': [1, 2, 3, 4], 
                                 'Market Value': [1, 2, 3, 4]})


# Mechanical Recycling - Shearing
df_shearing_fiber = pd.DataFrame({'Material': ['Polyester', 'Polypropelene', 'Nylon 6', 'Nylon 66'], 
                                  'Recyclability': [1, 2, 3, 4], 
                                  'Cost': [1, 2, 3, 4], 
                                  'Market Value': [1, 2, 3, 4]})

# Mechanical Recycling - Separation
df_rise_fiber = pd.DataFrame({'Material': ['Polyester', 'Polypropelene', 'Nylon 6', 'Nylon 66'], 
                                    'Recyclability': [1, 2, 3, 4], 
                                    'Cost': [1, 2, 3, 4], 
                                    'Market Value': [1, 2, 3, 4]})

# Chemical Recycling - Nylon Depolymerization
df_ndpoly_fiber = pd.DataFrame({'Material': ['Polyester', 'Polypropelene', 'Nylon 6', 'Nylon 66'], 
                                'Recyclability': [1, 2, 3, 4], 
                                'Cost': [1, 2, 3, 4], 
                                'Market Value': [1, 2, 3, 4]})

# Chemical Recycling - Formic Acid Dissolution
df_fadiss_fiber = pd.DataFrame({'Material': ['Polyester', 'Polypropelene', 'Nylon 6', 'Nylon 66'], 
                                'Recyclability': [1, 2, 3, 4], 
                                'Cost': [1, 2, 3, 4], 
                                'Market Value': [1, 2, 3, 4]})

# Backing Materials
# Mechanical Recycling - Beating
df_beating_backing = pd.DataFrame({'Material': ['Polyester', 'Polypropelene'], 
                                   'Recyclability': [1, 2], 
                                   'Cost': [1, 2], 
                                   'Market Value': [1, 2]})

# Mechanical Recycling - Shearing
df_shearing_backing = pd.DataFrame({'Material': ['Polyester', 'Polypropelene'], 
                                    'Recyclability': [1, 2], 
                                    'Cost': [1, 2], 
                                    'Market Value': [1, 2]})

# Mechanical Recycling - Separation
df_rise_backing = pd.DataFrame({'Material': ['Polyester', 'Polypropelene'], 
                                      'Recyclability': [1, 2], 
                                      'Cost': [1, 2], 
                                      'Market Value': [1, 2]})

# Chemical Recycling - Nylon Depolymerization
df_ndpoly_backing = pd.DataFrame({'Material': ['Polyester', 'Polypropelene'], 
                                  'Recyclability': [1, 2], 
                                  'Cost': [1, 2], 
                                  'Market Value': [1, 2]})

# Chemical Recycling - Formic Acid Dissolution
df_fadiss_backing = pd.DataFrame({'Material': ['Polyester', 'Polypropelene'], 
                                  'Recyclability': [1, 2], 
                                  'Cost': [1, 2], 
                                  'Market Value': [1, 2]})

beating = sqlite3.connect("beating.db")
df_beating_fiber.to_sql("fiber", beating, if_exists="replace")
df_beating_backing.to_sql("backing", beating, if_exists="replace")
beating.execute()

shearing = sqlite3.connect("shearing.db")
df_shearing_fiber.to_sql("fiber", shearing, if_exists="replace")
df_shearing_backing.to_sql("backing", shearing, if_exists="replace")
shearing.execute()

rise = sqlite3.connect("rise.db")
df_rise_fiber.to_sql("fiber", rise, if_exists="replace")
df_rise_backing.to_sql("backing", rise, if_exists="replace")
rise.execute()

ndpoly = sqlite3.connect("ndpoly.db")
df_ndpoly_fiber.to_sql("fiber", ndpoly, if_exists="replace")
df_ndpoly_backing.to_sql("backing", ndpoly, if_exists="replace")
ndpoly.execute()

fadiss = sqlite3.connect("fadiss.db")
df_fadiss_fiber.to_sql("fiber", fadiss, if_exists="replace")
df_fadiss_backing.to_sql("backing", fadiss, if_exists="replace")
fadiss.execute()


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
