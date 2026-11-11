from decimal import Decimal, getcontext


def pierwiastek(liczba, miejsca):

    if liczba < 0:
        raise ValueError(
            "nie ma pierwiastka z liczby ujemnej"
        )  # jesli liczba ujemna, zglaszamy blad i zatrzymujemy funkcje
    if liczba == 0:
        return Decimal(0)

    dlugosc = len(str(liczba))
    getcontext().prec = dlugosc + miejsca + 10
    epsilon = (
        Decimal(10) ** -miejsca
    )  # epsilon liczony z liczby miejsc (minus robi ulamek)
    bok_a = Decimal(liczba)
    bok_b = liczba / bok_a  # b liczony z pola

    while abs(bok_a - bok_b) >= epsilon:
        bok_a = (bok_a + bok_b) / 2  # nowy a to sredni z obu bokow
        bok_b = liczba / bok_a  # b liczony z nowego a

    return (bok_a + bok_b) / 2  # srodek miedzy bokami po skonczeniu petli


print(pierwiastek(2, 30))
print(pierwiastek(0, 2))
