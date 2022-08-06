from database import word

words = word.Word()
words.initdb()

while True:
    command = input("> ").strip().lower()
    if command == "добавить":    
        en_word = input("Введите английское слово: ").strip().lower()
        ru_word = input("Введите его перевод: ").strip().lower()
        words.write_translation(en_word, ru_word)
        print("Слово успешно добавлено!")
    elif command == "перевести":
        en_word = input("Введите английское слово: ").strip().lower()
        translations = words.get_translation(en_word)
        if len(translations) == 0:
            print("У нас нет перевода данного слова")
        else:
            for translation in translations:
                print(f'{translation[0]}: {translation[1]}')
    elif command == "выход":
        break
    else:
        print("""
добавить - для того чтобы добавить новое слово в словарь
перевести - чтобы перевести слово
выход - чтобы выйти
        """)

