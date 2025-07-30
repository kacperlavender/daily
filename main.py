import string

# Treść zadania:
#     Napisz funkcję policz_słowa_w_pliku(nazwa_pliku), która:
#         Otwiera plik tekstowy o nazwie podanej w argumencie.
#         Liczy wystąpienia wszystkich słów (ignoruj wielkość liter; słowa traktuj jako ciągi rozdzielone spacjami lub znakami interpunkcyjnymi).
#         Zwraca słownik, gdzie kluczem jest słowo, a wartością liczba jego wystąpień.
#         W głównym programie zapytaj użytkownika o nazwę pliku (np. tekst.txt).

# Wyświetl 5 najczęściej występujących słów w formie:

# słowo1: liczba1
# słowo2: liczba2

file = input("podaj nazwe pliku ktory chcesz sprawdzic: \n")
dict = {}

try:
    with open(file) as f:
        dane = f.read()
        dane = dane.lower()
        # czyszczenie danych ze znakow intepunkcyjnych
        clean_dane = ''.join(ch for ch in dane if ch not in string.punctuation)

        word = clean_dane.split("\n")

        for w in word:
            if w.isalpha():
                if w in dict:
                    dict[w] += 1
                else:
                    dict[w] = 1

    print(dict)

    # alfabetyczne sortowanie slownika
    print({k: dict[k] for k in sorted(dict)})

    # 5 najczęstszych słów:
    print("5 najczęściej występujących słów:")
    najczestsze = sorted(dict.items(), key=lambda x: x[1], reverse=True)[:5]
    for slowo, liczba in najczestsze:
        print(f"{slowo}: {liczba}")

except FileNotFoundError:
    print("Nie znaleziono pliku!")