import numpy as np
import xarray as xr
import os
from matplotlib import pyplot as plt
import itertools
import numpy as np
import pandas as pd
import random
import time

from matplotlib import pyplot as plt
from matplotlib.colors import Colormap as cm
data = [ [900.399, 980.142, 0.78], [922.252, 880.885, 0.68], [724.311, 780.543, 0.58], [523.195, 582.994, 0.46], [623.431, 680.427, 0.76], [926.363, 881.791, 1.81], [722.942, 783.257, 0.75], [223.751, 279.995, 0.16], [723.215, 781.004, 0.64], [724.541, 779.889, 0.55] ]
x=[d[0] for d in data]
y=[d[1] for d in data]
t=[d[2] for d in data]
plt.contourf(x,y,t,
    cmap=)
plt.colorbar()