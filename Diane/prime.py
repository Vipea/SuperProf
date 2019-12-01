def factor(numberToFactor, arr=list()):
    i = 2

    # Maximum deelbare nummer.
    maximum = numberToFactor / 2 + 1

    # Vanaf i=2 want met factor 1 schiet je niet op
    while i < maximum:

        # Als het deelbaar is, dus als modulo 0
        if numberToFactor % i == 0:

            # Dan kunnen we verder met het nieuwe gedeelde nummer
            return factor(numberToFactor/i,arr + [i])

        # Als je niet kon delen, dan i + 1 en kijk weer of je kunt delen
        i += 1
    return list(set(arr + [numberToFactor]))

print(factor(10)) # [3, 5, 1747, 757]
