import hashlib

def register_user():
    """
    we tell the user they have not registered, get the password they want to use, hash it and store it
    """
    print("No password found")
    password_input = password_prompting()
    password_hash = hash(password_input=password_input)
    with open("master_password.txt", "w") as master_password:
        master_password.write(password_hash)

def login():
    password_input = password_prompting()
    password_hash = hash(password_input=password_input)
    # open and read the file, compare it to hash of the input, allowing access if a match
    with open("master_password.txt", "r") as master_password:
        if master_password.read() != password_hash:
            print("Incorrect Password, please try again.")
        else:
            print("Welcome!")

def password_prompting():
    # get the password input twice so we can confirm it. after confirmation, we just return the first one
    password_input1 = input("Choose/enter a password: ")
    password_input2 = input("Please confirm password: ")
    while password_input1 != password_input2:
        print("Passwords don't match. Please try again")
        password_input1 = input("Choose a password: ")
        password_input2 = input("Please confirm password")
    return password_input1

def hash(password_input):
    h = hashlib.new('sha256')
    h.update(password_input.encode())
    return h.hexdigest()

# open and read the master_password file
master_password = open("master_password.txt")
content = master_password.read()
# if its empty, they have yet to register so we must register them, else they must log in
if content == "":
    register_user()
else:
    login()