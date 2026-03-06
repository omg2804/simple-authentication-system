import pytest
from database import Database

@pytest.fixture
def db():
    db = Database()
    yield db
    db.close()

def test_add_user(db):
    db.add_user('user1', 'password1')
    assert db.get_user('user1') is not None

def test_update_user(db):
    db.add_user('user1', 'password1')
    db.update_user('user1', 'newpassword')
    user = db.get_user('user1')
    assert user[2] == 'newpassword'

def test_delete_user(db):
    db.add_user('user1', 'password1')
    db.delete_user('user1')
    assert db.get_user('user1') is None