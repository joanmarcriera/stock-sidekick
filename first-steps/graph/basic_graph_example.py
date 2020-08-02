#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
#style.use('dark_background')

d = {'x' : [1,2,3,4,5,6,7,8,9,10],
     'y_one' : [10,11,12,13,14,15,16,17,18,19],
     'y_two' : [20,21,22,23,24,25,26,27,28,29]}

df = pd.DataFrame(d)

df.plot('x',y=['y_one','y_two'])
plt.show()
