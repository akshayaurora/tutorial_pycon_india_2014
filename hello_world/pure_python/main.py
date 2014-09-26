'''Hello World Example using kivy
'''

from kivy.app import App
from kivy.uix.button import Button

class Main(App):
    '''Just a bad button.
    '''
    
    def build(self):
        but_bad = Button(text="Who's bad?",
                         font_size=24)
        return but_bad

if __name__ == '__main__':
    Main().run()    
