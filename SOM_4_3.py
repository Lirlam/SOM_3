# documentation scipy.stats.norm: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html
from scipy.stats import norm
import numpy as np
# EMSR a mit 3 Klassen
r = [300, 100, 50]  # Einnahmen pro Klasse
mu = [35, 25, 500]  # Mittelwerte der Nachfrage
sigma = [2, 2, 2]  # Standardabweichungen der Nachfrage
C = 160  # Kapazität
# Werte für G2
G_3_1 = np.round(norm(mu[0], sigma[0]).ppf(1-r[2]/r[0]),0)
G_3_2 = np.round(norm(mu[1], sigma[1]).ppf(1-r[2]/r[1]),0)
G2 = G_3_1 + G_3_2
B3 = C - G2

G1 = np.round(norm(mu[0], sigma[0]).ppf(1-r[1]/r[0]),0)  #ppf=percent point function (inverse of cumulative distribution function)
B2 = C-G1
B1 = C
G3 = C
print("G1: {}".format(G1))
print("G2: {}".format(G2))
print("G3: {}".format(G3))
print("B1: {}".format(B1))
print("B2: {}".format(B2))
print("B3: {}".format(B3))