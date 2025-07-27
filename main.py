# Treść zadania:
#     Napisz funkcję filtruj_i_podnos, która:
#         Przyjmuje listę liczb całkowitych.
#         Filtruje z niej liczby parzyste większe niż 10.
#         Następnie podnosi każdą z tych liczb do potęgi 3 (sześcian).
#         Zwraca nową listę wynikową.

#     Napisz prosty program, który:
#         Poprosi użytkownika o podanie liczb całkowitych oddzielonych spacją.
#         Zamieni je na listę liczb.
#         Użyje funkcji filtruj_i_podnos do przetworzenia listy.
#         Wypisze wynik.

def filtruj_i_podnos(l: list):
    # for i in range(len(l)):
    #     l[i] = int(l[i])

    return [x**3 for x in l if x > 10 and x % 2 == 0]

text = input("podaj liczby oddzielone spacjami:\n")
# l = text.split(" ")
l = [int(x) for x in text.split()]

print(filtruj_i_podnos(l))