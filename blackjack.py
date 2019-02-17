#!/usr/bin/env python3
import random

while True:
    house_card = 0
    house_hidden_card = 0
    house_number_of_aces = 0

    player_card = 0
    player_number_of_aces = 0

    house_card = random.randint(2,11)
    if house_card == 11:
        house_number_of_aces += 1

    for i in range(2):
        card = random.randint(2,11)
        if card == 11:
            player_number_of_aces += 1
        player_card += random.randint(2,11)

    print("You drew " + str(player_card))
    print("House drew " + str(house_card))

    decision = input("(H)it (S)tay: ").lower()
    if decision == "h":
        card = random.randint(2,11)
        if card == 11:
            player_number_of_aces += 1
        player_card += random.randint(2,11)

        if player_card > 21:
            if player_number_of_aces > 0:
                player_card -= 10
                player_number_of_aces -= 1
            else:
                print("Your total is " + str(player_card) + ", you went bust!\n")
                continue
