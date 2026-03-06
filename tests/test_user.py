import pytest
from user import create_user, update_user, delete_user

def test_create_user():
    user = create_user('user1', 'password1')
    assert user.username == 'user1'
    assert user.password == 'password1'

def test_update_user():
    user = create_user('user1', 'password1')
    updated_user = update_user(user, new_username='user2', new_password='newpassword')
    assert updated_user.username == 'user2'
    assert updated_user.password == 'newpassword'

def test_delete_user():
    user = create_user('user1', 'password1')
    assert delete_user(user) == 'User user1 deleted.'