from film import Film
from ticket import Ticket

class Cinema:
    def __init__(self):
        self.__films = []
        self.__bookings = {}

    def create_booking(self, seat, person, file_name):
        self.add_film(file_name)
        self.__bookings[seat] = Ticket(file_name, person)

    def cancel_booking(self, seat):
        if seat in self.__bookings.keys():
            del self.__bookings[seat]

    def display_bookings(self):
        for key in self.__bookings.keys():
            print(f"-Ticket {key}-\n{self.__bookings[key]}")

    def add_film(self, film_name):
        flag = any(film.get_film_name() == film_name for film in self.__films)
        if not flag:
            self.__films.append(Film(film_name))

    def remove_film(self, film):
        self.__films.remove(film)

cinema = Cinema()
cinema.display_bookings()

cinema.create_booking("A3", "Link", "The Fifth Element")
cinema.create_booking("A4", "Zelda", "The Fifth Element")
cinema.create_booking("D5", "Ganon", "The Fifth Element")

cinema.create_booking("A3", "Ganon", "The Cruise")

cinema.cancel_booking("D5")
cinema.display_bookings()

print(type(cinema._Cinema__bookings))