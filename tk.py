import requests
from bs4 import BeautifulSoup
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
import os
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.card import MDCard

url = 'https://www.cbr.ru/currency_base/daily/'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', attrs={'class': 'data'})

rows = table.find_all('tr')[1:]

rates = []

for row in rows:
    cols = row.find_all('td')
    name = cols[1].text.strip()
    rate = float(cols[4].text.replace(',', '.'))
    rates.append([name, rate])



class Converter(MDApp):

    def menu_open(self):
        menu_items = [
            {
                "text": f"{rates[i][0]}",
                "on_release": lambda x=f"{rates[i][0]}", drop=i: self.menu_callback(x, drop),
            } for i in range(len(rates))
        ]
        MDDropdownMenu(
            caller=self.root.ids.drop_item, items=menu_items
        ).open()
    baluta = None
    id_balut = None
    def menu_callback(self, text_item, drop):
        self.baluta = text_item
        self.id_balut = drop
        print(self.baluta, self.id_balut)
        self.root.ids.drop_item.text = text_item
        self.root.ids.input.hint_text = text_item
        print(rates)
    def convert(self):
        print(int(self.root.ids.input.text))
        a = int(self.root.ids.input.text) * int(rates[self.id_balut][1])
        print(self.baluta, self.id_balut)
        self.root.ids.output.text = f"{a}"
    def build(self):
        return Builder.load_file('kivyconwerter.kv')

Converter().run()