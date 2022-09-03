def my_shiny_new_decorator(function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate() # Сама функция
        print("А я - код, срабатывающий после")
    # Вернём эту функцию
    return the_wrapper_around_the_original_function


# Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
@my_shiny_new_decorator
def stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")

@my_shiny_new_decorator
def qwe():
    print("ТАНЯ ТАНЯ ТАНЯ")


qwe()

