# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
x = np.arange (-2.1, 3.1,0.001)
plt.plot (x, (x*x-x-6))
plt.grid(True)
plt.show()