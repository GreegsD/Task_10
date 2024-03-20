from kivy.app import App
from kivy.uix.button import Button
class myapp(App):
    def build(self):
        btn = Button(text="Shit Button")
        return btn
myapp().run()