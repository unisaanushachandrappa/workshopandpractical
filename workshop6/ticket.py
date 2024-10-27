class Ticket:
    def __init__(self, film, person):
        self.__film = film
        self.__person = person

    def __str__(self):
        return f"Playing: {self.__film}, held by {self.__person}"