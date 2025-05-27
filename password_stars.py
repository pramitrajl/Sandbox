min_length = 8
password = input("Enter password: ")
while len(password) < min_length:
    print(f"Error: Password must be at least {min_length} characters long.")
    password = input("Enter password: ")
print("Password accepted")