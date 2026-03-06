import pytest
from email_service import EmailService
from unittest.mock import MagicMock

@pytest.fixture
def email_service():
    return EmailService('smtp.example.com', 587, 'user@example.com', 'password')

@pytest.fixture
def mocker_fixture():
    return MagicMock()


def test_send_recovery_email(email_service, mocker_fixture):
    mock_send = mocker_fixture.patch('smtplib.SMTP.send_message')
    result = email_service.send_recovery_email('recipient@example.com', 'http://recovery.link')
    assert result is True
    mock_send.assert_called_once()