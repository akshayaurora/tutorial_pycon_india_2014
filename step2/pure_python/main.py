from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):

    def build(self):
        # create root widget
        root_widget = BoxLayout(orientation='vertical')

        # create the labels and the textinputs
        lbl_user =  Label(text='User Name:')
        lbl_password = Label(text='Password')
        ti_user = TextInput()
        ti_password = TextInput(password=True)
        
        # create the containers for the labels and textinputs
        grid_user_pass = GridLayout(rows=2, cols=2)
        # create the ok button
        my_but_is_ok = Button(text='OK')

        # add the labels and input fields to the container 
        grid_user_pass.add_widget(lbl_user)
        grid_user_pass.add_widget(ti_user)
        grid_user_pass.add_widget(lbl_password)
        grid_user_pass.add_widget(ti_password)

        # add the grid_container into it's container
        root_widget.add_widget(grid_user_pass)
        # add the ok button at the bottom of the grid
        root_widget.add_widget(my_but_is_ok)

        return root_widget
if __name__ == "__main__":
    MainApp().run()
