password = "password"

if len(password) < 8:
    print("Password mus be at least 8 characters")
elif len(password) > 30:
    print("Password is too long")
else:
    print("It's a good password")