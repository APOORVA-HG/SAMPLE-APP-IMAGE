from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.image import AsyncImage
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.uix.boxlayout import BoxLayout

class SampleApp(MDApp):

    def build(self):
        self.app_kv = '''
BoxLayout:
    orientation: 'vertical'

    BoxLayout:
        size_hint_y: None
        height: dp(50)
        Label:
            text: 'Electronics'
            font_size: '24sp'
            halign: 'center'
            valign: 'center'
            color: 0, 0, 0, 1

    AsyncImage:
        source: 'appimage.jpg'
        size_hint_y: 1
'''
        app_screen = Builder.load_string(self.app_kv)
        return app_screen

SampleApp().run()
