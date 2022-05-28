# Задача: Написать программу, куда пользователь вводит любой текст
# Программа возвращается тот же текст, но заменяет значки смайлов
# на настоящие смайлы. Пример:
# > I am sad ):
# I am sad 😞











message = input("> ")
words = message.split(" ")

emojis = {
    ":)": "😀",
    "(:": "😞",
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)