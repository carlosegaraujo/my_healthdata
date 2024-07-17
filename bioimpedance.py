# Program: bioimpedance.py / Run: "python3 bioimpedance.py"
# Objective: Tabulate bioimpedqance data from gym activities
# Source:
# https://sparkbyexamples.com/pandas/pandas-empty-dataframe-with-specific-column-types/
# Author: Carlos E.G. Araujo
# Created: 31-Mar-2023 - Last Update: 16-Jul-2024
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import time
#
start_time = time.time() # Start timer - source: https://ibit.ly/f4Yby
# 
# Create empty dataframe
#
df = pd.DataFrame({'Data': pd.Series(dtype='str'),
                   'Peso': pd.Series(dtype='float'),
                   'IMC': pd.Series(dtype='float'),
                   'PctGord': pd.Series(dtype='float'),
                   'PctMassMagra': pd.Series(dtype='float'),
                   'IdadeCorpo': pd.Series(dtype='int'),
                   'PctGordVisc': pd.Series(dtype='float'),})
#
# Insert values on dataframe. Source:
# https://stackoverflow.com/questions/16597265/appending-to-an-empty-dataframe-in-pandas
# Attention: The frame.append method is deprecated and will be removed
# from pandas in a future version. Use pandas.concat instead.
#
new_row = pd.DataFrame([{'Data': '11/04/2023', 'Peso': 87.5, 'IMC': 29.2, 'PctGord': 24.2,
                'PctMassMagra': 35.2 , 'IdadeCorpo': 60, 'PctGordVisc': 13}])
df = pd.concat([df,new_row],ignore_index=True)
#
new_row = pd.DataFrame([{'Data': '12/06/2023', 'Peso': 88.3, 'IMC': 29.5, 'PctGord': 23.4,
                'PctMassMagra': 35.6 , 'IdadeCorpo': 61, 'PctGordVisc': 14}])
df = pd.concat([df,new_row],ignore_index=True)
#
new_row = pd.DataFrame([{'Data': '06/11/2023', 'Peso': 81.9, 'IMC': 27.4, 'PctGord': 19.2,
                'PctMassMagra': 37.8 , 'IdadeCorpo': 54, 'PctGordVisc': 11}])
df = pd.concat([df,new_row],ignore_index=True)
#
new_row = pd.DataFrame([{'Data': '29/01/2024', 'Peso': 79.5, 'IMC': 26.6, 'PctGord': 12.4,
                'PctMassMagra': 41.3 , 'IdadeCorpo': 52, 'PctGordVisc': 9}])
df = pd.concat([df,new_row],ignore_index=True)
#
new_row = pd.DataFrame([{'Data': '16/07/2024', 'Peso': 81.5, 'IMC': 27.2, 'PctGord': 12.8,
                'PctMassMagra': 41.1 , 'IdadeCorpo': 54, 'PctGordVisc': 10}])
df = pd.concat([df,new_row],ignore_index=True)
#
print(df)
#
print("\nEnd of process in: %4.5f seconds ---\n" % (time.time() - start_time))
#