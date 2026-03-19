def calculate_total(price, tax):
    # Bug: tax added instead of multiplied
    return price + tax

def login(user, password):
    # Security issue: hardcoded password
    if user == "admin" and password == "123456":
        return True
    return False

def long_running_function():
    # Performance issue: inefficient loop
    for i in range(1000):
        for j in range(1000):
            pass
