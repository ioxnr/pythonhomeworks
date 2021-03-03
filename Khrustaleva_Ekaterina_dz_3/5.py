from random import randrange  # импортируем модуль, который возвращает случайное число


def get_jokes(n):
    jokes = []  # список для сбора готовых шуток
    for i in range(n):
        random_noun = randrange(0, len(nouns))  # генерируем случайный индекс для списка существительных
        random_adverb = randrange(0, len(adverbs))  # генерируем случайный индекс для списка наречий
        random_adjective = randrange(0, len(adjectives))  # генерируем случайный индекс для списка прилагательных
        jokes.append(nouns[random_noun] + ' ' + adverbs[random_adverb] + ' ' + adjectives[
            random_adjective])  # добавляем в список готовых шуток нашу сгенерированную шутку
    return jokes  # возвращаем список готовых шуток


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(2))
