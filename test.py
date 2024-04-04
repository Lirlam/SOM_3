
import numpy as np
import scipy.optimize as optimize
from scipy.optimize import Bounds
from scipy.stats import norm


G1 = np.round(norm(4, 2).ppf(1-0.45),3)
print(G1)