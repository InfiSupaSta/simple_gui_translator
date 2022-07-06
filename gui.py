import tkinter

from gui_settings import TextInputSettings, ButtonSettings, LabelSettings, WindowSettings
from translator import TranslatorFromEnglishToRussian


class ComponentsCreation:

    """
    Класс с методами создания компонентов основного окна приложения.
    """

    @staticmethod
    def create_button() -> tkinter.Button:
        button = tkinter.Button(
            text=ButtonSettings.default_button_text,
            font=ButtonSettings.font_type_and_size,
            background=ButtonSettings.background_color,
            fg=ButtonSettings.font_color
        )
        return button

    @staticmethod
    def create_label() -> tkinter.Label:
        label = tkinter.Label(
            text=LabelSettings.default_text,
            background=LabelSettings.background_color,
            font=LabelSettings.font_type_and_size,
            fg=LabelSettings.font_color
        )
        return label

    @staticmethod
    def create_text_input() -> tkinter.Text:
        text_input = tkinter.Text(
            width=TextInputSettings.width,
            height=TextInputSettings.height,
            bg=TextInputSettings.background_color,
            font=TextInputSettings.font_type_and_size,
            fg=TextInputSettings.font_color
        )
        return text_input


class Window:

    """
    Класс для создания основного окна приложения.
    """

    def __init__(self):
        self.__window = tkinter.Tk()
        self.translator = TranslatorFromEnglishToRussian()
        self.topmost = False

    def set_window_settings(self) -> None:
        self.__window.geometry(WindowSettings.geometry)
        self.__window.title(WindowSettings.title)
        self.__window.configure(
            bg=WindowSettings.background_color
        )
        self.__window.resizable(width=False, height=False)

    def create_field_for_text_input(self) -> None:
        self.text_input = ComponentsCreation.create_text_input()

        self.text_input.pack()

    def get_text_from_input(self) -> str:
        return self.text_input.get("1.0", "end")

    def get_translation(self):
        translation = self.translator.translate_to_russian(
            self.get_text_from_input()
        )
        self.label["text"] = translation

    def create_button_for_translation_request(self):
        self.translate_button = ComponentsCreation.create_button()

        self.translate_button.config(
            text='Get translation',
            command=self.get_translation)
        self.translate_button.pack()

    def create_button_for_topmost_choice(self) -> None:
        self.choice_button = ComponentsCreation.create_button()

        self.choice_button.config(
            text=ButtonSettings.default_topmost_choice_button_text,
            command=self.to_topmost)
        self.choice_button.pack()

    def create_label(self) -> None:
        self.label = ComponentsCreation.create_label()

        self.label.pack()

    def to_topmost(self) -> None:
        if self.topmost:
            self.__window.attributes("-topmost", False)
            self.topmost = False
            self.choice_button["text"] = ButtonSettings.default_topmost_choice_button_text
        else:
            self.__window.attributes("-topmost", True)
            self.topmost = True
            self.choice_button["text"] = 'В данный момент приложение поверх всех окон. \n Нажми для отмены!'

    def application_preparations(self):

        """
        В каком порядке методы будут вызваны,
        в таком они и будут отрисованы.
        (может измениться в будущем)
        """

        self.set_window_settings()
        self.create_button_for_topmost_choice()
        self.create_field_for_text_input()
        self.create_button_for_translation_request()
        self.create_label()

    def create_mainloop(self) -> None:
        self.__window.mainloop()
