# Zadanie na dziś to kolejny krok w stronę praktycznych umiejętności, które są przydatne na stanowisku Junior Python Developer. Tym razem poćwiczysz pracę z ciągami znaków, słownikami i prostą analizą tekstu.
# Treść zadania:

#     Poproś użytkownika o wpisanie dowolnego tekstu (może być nawet kilka zdań).
#     Policz, ile razy występuje każda litera w tekście (ignoruj wielkość liter, nie licz znaków innych niż litery alfabetu).
#     Wynik pokaż w formie słownika (np. {'a': 3, 'b': 0, ...}), gdzie klucz to litera, a wartość to jej liczba wystąpień.
#     Posortuj słownik alfabetycznie po literach przed wyświetleniem.


text = input("podaj zdanie ktorego liczbe wystapien liter chcesz policzyc:\n")

text = text.lower()

d = {}

for char in text:
    if char.isalpha():
        if char in d:
            d[char] += 1
        else:
            d[char] = 1

print(d)
print({k: d[k] for k in sorted(d)})