import numpy as np
from Planet import Planet
from Physics import Gravity
from Visualiser import Visualiser

planets_dict = {
    "Sun": [1, np.array([0.0, 0.0]), np.array([0.0, 0.0]), 0.2, "orange"],
    "Earth": [3e-6, np.array([1.0, 0.0]), np.array([0.0, 2*np.pi]), 0.05, "blue"],
    "Moon": [3.69432e-8, np.array([1.0 + 0.002569, 0.0]), np.array([0.0, 1.1*2*np.pi*0.002569*365]), 0.02, "grey"],
    "Mercury": [1.651e-7, np.array([0.387098, 0.0]), np.array([0.0, 2*np.pi*0.387098/0.240846]), 0.04, "green"],
    "Venus": [2.447e-6, np.array([0.723332, 0.0]), np.array([0.0, 2*np.pi*0.723332/0.615198]), 0.04, "pink"],
    "Mars": [3.213e-7, np.array([1.523679, 0.0]), np.array([0.0, 2*np.pi*1.523679/1.88085]), 0.04, "red"],
    # "Jupiter": [9.55109e-4, np.array([5.2044, 0.0]), np.array([0.0, 2*np.pi*5.2044/11.862]), 0.06, "coral"],
}

planets = [Planet(*feat, name) for name, feat in planets_dict.items()]

G = Gravity()

v = Visualiser(G, planets)

v.run()