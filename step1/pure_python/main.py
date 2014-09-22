from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):

  def build(self):
    but_trouble =  Button(text='Hello')
    but_lazy = Button(text='World')
    root_widget = BoxLayout()

    root_widget.add_widget(but_trouble)
    root_widget.add_widget(but_lazy)

    return root_widget

if __name__ == "__main__":
    MainApp().run()
