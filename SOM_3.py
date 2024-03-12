## Author: Liam Decaster
## Date: 12.03.2024

import numpy as np
import scipy.optimize as optimize
from scipy.optimize import Bounds
from scipy.stats import norm

sigma1 = 2
c = 30
r2 = 85

## Preisfunktion
def mu1(r1):
    mu = 30 - 0.2 * r1
    return mu
def umsatzfunktion(r1):
    g1 = np.round(norm(mu1(r1), sigma1).ppf(1-r2/r1), 0)
    #g1 = mu1(r1)
    umsatz = g1 * r1 + r2 * (c - g1)
    return umsatz * (-1)

bounds = Bounds([86], [150])


result = optimize.minimize(umsatzfunktion, [42], bounds=bounds)

print("Optimaler Preis: ", np.round(result.x, 2), "CHF")

