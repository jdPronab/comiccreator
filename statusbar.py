from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty

class StatusBar(BoxLayout):
    counter = NumericProperty(0)
    previous_counter = 0

    def on_counter(self, instance, value):
        if value == 0:
            self.msg_text.text = "Drawing space cleard"
        elif value - 1 == self.__class__.previous_counter:
            self.msg_text.text = "Widget added"
        elif value + 1 == self.previous_counter:
            self.msg_text.text = "Widget removed"
        self.previous_counter = value