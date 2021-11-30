import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle


class Visualiser(object):

    def __init__(self, physics, planets):
        self.planets = planets
        self.physics = physics

    def run(self):

        # Initialize figure
        figure = plt.figure()
        axes = figure.add_subplot(111, aspect='equal')
        axes.set_xlim(-1.5, 1.5)
        axes.set_ylim(-1.5, 1.5)

        # Initialize graphics objects
        self.circles = []
        for planet in self.planets:
            p = Circle((planet.position[0], planet.position[1]), 
                       planet.dimension, color=planet.color)
            p.set_visible(False)
            axes.add_patch(p)
            self.circles.append(p)

        def animate(frameNumber):
            # Without this, a copy of the figure will always be shown at its
            # original position.
            # Probably an easier way to do this, but the workaround is fine
            if frameNumber == 1:
                for c in self.circles:
                    c.set_visible(True)

            # Call the user updateFunc
            self.physics.timestep(self.planets)

            for c, p in zip(self.circles, self.planets):
                c.center = (p.position[0], p.position[1])

            # if self.physics.collision(self.projectile, self.castle):
            #     raise TypeError

            return self.circles

        ani = animation.FuncAnimation(figure,
                                      animate,
                                      frames=1000,
                                      interval=25,
                                      repeat=False,
                                      blit=True)

        plt.show()
