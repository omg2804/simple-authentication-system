import pytest
from main import main

@pytest.fixture
def capsys(capfd):
    return capfd

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Welcome to the Simple Authentication System'