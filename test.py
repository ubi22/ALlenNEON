from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.filemanager import MDFileManager
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (400, 600)

KV = '''
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: "Choose File"
            MDRaisedButton:
                id: choose_file_button
                text: "Choose file"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        '''


class MyApp(MDApp):
    def build(self):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            previous=True,
        )
        screen = Builder.load_string(KV)
        screen.ids.choose_file_button.bind(on_release=self.show_file_manager)
        return screen

    def show_file_manager(self, instance):
        self.file_manager.show('/')

    def select_path(self, path):
        with open(path, 'r') as file:
            data = file.read()
            print(data)

    def exit_manager(self, *args):
        self.file_manager.close()


if __name__ == "__main__":
    MyApp().run()
