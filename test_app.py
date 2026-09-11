from app import create_message


def test_create_message():
    assert create_message("Cami") == "Bonjour Cami !"

def test_create_message_supprime_les_espaces():
    assert create_message(" Cami ") == "Bonjour Cami !"
