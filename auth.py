# auth.py

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# In-memory user storage for demonstration purposes
users_db = {}

def signup(username, password):
    if username in users_db:
        return "Username already exists."
    users_db[username] = User(username, password)
    return "User registered successfully."

def login(username, password):
    user = users_db.get(username)
    if user and user.password == password:
        return "Login successful."
    return "Invalid username or password."

def recover_password(username, new_password):
    user = users_db.get(username)
    if user:
        user.password = new_password
        return "Password updated successfully."
    return "User not found."