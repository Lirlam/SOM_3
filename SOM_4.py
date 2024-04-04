from scipy.stats import norm
import numpy as np

# EMSR-a mit 4 Klassen
r = [120, 100, 90, 60]  # Einnahmen pro Klasse
mu = [1000, 2000, 18000, 21000]  # Mittelwerte der Nachfrage
sigma = [800, 600, 2000, 1000]  # Standardabweichungen der Nachfrage
C = 21000  # Kapazität

# Berechnung für G3 und B3
G_4_1 = np.round(norm(mu[0], sigma[0]).ppf(1 - r[3] / r[0]), 0)
G_4_2 = np.round(norm(mu[1], sigma[1]).ppf(1 - r[3] / r[1]), 0)
G_4_3 = np.round(norm(mu[2], sigma[2]).ppf(1 - r[3] / r[2]), 0)
G3 = G_4_1 + G_4_2 + G_4_3
B4 = C - G3

# Berechnung für G2 und B2
G_4_1 = np.round(norm(mu[0], sigma[0]).ppf(1 - r[2] / r[0]), 0)
G_4_2 = np.round(norm(mu[1], sigma[1]).ppf(1 - r[2] / r[1]), 0)
G2 = G_4_1 + G_4_2
B3 = C - G2

# Berechnung für G1 und B1
G1 = np.round(norm(mu[0], sigma[0]).ppf(1 - r[1] / r[0]), 0)
B2 = C - G1
B1 = C

# Ausgabe der Ergebnisse
print("G1: {}".format(G1))
print("G2: {}".format(G2))
print("G3: {}".format(G3))
print("G4: {}".format(C))  # Da die vierte Klasse die volle Kapazität verwendet
print("B1: {}".format(B1))
print("B2: {}".format(B2))
print("B3: {}".format(B3))
print("B4: {}".format(B4))
