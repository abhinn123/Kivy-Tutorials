from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MyGrid(GridLayout):
    def login(self, instance):
        print("Login Successfull")

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":

    MyApp().run()