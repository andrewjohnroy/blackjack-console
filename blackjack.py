#!/usr/bin/env python3
import random
import sys

while True:
    house_card = 0
    house_hidden_card = 0
    house_number_of_aces = 0
    house_soft = False
    house_number_of_cards = 0
    
    player_card = 0
    player_number_of_aces = 0
    player_soft = False
    player_number_of_cards = 0

    house_card = random.randint(2,11)
    house_number_of_cards += 1
    if house_card == 11:
        house_number_of_aces += 1
        house_soft = True

    for i in range(2):
        card = random.randint(2,11)
        if card == 11:
            player_number_of_aces += 1
            player_soft = True
        player_card += card
        player_number_of_cards += 1 
    
    if player_soft:
        print("You drew soft " + str(player_card))
    else:
        print("You drew " + str(player_card)) 
    
    if house_soft:
        print("House drew soft " + str(house_card))
    else:
        print("House drew " + str(house_card))
    
    while True:
        decision = input("(H)it (S)tay (Q)uit: ").lower()
        if decision == "h":
            card = random.randint(2,11)
            if card == 11:
                player_number_of_aces += 1
                house_soft = True
            player_card += card
            player_number_of_cards += 1
            
            if player_card > 21:
                if player_number_of_aces > 0:
                    player_card -= 10
                    player_number_of_aces -= 1
                    if player_number_aces > 0:
                        print("Your total is soft " + str(player_card))
                else:
                    print("Your total is " + str(player_card) + ", you went bust!\n")
                    break
                elif player_card == 21:
                   print("Your total is 21! Blackjack!") 
        elif decision == "s":
            pass 
        elif decision == "q":
            sys.exit()
