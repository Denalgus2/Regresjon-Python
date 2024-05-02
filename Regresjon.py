import numpy as np
import matplotlib.pyplot as plt

x_verdier = []
y_verdier = []

modell = np.poly1d(np.polyfit(x_verdier, y_verdier, 1))  # regresjonsmodell av grad 1

print(modell)

plt.plot(x_verdier, y_verdier, 'o')

x_modell = np.linspace(0,10,100)

plt.plot(x_modell, modell(x_modell))

plt.show()


