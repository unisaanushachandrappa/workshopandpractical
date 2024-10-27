from workshop5.button import Button
from workshop5.trigger import Trigger

class Controller:
    def __init__(self):
        self.__character = None
        self.__triggers = []
        self.__action_buttons = []
        self.__directional_buttons = []

    def get_triggers(self):
        return self.__triggers

    @property
    def triggers(self):
        trigger_names = []
        for trigger in self.__triggers:
            trigger_names.append(trigger.mapping)
        return trigger_names

    def get_action_buttons(self):
        return self.__action_buttons

    @property
    def action_buttons(self):
        action_button_names = []
        for button in self.__action_buttons:
            action_button_names.append(button.mapping)
        return action_button_names

    def get_directional_buttons(self):
        return self.__directional_buttons

    @property
    def directional_buttons(self):
        directional_button_names = []
        for button in self.__directional_buttons:
            directional_button_names.append(button.mapping)
        return directional_button_names

    def set_character(self, character):
        self.__character = character

    def press_button(self, button):
        button.on_press()

    def map_controller(self):
        self.__triggers.append(Trigger("L1"))
        self.__triggers.append(Trigger("L2"))
        self.__triggers.append(Trigger("R1"))
        self.__triggers.append(Trigger("R2"))

        self.__action_buttons.append(Button("A"))
        self.__action_buttons.append(Button("B"))
        self.__action_buttons.append(Button("X"))
        self.__action_buttons.append(Button("Y"))

        self.__directional_buttons.append(Button("Left"))
        self.__directional_buttons.append(Button("Right"))
        self.__directional_buttons.append(Button("Up"))
        self.__directional_buttons.append(Button("Down"))

cont = Controller()
cont.map_controller()
for x in cont.triggers:
    print(x)
print("--------")

for x in cont.directional_buttons:
    print(x)
print("--------")

for x in cont.action_buttons:
    print(x)
print("--------")