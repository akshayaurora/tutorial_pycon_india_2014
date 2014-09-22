from kivy.app import App
from plyer import tts

class MainApp(App):

    def check_user(self, user, pwd):
        if pwd.lower() == 'pyconindia':
            tts.speak('Hello {}. Welcome to Pycon India!'.format(user))
        if pwd.lower() == 'funny':
            tts.speak('Lalu ji ko rabri achi lagti hai')

if __name__ == "__main__":
    MainApp().run()
