# This is left open as a excercise for users to implement the python equivalent code
# that matches the functionality present in the kv section
# Problem: Implement ScreenManager and screens as present in the kv section 
# however only using python code.
# The Solution will be posted online after the talk

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from plyer import tts

class MainApp(App):

    def build(self):
        # create root widget
        root_widget = FloatLayout()
        box = BoxLayout(orientation='vertical',
                        size_hint=(None, None),
                        size=(400, 200),
                        spacing=dp(20),
                        padding=dp(20),
                        pos_hint={'center_x': .5, 'center_y':.5})

        # create the labels and the textinputs
        lbl_user =  Label(text='User Name:')
        lbl_password = Label(text='Password')
        ti_user = TextInput()
        ti_password = TextInput(password=True)
        
        # create the containers for the labels and textinputs
        grid_user_pass = GridLayout(rows=2, cols=2, spacing=dp(20))
        # create the ok button
        my_but_is_ok = Button(text='OK')
        my_but_is_ok.bind(on_release=lambda *args: self.check_user(ti_user.text, ti_password.text))

        # add the labels and input fields to the container 
        grid_user_pass.add_widget(lbl_user)
        grid_user_pass.add_widget(ti_user)
        grid_user_pass.add_widget(lbl_password)
        grid_user_pass.add_widget(ti_password)

        # add the grid_container into it's container
        box.add_widget(grid_user_pass)
        root_widget.add_widget(box)
        # add the ok button at the bottom of the grid
        box.add_widget(my_but_is_ok)

        return root_widget

    def check_user(self, user, pwd):
        if pwd.lower() == 'pyconindia':
            tts.speak('Hello {}. Welcome to Pycon India!'.format(user))
        if pwd.lower() == 'funny':
            tts.speak('Lalu ji ko rabbri, bahoot pasand hai!')


if __name__ == "__main__":
    MainApp().run()
