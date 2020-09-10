import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

Year = [2001,2002,2003,2004,2005,2006,2007]

Revenue = [10,15,9,5,20,30,40]


barColors = ['#034694','#001C58','#5CBFEB','#D00027', '#EF0107','#DA020E']
pl.bar(x = Year, height =Revenue, color=barColors)

pl.xticks(Year)
pl.xlabel("Year")
pl.ylabel("Revenue")
pl.title("Bar Chart displaying revenues from 2001-2007")






pl.show()