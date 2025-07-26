# Napisz program, który:
#
#     Pobierze od użytkownika ciąg liczb całkowitych oddzielonych spacją (np. 4 7 -2 10 3).
#     Zwróci listę liczb tylko dodatnich i podniesie je do kwadratu.
#     Jeśli użytkownik poda coś, co nie jest liczbą, program powinien wyświetlić komunikat o błędzie i poprosić o podanie liczb ponownie (czyli aż do skutku).


while True:
    lst = []

    try:
        user_input = input("podaj liczby oddzielone spacjami: ")
        numbers = [int(x.strip()) for x in user_input.split(" ")]

        # for i in range(len(numbers)):
        #     if numbers[i-1] > 0:
        #         lst.append(numbers[i-1])
        #     else:
        #         continue

    except ValueError as e:
        print(e)
        print("niepoprawny format. podaj liczby ponownie")
        continue

    l = [x*x for x in numbers if x > 0]
    print(l)
    break