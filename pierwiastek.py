def pierwiastek(liczba,miejsca):
    epsilon = 0.0001
    bok_a = liczba
    bok_b = liczba/bok_a #b liczony z pola

    while abs(bok_a - bok_b) >= epsilon:
        bok_a = (bok_a + bok_b) /2 #nowy a to sredni z obu bokow 
        bok_b = liczba / bok_a # b liczony z nowego a


    return (bok_a + bok_b) / 2 #srodek miedzy bokami po skonczeniu petli


print(pierwiastek(2,4))