from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_string("""

<GridLayout>:
    cols: 2
    Label:
        canvas:
            Color:
                rgba: 1, 0, 0, 1
            Line:
                points: self.x, self.y, self.x+self.width, self.y+self.height          
    Widget:
        canvas:
            # Color:
            #     rgba: 1, 1, 0, 1
            Line:
                points: self.x, self.y, self.x+self.width, self.y+self.height
    
""")

class LabelApp(App):
    def build(self):
        return GridLayout()

if __name__== '__main__':
    LabelApp().run()