def register(name):
    print(f"Student {name} registered successfully.")

#Login Feature code
def login(user, password):
    # simple hardcoded credentials
    correct_user = "admin"
    correct_password = "1234"

    if user == correct_user and password == correct_password:
        print("Login successful")
    else:
        print("Login failed")

register("admin")
login("admin", "1234")
