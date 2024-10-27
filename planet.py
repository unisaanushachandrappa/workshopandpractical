import math

class Planet:
    def __init__(self, name, mass, diameter, density, gravity, distance_from_sun, mean_temperature, moon_count, ring_system, global_magnetic_field):
        self.name = name
        self.mass = mass
        self.diameter = diameter
        self.density = density
        self.gravity = gravity
        self.distance_from_sun = distance_from_sun
        self.mean_temperature = mean_temperature
        self.moon_count = moon_count
        self.ring_system = ring_system
        self.global_magnetic_field = global_magnetic_field

    def get_name(self):
        return self.name

    def radius(self):
        return self.diameter/2

    def surface_area(self):
        return round(4 * math.pi * self.radius() * self.radius(), 2)

    def get_mass(self):
        return f"{self.name} has a mass of {self.mass}.\n"

    def calculate_mass(self, weight):
        mass = weight * self.gravity
        return f"My mass is {mass} (Newtons) on {self.name}"

    def calculate_weight(self, mass):
        weight = round(mass * self.gravity/9.8, 1)
        return f"I weigh {weight} (kg) on {self.name}"

    def get_distance(self):
        return f"It is {self.distance_from_sun} 10\u2076 km from the sun.\n"

    def get_moon_count(self):
        if self.moon_count <= 0:
            return f"There are no moons orbiting {self.name}."
        elif self.moon_count == 1:
            return f"There is a single moon which orbits {self.name}."
        else:
            return f"There are {self.moon_count} moons orbiting {self.name}."

    def get_magnetic_field(self):
        if self.global_magnetic_field:
            return f"\n{self.name} has a global magnetic field."
        else:
            return ""

    def get_ring_system(self):
        if self.ring_system:
            return " It has ring(s) surrounding it.\n"
        else:
            return "\n"

    def __str__(self):
        return (f"---{self.name.upper()}---\n"
                f"{self.get_mass()}"
                f"{self.get_distance()}"
                f"{self.get_moon_count()}"
                f"{self.get_magnetic_field()}"
                f"{self.get_ring_system()}")