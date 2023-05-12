import string


class Alphabet:

    def info(self):
        print(f"{self.lang}")
        print(f"{self.letters}")

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        print(f"Буквы алфавита: {self.letters}")

    def letters_num(self):
        print(f"{len(self.letters)}")


class EngAlphabet(Alphabet):
    __letters_num = 26
    default_lang = "En"

    def __init__(self):
        super().__init__(EngAlphabet.default_lang, string.ascii_uppercase)

    def is_en_letter(self, letter):
        if letter in self.letters:
            return True
        return False

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print(f"Пример текста на английском языке:\nDont judje book by its cover")


if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('F'))
    print(eng_alphabet.is_en_letter('Щ'))
    EngAlphabet.example()
