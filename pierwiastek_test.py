import pytest
from pierwiastek import pierwiastek, main
from decimal import Decimal, getcontext
from pierwiastek import pierwiastek, main


@pytest.mark.parametrize(  # uruchom test poniżej cztery razy, za każdym razem z innymi danymi z tabelki
    "liczba, miejsca, oczekiwane",
    [
        (4, 2, 2),
        (9, 3, 3),
        (0, 2, 0),
        (1, 2, 1),
    ],
)
def test_pierwiastek_znane_wartosci(liczba, miejsca, oczekiwane):
    # AAA
    # Arrange: dane przychodza z tabelki wyzej
    # Act: wywolanie funkcji
    wynik = pierwiastek(liczba, miejsca)
    # Assert: sprawdzenie
    assert round(wynik, miejsca) == oczekiwane


# test uruchamia sie 3 razy, za kazdym razem z innymi danymi z tabelki
@pytest.mark.parametrize(
    "liczba,miejsca",
    [(2, 2), (2, 50), (10, 4)],
)
def test_blad_mniejszy_niz_pole_epsilon(liczba, miejsca):
    # Arrange: wzorzec liczymy niezaleznie, z duza dokladnoscia
    getcontext().prec = 1500
    wzorzec = Decimal(liczba).sqrt()
    epsilon = Decimal(10) ** -miejsca
    # Act: wywolanie funkcji
    wynik = pierwiastek(liczba, miejsca)
    # Assert: blad mniejszy niz pol epsilona
    assert abs(wynik - wzorzec) < epsilon / 2


def test_ujemna_liczba():
    # arrange: dane
    liczba = -4
    miejsce = 2
    # Act i Assert razem: wywolanie musi rzucic ValueError
    with pytest.raises(ValueError):
         
        pierwiastek(liczba,miejsce)


def test_zly_typ():
    #arrange: liczba z przecinkiem zamiat całkowitej
    liczba = 2.5
    miejsca = 2
    # act i assert razem:
    with pytest.raises(TypeError):
        pierwiastek(liczba, miejsca)


def test_main_dla_4_i_2():
    dane = ["4", "2"]# udajemy wpisanie 2
    wynik = []

    def read():
        return dane.pop(0) #pop bierze pierwszy element z listy
    # Act: main pisze do listy wynik zamiast na ekran
    main(read, wynik.append)
    # Assert: main wypisal 2.00
    assert str(wynik[0]) == "2.00"


def test_main_brak_dancyh():
    # Arrange: read od razu zglasza koniec danych
    wynik= []

    def read():
        raise EOFError

    # Act
    main(read, wynik.append)
    
    # Assert: main pokazal komunikat zamiast sie wywalic
    assert wynik[0] == "Brak danych"
