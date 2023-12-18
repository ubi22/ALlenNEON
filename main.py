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
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import hashlib
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
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

    def pad(self, s):
        return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

    def undo_pad(self, s):
        return s[:-ord(s[len(s) - 1:])]

    def screen(self, screen_name):
        self.root.current = screen_name

    def file_manager_open(self, file):
        self.manager_open = True
        self.file_manager.show(os.path.expanduser("D:/"))

    def login_using_password(self):
        self.screen('main_screen')
        # self.screen('main_screen')
        # text = self.root.ids.seed_text.text
        # password = self.root.ids.password_login.text
        # encrypted_text = self.encrypt_text(password, text)
        # with open("file.txt", "w") as myfile:
        #     myfile.write(f"{encrypted_text}")
        # with open("file.dat", "w") as myfile:
        #     a = self.root.ids.password_login.text
        #     hashed_string = hashlib.sha256(a.encode('utf-8')).hexdigest()
        #     myfile.write(f"{hashed_string}")
        #     myfile.close()

    def sign_in_enter_using_password(self):
        self.screen('main_screen')
        # with open("file.txt", "r") as myfile:
        #     password_sig_in = self.root.ids.password_sig_in.text
        #     a = codecs.decode(myfile.read())
        #     print(a)
        #     s = self.decrypt_text(a, password_sig_in)
        #     print(s)

        # with open("file.dat", "r") as myfile:
        #     set = myfile.readline()
        #     set1 = self.root.ids.password_sig_in.text
        #     a = hashlib.sha256(set1.encode('utf-8')).hexdigest()
        #     print(set)
        #     print(a)
        #     if a == set:
        #         print(set)
        #         self.screen('main_screen')
        #     else:
        #         toast('Пороль не правильный')

    def login_account(self):
        self.screen('create_account_enter_password')

    def create_account(self):
        self.screen('create_account_enter_password')

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
        if os.path.isfile("file.txt"):
            sm.current = "login_account_enter_password"
        return sm

Wallet().run()