import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

Year = [2001,2002,2003,2004,2005,2006,2007]

Revenue = [10,15,9,5,20,30,40]

# bar argument plots data. 

pl.bar(x=np.arange(1,21),height=['Revenue'])

pl.show()