

def num_translate_adv(en_digit):
    dict_digit = {
        'one': 'один', 'two': 'два',
        'three': 'три', 'four': 'четыре',
        'five': 'пять', 'six': 'шесть',
        'seven': 'семь', 'eight': 'восемь',
        'nine': 'девять', 'ten': 'десять'
    }
    fst_sym = en_digit
    en_digit = en_digit.lower()
    if fst_sym == en_digit:
        print(dict_digit.get(en_digit))
    else:
        fst_sym = dict_digit.get(en_digit)
        print(fst_sym.capitalize())


digit = input('Введите число от 1го до 10 на англ. языке: ')
num_translate_adv(digit)
