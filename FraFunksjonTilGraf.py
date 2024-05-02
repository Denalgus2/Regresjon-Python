import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 2  #skriv funksjon inn her

x_verdier = np.linspace(-10, 10, 100)  # lager 100 x-verdier fra -10 til 10
y_verdier = f(x_verdier)  # regner ut y-verdier for x-verdiene

plt.plot(x_verdier, y_verdier)  # plotter x-verdiene mot y-verdiene
plt.show()  # viser plottet