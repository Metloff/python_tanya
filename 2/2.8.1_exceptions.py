from argparse import ArgumentError


age = int(input('Age: '))
print(age)


try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid value')


try:
    age = int(input('Age: '))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')