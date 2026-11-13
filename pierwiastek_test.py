from pierwiastek import pierwiastek


def test_pierwiastek_z_4():
    # Arrange: przygotowanie danych
    liczba = 4
    miejsca = 2
    # Act: wywolanie funkcji
    wynik = pierwiastek(liczba,miejsca)
    # Assert: sprawdzenie
    assert round(wynik,2) ==2
    