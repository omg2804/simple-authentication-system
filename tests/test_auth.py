import pytest
from auth import signup, login, recover_password, User

@pytest.fixture
def setup_users():
    return {'user1': 'password1', 'user2': 'password2'}

def test_signup(setup_users):
    assert signup('user1', 'password1') == 'User registered successfully.'
    assert signup('user1', 'password1') == 'Username already exists.'

def test_login(setup_users):
    signup('user1', 'password1')
    assert login('user1', 'password1') == 'Login successful.'
    assert login('user1', 'wrongpassword') == 'Invalid username or password.'

def test_recover_password(setup_users):
    signup('user1', 'password1')
    assert recover_password('user1', 'newpassword') == 'Password updated successfully.'
    assert login('user1', 'newpassword') == 'Login successful.'