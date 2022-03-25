from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.animation import Animation

from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import pprint
import csv
import os

Window.size = (1000, 600)


#screens
class ScreenManagement(ScreenManager):
    pass


class MenuScreen(Screen):
    def go_to_setting(self):
        self.parent.transition.direction = 'left'
        self.parent.current = 'SettingScreen'

    def animation_on_press(self, widget, *args):
        animate = Animation(background_color=(0.05, 0.43, 0.48, 0.5), duration=0.01)
        # animate &= Animation(size_hint=(0.075, 0.045), duration=0.1)
        animate &= Animation(size_hint=(widget.size_hint_x*0.9, widget.size_hint_y*0.9), duration=0.01)
        animate &= Animation(font_size=widget.font_size - 1, duration=0.1)
        animate.start(widget)

    def animation_on_release(self, widget, *args):
        animate = Animation(background_color=(0.15, 0.53, 0.58, 0.5), duration=0.01)
        # animate &= Animation(size_hint=(0.08, 0.05), duration=0.01) Ебал я снова это вычислять, пусть будет
        animate &= Animation(size_hint=(widget.size_hint_x*1.1, widget.size_hint_y*1.1), duration=0.01)
        animate &= Animation(font_size=widget.font_size + 1, duration=0.1)
        animate.start(widget)

    def send_owl(self,widget):
        print("И что ты хочешь?")



    def check_box_hendler(self, widget, value):
        if value:
            with open('data/platforms.csv', "r", newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    if widget.name == row[0]:
                        return
            with open('data/platforms.csv', "a", newline='') as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerow([widget.name])
        else:
            mas_row = []
            with open('data/platforms.csv', "r", newline='') as f1:
                reader = csv.reader(f1)
                for row in reader:
                    mas_row.append(row[0])

            with open('data/platforms.csv', 'w', newline='') as f1:
                writer = csv.writer(f1, delimiter=',')
                for row in mas_row:
                    if row != widget.name:
                        writer.writerow([row])




    #bind(on_dropfile=self.handledrops)


class SettingScreen(Screen):
    def go_to_menu(self):
        self.parent.transition.direction = 'right'
        self.parent.current = 'MenuScreen'

    def animation_on_press(self, widget, *args):
        animate = Animation(background_color=(0.05, 0.43, 0.48, 0.5), duration=0.01)
        animate &= Animation(size_hint=(0.11, 0.045), duration=0.1)
        animate &= Animation(font_size=widget.font_size - 1, duration=0.1)
        animate.start(widget)

    def animation_on_release(self, widget, *args):
        animate = Animation(background_color=(0.15, 0.53, 0.58, 0.5), duration=0.01)
        animate &= Animation(size_hint=(0.12, 0.05), duration=0.01)
        animate &= Animation(font_size=widget.font_size + 1, duration=0.1)
        animate.start(widget)

    def save_setting(self,widget):
        with open('data/password.txt', "r", newline='') as f:
            for row[:4дд] == row[0]:
                    return


class Owl_MailApp(App):
    def on_start(self):
        with open('data/platforms.csv', "r", newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    self.root.screens[0].ids[row[0]].active = True
                except:
                    pass


    def on_stop(self):
        pass
        return True





if __name__ == '__main__':
    Owl_MailApp().run()
