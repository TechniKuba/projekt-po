import pytest
from pierwiastek import pierwiastek


@pytest.mark.parametrize(  #uruchom test poniżej cztery razy, za każdym razem z innymi danymi z tabelki
    "liczba, miejsca, oczekiwane",
    [
        (4, 2, 2),
        (9, 3, 3),
        (0, 2, 0),
        (1, 2, 1),
    ],
)
def test_pierwiastek_znane_wartosci(liczba, miejsca, oczekiwane):
    #AAA 
    # Arrange: dane przychodza z tabelki wyzej
    # Act: wywolanie funkcji
    wynik = pierwiastek(liczba, miejsca)
    # Assert: sprawdzenie
    assert round(wynik, miejsca) == oczekiwane