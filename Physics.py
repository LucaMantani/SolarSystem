import numpy as np
from itertools import combinations


def distance(p1, p2):
    """
    Function that takes two planets and returns their
    euclidean distance.
    """
    d = np.linalg.norm(p1.position - p2.position)
    return d


def rVersor(p1, p2):
    """
    Function that takes two planets and returns
    the distance versor
    """
    d = p1.position - p2.position
    return d/np.linalg.norm(d)


class Gravity(object):
    """
    This class implements Newtonian gravity.
    """

    def __init__(self):
        # Definition of G in AU^3 yr^-2 Mo^-1
        self.G = 39.478

        # time step in years (1 day)
        self.dt = 1/365.0/2.0

    def g(self, p1, p2):
        """
        Returns the force of gravity.
        """
        return self.G * (p1.mass * p2.mass)/(distance(p1, p2)**2) * rVersor(p1, p2)

    def timestep(self, planets):
        """
        Modifies position and velocity of the planets
        according to Newton's gravitation law.
        """
        planet_pairs = list(combinations(planets, 2))

        for p1, p2 in planet_pairs:
            p1.velocity += -self.g(p1, p2)/p1.mass * self.dt
            p2.velocity += -self.g(p2, p1)/p2.mass * self.dt

        for p in planets:
            p.position += p.velocity * self.dt
