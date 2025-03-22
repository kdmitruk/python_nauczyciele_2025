def sortowanie_przez_wstawianie(dane):
    for i in range(1, len(dane)):
        aktualny = dane[i]
        for j in range(i):
            if aktualny < dane[j]:
                dane.pop(i)
                dane.insert(j, aktualny)
                break

