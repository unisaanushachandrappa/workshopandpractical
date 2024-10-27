from character import Character

class Button:
    def __init__(self, mapping):
        self.__mapping = mapping

    def get_mapping(self):
        return self.__mapping

    @property
    def mapping(self):
        return self.__mapping

    def on_press(self, character):
        if self.mapping == "A":
            character.dodge()
        elif self.mapping == "B":
            character.attack()
        elif self.mapping == "X":
            character.aim_bow()
        elif self.mapping == "Y":
            character.shoot_arrow()
        elif self.mapping == "Left":
            character.move(self.mapping)
        elif self.mapping == "Right":
            character.move(self.mapping)
        elif self.mapping == "Up":
            character.move(self.mapping)
        elif self.mapping == "Down":
            character.move(self.mapping)

button = Button("A")
print(button.get_mapping())

button = Button("B")
print(button.mapping)