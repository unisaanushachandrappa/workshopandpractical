class Seat:
    def __init__(self, row, seat):
        self.__row = row
        self.__seat = seat

    def __str__(self):
        return f"row {self.__row}, seat {self.__seat}"