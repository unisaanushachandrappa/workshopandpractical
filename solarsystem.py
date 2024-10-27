from planet import Planet

class SolarSystem:
    def __init__(self):
        self.planets = []
        self.valid_planets = ["mercury","venus", "earth","mars","jupiter","saturn","uranus","neptune"]

    def add_planet(self, planet):
        if not planet.get_name().lower() in self.valid_planets:
            print("----------")
            print(f"L {planet.get_name()}. You are not a real planet.\n")
        elif isinstance(planet, Planet):
            self.planets.append(planet)
        else:
            print(f"{planet.get_name()}. You are not a real planet")

    def remove_planet(self, planet):
        if planet in self.planets and isinstance(planet, Planet):
            self.planets.remove(planet)

    def __str__(self):
        newline = "\n"
        return (f"Planets in our Solar System:\n"
                f'{newline.join(f"{planet}" for planet in self.planets)}')

solar_system = SolarSystem()
mercury = Planet("Mercury", 0.333, 4879, 5429, 3.7, 57.9, 167, 0, False, True)
venus = Planet("Venus", 4.87, 12104, 5243, 8.9, 108.2, 464, 0, False, False)
earth = Planet("Earth", 5.97, 12756, 5514, 9.8, 149.6, 15, 1, False, True)
mars = Planet("Mars", 0.642, 6792, 3934, 3.7, 228.0, -65, 2, False, False)
jupiter = Planet("Jupiter", 1898, 142984, 1326, 23.1, 778.5, -110, 92, True, True)
saturn = Planet("Saturn", 568, 120536, 687, 9.0, 1432.0, -140, 83, True, True)
uranus = Planet("Uranus", 86.8, 51118, 1270, 8.7, 2867.0, -195, 27, True, True)
neptune = Planet("Neptune", 102, 49528, 1638, 11.0, 4515.0, -200, 14, True, True)
pluto = Planet("Pluto", 0.0130, 2376, 1850, 0.7, 5906.4, -225, 5, False, None)

solar_system.add_planet(mercury)
solar_system.add_planet(venus)
solar_system.add_planet(earth)
solar_system.add_planet(mercury)
solar_system.add_planet(mars)
solar_system.add_planet(jupiter)
solar_system.add_planet(saturn)
solar_system.add_planet(uranus)
solar_system.add_planet(neptune)
solar_system.add_planet(pluto)

print(solar_system)