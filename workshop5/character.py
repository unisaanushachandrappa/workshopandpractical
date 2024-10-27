class Character:
    def __init__(self, name):
        self.__name = name
        self.__arrows = 6
        self.__is_jumping = False
        self.__position = None

    def jump(self, is_jumping):
        self.__is_jumping = is_jumping

    def dodge(self):
        print(f"{self.__name} swiftly evades the enemy.")

    def attack(self):
        print(f"{self.__name} strikes the foe.")

    def aim_bow(self):
        print(f"{self.__name} takes aim.")

    def shoot_arrow(self):
        self.__arrows -= 1
        print(f"{self.__name} releases the shot.")
        self.display_arrows()

    def craft_arrow(self):
        self.__arrows += 1
        print(f"{self.__name} crafts a new arrow.")
        self.display_arrows()

    def move(self, position):
        self.__position = position

    def display_arrows(self):
        print(f"There are {self.__arrows} remaining in the quiver.")

char = Character("Billy")
char.display_arrows()
char.craft_arrow()
char.shoot_arrow()
char.aim_bow()
char.attack()
char.dodge()