from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class myapp(App):
    def build(self):
        txt=Label(text='Shit text')
        btn= Button(text ='shit button')
        layout= BoxLayout()
        layout.add_widget(txt)
        layout.add_widget(btn)
        return layout


myapp().run()