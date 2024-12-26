# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
#
# Декілька правил:
#
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
# Приклади:
# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes



import string

# Вывод списка
texts = [
    "Python Community",
    "I like python community!",
    "Should, I. subscribe? Yes!"
]

# обрабатываем каждый ряд в списке
for text in texts:
    # удаляем все символы пунктуации
    clean_text = text.translate(str.maketrans("", "", string.punctuation))

    # разбиваем ряд на слова
    words = clean_text.split()
    hashtag = "#" + "".join(word.capitalize() for word in words)

    # обрезаем хештег, если он больше 140 символов
    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    # выводим хештег
    print("Хештег:", hashtag)
