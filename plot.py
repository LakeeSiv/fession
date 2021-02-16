import matplotlib.pyplot as plt
import sqlite3
from scipy.stats import norm
import matplotlib.mlab as mlab
import numpy as np
from scipy.optimize import curve_fit


bins = 50

conn = sqlite3.connect("realoxfess.db")
c = conn.cursor()

a = (c.execute("""SELECT sentiment FROM posts""")).fetchall()
a = [round(i[0],5) for i in a]


def gaussian(x, mean, amplitude, standard_deviation):
    return amplitude * np.exp( - ((x - mean) / standard_deviation) ** 2)

x = np.random.normal(10, 5, size=10000)

bin_heights, bin_borders, _ = plt.hist(a, bins='auto', label='histogram')
bin_centers = bin_borders[:-1] + np.diff(bin_borders) / 2
popt, _ = curve_fit(gaussian, bin_centers, bin_heights, p0=[1., 0., 1.])

mu = popt[0]
sigma = popt[2]

x_interval_for_fit = np.linspace(bin_borders[0], bin_borders[-1], 10000)
plt.plot(x_interval_for_fit, gaussian(x_interval_for_fit, *popt), label='fit')
plt.title(f"Gaussian Distribution $\mu={mu},\sigma={sigma}$")
plt.legend()
plt.show()