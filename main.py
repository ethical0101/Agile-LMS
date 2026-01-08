def register(name):
    print(f"Student {name} registered successfully.")

#Login Feature code
def login(user, password):
    correct_user = "admin1"
    correct_password = "12345"

    if user == correct_user and password == correct_password:
        print("Login successful")
    else:
        print("Invalid username or password")


register("admin")
login("admin", "1234")
