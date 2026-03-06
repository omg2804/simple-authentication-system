# user.py

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User(username={self.username})"

def create_user(username, password):
    return User(username, password)

def update_user(user, new_username=None, new_password=None):
    if new_username:
        user.username = new_username
    if new_password:
        user.password = new_password
    return user

def delete_user(user):
    # In a real application, you would remove the user from the database
    return f"User {user.username} deleted."