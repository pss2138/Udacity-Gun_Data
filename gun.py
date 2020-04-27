import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_gun = pd.read_excel('gun_data.xlsx')
df_gun.to_csv('gun_data.csv', index=True, header=True)
df_census = pd.read_csv('census_data.csv')