class Planet(object):
    """
    Defines a class for the planets.
    """

    def __init__(self, mass, position, velocity):
        self._mass = mass
        self.position = position
        self.velocity = velocity

    @property
    def mass(self):
        return self._mass

    def __str__(self):
        return "Mass = %f\nPosition = (%f, %f)\nVelocity = (%f, %f)\n"\
                % (self.mass, self.position[0], self.position[1], 
                   self.velocity[0], self.velocity[1])
    
