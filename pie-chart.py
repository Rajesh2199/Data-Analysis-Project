import pandas as pd
import matplotlib.pyplot as pl


macros = {'Names':['Protein', 'Fats' , 'Carbohydrates'],
'Portion':[40, 20, 40]}

df = pd.DataFrame(macros, columns=['Names', 'Portion'])



pl.pie(df['Portion'])
pl.tight_layout()