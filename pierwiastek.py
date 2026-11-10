from decimal import Decimal, getcontext


def pierwiastek(liczba, miejsca):

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
print(pierwiastek(10**400, 5))
