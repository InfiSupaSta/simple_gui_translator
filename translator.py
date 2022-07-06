import translate
from translate import Translator


class TranslatorFromEnglishToRussian:

    def __init__(self, language_from: str = "en"):
        self.language_from = language_from

    def get_translator(self) -> translate.Translator:
        return Translator(to_lang="ru",
                          from_lang=self.language_from)

    def translate_to_russian(self, text_to_translate: str = '') -> str:

        translation = self.get_translator().translate(text_to_translate)

        try:
            string_for_long_input_text = ''

            if len(translation) >= 35:

                list_of_words = translation.split()
                part_size = 0

                for word in list_of_words:
                    if part_size >= 35:
                        string_for_long_input_text += '\n'
                        part_size = 0
                    string_for_long_input_text += f"{word} "
                    part_size += len(word)
            if string_for_long_input_text:
                translation = string_for_long_input_text

        except RuntimeError:
            translation = "Произошла ошибка во время выполнения программы. Попробуйте еще раз!"

        return translation
