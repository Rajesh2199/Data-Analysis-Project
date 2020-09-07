import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

Year = [2001,2002,2003,2004,2005,2006,2007]

Revenue = [10,15,9,5,20,30,40]

# bar argument plots data. 

pl.bar(Year, Revenue)

pl.xticks( Year)
pl.xlabel("Year")
pl.ylabel("Revenue")
pl.title("Dummy Chart")

pl.show()