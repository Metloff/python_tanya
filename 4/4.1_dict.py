from database import word

words = word.Word()
words.load_data()

while True:
    command = input("> ").strip().lower()
    if command == "добавить":    
        en_word = input("Введите английское слово: ").strip().lower()
        ru_word = input("Введите его перевод: ").strip().lower()
        words.write_translation(en_word, ru_word)
        print("Слово успешно добавлено!")
    elif command == "перевести":
        en_word = input("Введите английское слово: ").strip().lower()
        translation = words.get_translation(en_word)
        if len(translation) == 0:
            print("У нас нет перевода данного слова")
        else:
            print(translation)
    elif command == "выход":
        break
    else:
        print("""
добавить - для того чтобы добавить новое слово в словарь
перевести - чтобы перевести слово
выход - чтобы выйти
        """)
