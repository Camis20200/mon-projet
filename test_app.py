from app import create_message


def test_create_message():
    assert create_message("Cami") == "Bonjour Cami !"
