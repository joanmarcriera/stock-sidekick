import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('/Users/mriera/repos/stock/first/graph/SPY_D.csv', sep=',')
#df.ta.mp = True #to enable multiprocessing. This computer has 4 cores. Default: False

# Calculate Returns and append to the df DataFrame
df.ta.log_return(cumulative=True, append=True)
df.ta.percent_return(cumulative=True, append=True)

# New Columns with results
df.columns

# vv Continue Post Processing vv

# Running the Builtin CommonStrategy as mentioned above
df.ta.strategy(ta.CommonStrategy)

# The Default Strategy is the ta.AllStrategy. The following are equivalent
# df.ta.strategy(ta.AllStrategy)
# df.ta.strategy(name="All")
df.ta.strategy()


# Take a peek
df.tail()
df.plot()
plt.show()

import time

time.sleep (30)
