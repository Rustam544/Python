import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num_jokes):
    """
    Generate jokes from three arrays
    :param num_jokes: takes a lot of jokes
    :return:a string from the words of each array, the required number of times
    """
    len_list = len(nouns)-1
    i = 1
    while i <= num_jokes:
        print(f'{nouns[random.randint(0,len_list)]},'
              f'{adverbs[random.randint(0,len_list)]},'
              f'{adjectives[random.randint(0,len_list)]}')
        i += 1


num_jok = int(input('Введите количество шуток: '))
get_jokes(num_jok)
