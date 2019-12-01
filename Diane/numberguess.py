import random

def guess():
    random_number = random.randrange(100)
    max_pogingen = 8
    print("Raad een getal onder de 100")
    aantal_keren_geprobeerd = 0
    while aantal_keren_geprobeerd < max_pogingen:
        geraden_getal = int(input("Raad een getal: "))
        aantal_keren_geprobeerd += 1
        if geraden_getal == random_number:
            print(f"Goed geraden! En dat in {aantal_keren_geprobeerd} pogingen.")
        elif geraden_getal < random_number:
            print("Hoger!")
        else:
            print("Lager!")
    print("Helaas, het is je niet gelukt om het getal te raden!")

guess()
