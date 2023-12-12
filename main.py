import json
import hashlib
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.animation import Animation
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.tab import MDTabsBase
import requests
import sqlite3
from kivymd.uix.floatlayout import MDFloatLayout
import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
Window.size = (480, 800)

LabelBase.register(name='text',
                      fn_regular='Style/ba.ttf')
LabelBase.register(name='text_double',
                      fn_regular='Style/Mikar.ttf')


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class Wallet(MDApp):
    # def open_file(self):
    #     self.screen('file_pem')
    #     selected_file = self.root.ids.file_chooser.selection and self.root.ids.file_chooser.selection[0]
    #     if selected_file:
    #         with open(selected_file, 'r') as file:
    #             file_contents = file.read()
    #             print(file_contents)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True
        )
        self.file_manager.ext = [".txt"]

    def screen(self, screen_name):
        self.root.current = screen_name
    def file_manager_open(self, file):
        self.manager_open = True
        self.file_manager.show(os.path.expanduser("D:/"))
    def login_using_password(self):
        self.screen('main_screen')

    def sign_in_enter_using_password(self):
        self.screen('main_screen')

    def login_account(self):
        pass

    def create_account(self):
        self.screen('create_account_enter_password')
        open('file.dat', 'w')

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        self.root.ids.download_pem.text = f"{path}"

        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


    def upload_pem(self):
        pass

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.material_style = "M3"
        # self.root.current = 'second_login'
        sm = Builder.load_file("kivy.kv")
        if os.path.isfile("file.dat"):
            sm.current = "login_account_enter_password"
        return sm




Wallet().run()