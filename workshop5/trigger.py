from character import Character

class Trigger:
    def __init__(self, mapping):
        self.__mapping = mapping

    def get_mapping(self):
        return self.__mapping

    @property
    def mapping(self):
        return self.__mapping

    def on_press(self, character):
        if self.mapping == "L1":
            character.jump()
        if self.mapping == "L2":
            character.jump()
        if self.mapping == "R1":
            character.jump()
        if self.mapping == "R2":
            character.jump()