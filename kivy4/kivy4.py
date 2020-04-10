from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

class MyGrid(GridLayout):
    usr = ObjectProperty(None)
    pss = ObjectProperty(None)

    def login(self):
        if self.usr.text == "inside" and self.pss.text == "python":
            print("Login Successfull")

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":

    MyApp().run()