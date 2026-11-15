import pytest
from pierwiastek import pierwiastek
from decimal import Decimal, getcontext


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

# test uruchamia sie 3 razy, za kazdym razem z innymi danymi z tabelki
@pytest.mark.parametrize(
    "liczba,miejsca",
    [(2,2),(2,50), (10,4)],
)
def test_blad_mniejszy_niz_pole_epsilon(liczba,miejsca):
    # Arrange: wzorzec liczymy niezaleznie, z duza dokladnoscia
    getcontext().prec = 1500
    wzorzec = Decimal(liczba).sqrt()
    epsilon = Decimal(10) ** -miejsca
    # Act: wywolanie funkcji    
    wynik = pierwiastek(liczba, miejsca)
    # Assert: blad mniejszy niz pol epsilona
    assert abs(wynik - wzorzec) < epsilon / 2

    def ujemna_liczba():
        #arrange: dane
        liczba = -4
        miejsce = 2
         # Act i Assert razem: wywolanie musi rzucic ValueErro
        with pytest.raises(ValueError):
                pierwiastek(liczba,miejsce)