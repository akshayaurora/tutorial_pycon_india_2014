'''Plyer test
'''
from kivy.app import App
from plyer import battery
from plyer import notification
from plyer import tts

class Main(App):

    def get_battery(self, but):
        but.text = repr(battery.status)

    def speak(self):
        tts.speak('Plyer is sexy!')

Main().run()
