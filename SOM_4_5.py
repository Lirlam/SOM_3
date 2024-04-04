from scipy.stats import norm
import numpy as np


def emsr_a_analysis(r, mu, sigma, C):
    num_classes = len(r)

    G_values = []
    B_values = []

    for i in range(num_classes - 1):
        G = 0
        for j in range(i + 1):
            demand = np.round(norm(mu[j], sigma[j]).ppf(min(1 - r[i] / r[j], 0.999)), 0)
            G += demand if demand >= 0 else 0  # Ensure demand is non-negative
        G_values.append(G)
        B_values.append(C - G)

    # Letzte Klasse verwendet die gesamte Kapazität
    G_values.append(C)
    B_values.append(0)

    return G_values, B_values


r = [300, 200, 100, 50, 25]  # geordnete Einnahmen pro Klasse
mu = [10, 15, 25, 50, 500]  # geordnete Mittelwerte der Nachfrage
sigma = [2, 2, 3, 3, 5]  # geordnete Standardabweichungen der Nachfrage
C = 160  # Kapazität

G_values, B_values = emsr_a_analysis(r, mu, sigma, C)

for i in range(len(G_values)):
    print("G{}: {}".format(i + 1, G_values[i]))

for i in range(len(B_values)):
    print("B{}: {}".format(i + 1, B_values[i]))
