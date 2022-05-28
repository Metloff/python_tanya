try:
    age = int(input('Age: '))
    print(age)
    income = 2000
    risk = income / age
    print(risk)
except ZeroDivisionError:
    print("Делить на ноль нельзя")
except ValueError:
    print('Invalid value')