customer = {
    "name": "Jhon",
    "age": 32,
    "is_verified": True,
}

print(customer["name"])
print(customer["Name"])

print(customer.get("name"))
print(customer.get("Name"))
print(customer.get("birt_date", "01.01.1992"))

customer["gender"] = "male"
print(customer)

# Задание: Написать программу, которая спрашивает у пользователя номер
# и возвращает каждую цифру буквами:
# Phone: 123456
# One Two Three Four



phone = input("Phone: ")
didgits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three" 
}

output = ""
for ch in phone:
   output += didgits_mapping.get(ch, "!") + " "
print(output)