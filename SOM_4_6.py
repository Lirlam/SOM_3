from scipy.stats import norm
import numpy as np


def emsr_b_analysis(r, mu, sigma, C):
    num_classes = len(r)

    Schutzgrenzen = [0] * num_classes
    Buchungsgrenzen = [0] * num_classes

    for i in range(num_classes):
        Schutzgrenze = mu[i] + sigma[i] * norm.ppf(1 - r[i] / sum(r[:i + 1]))
        Schutzgrenzen[i] = max(0, Schutzgrenze)

    Buchungsgrenzen[0] = min(C, Schutzgrenzen[0])
    for i in range(1, num_classes):
        Buchungsgrenzen[i] = min(C, Schutzgrenzen[i] - sum(Buchungsgrenzen[:i]))

    return Schutzgrenzen, Buchungsgrenzen


r = [500, 400, 200, 100, 50, 25]  # geordnete Einnahmen pro Klasse
mu = [4, 8, 15, 25, 50, 500]  # geordnete Mittelwerte der Nachfrage
sigma = [2, 2, 4, 10, 20, 50]  # geordnete Standardabweichungen der Nachfrage
C = 200  # Kapazität

Schutzgrenzen, Buchungsgrenzen = emsr_b_analysis(r, mu, sigma, C)

print("Schutzgrenzen:", Schutzgrenzen)
print("Buchungsgrenzen:", Buchungsgrenzen)
