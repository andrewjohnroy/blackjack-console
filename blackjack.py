#!/usr/bin/env python3
import random
import sys

while True:
    house_card = 0
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
   
    while player_number_of_aces > 0 and player_card > 21:
        player_card -= 10
        player_number_of_aces -= 1
    
    if player_soft:
        print("\nYou drew soft " + str(player_card))
    else:
        print("\nYou drew " + str(player_card)) 
    
    if house_soft:
        print("House drew soft " + str(house_card))
    else:
        print("House drew " + str(house_card))
    
    while True:
        decision = input("(H)it (S)tay (Q)uit: ").lower()
        if decision == "h":
            print()
            card = random.randint(2,11)
            if card == 11:
                player_number_of_aces += 1
                player_soft = True
            player_card += card
            player_number_of_cards += 1
            
            while player_number_of_aces > 0 and player_card > 21:
                    player_card -= 10
                    player_number_of_aces -= 1
            
            if player_soft:
                print("Your total is soft " + str(player_card) + " " + str(player_number_of_aces) + " ace(s) unused.")
                print("House remains at " + str(house_card))
            else:
                print("Your total is " + str(player_card))
                print("House remains at " + str(house_card))
            
            if player_card > 21:
                print("You went bust!")
                break

        elif decision == "s":
            print()
            while house_card < 17:
                card = random.randint(2,11)
                if card == 11:
                    house_number_of_aces += 1
                    house_soft = True
                house_card += card
                house_number_of_cards += 1
           
            while house_number_of_aces > 0 and house_card > 21:
                house_card -= 10
                house_number_of_aces -= 1

            if house_soft and house_card == 21 and house_number_of_cards == 2:
                print("Dealer's final hand is 21, Blackjack!")
            elif house_soft and house_card <= 21:
                print("Dealer's final hand is soft " + str(house_card))
            elif house_soft and house_card > 21:
                print("Dealer went bust with soft " + str(house_card))
            elif house_card > 21:
                print("Dealer went bust with " + str(house_card))
            else:
                print("Dealer finished with " + str(house_card))

            if player_soft and player_card == 21 and player_number_of_cards == 2:
                print("Your final hand is 21, Blackjack!")
            elif player_soft and player_card <= 21:
                print("Your final hand is soft " + str(player_card))
            elif player_soft and player_card > 21:
                print("Your went bust with soft " + str(player_card))
            elif player_card > 21:
                print("Your went bust with " + str(player_card))
            else:
                print("You finished with " + str(player_card))

            if house_card == 21 and player_card == 21 and house_number_of_cards == 2 and player_number_of_cards == 2:
                print("Dealer and you get Blackjack. You win!")
            elif house_card == 21 and house_number_of_cards == 2 and player_soft:
                print("Dealer gets Blackjack. You lose with soft " + str(player_card))
            elif house_card == 21 and house_number_of_cards == 2:
                print("Dealer gets Blackjack. You lose with " + str(player_card))
            elif player_card == 21 and player_number_of_cards == 2:
                print("You get Blackjack! Dealer loses with " + str(house_card))
            elif player_card == 21 and player_number_of_cards == 2 and house_soft:
                print("You get Blackjack! Dealer loses with soft " + str(house_card))
            elif house_card > player_card and house_card <= 21:
                print("Dealer wins with " + str(house_card) + ", while you got " + str(player_card))
            elif player_card > house_card and player_card <= 21:
                print("You win with " + str(player_card) + ", while dealer got " + str(house_card) )
            elif player_card > 21 and house_card <= 21 and player_soft and house_soft:
                print("You went bust with soft " + str(player_card) + ", while dealer won with soft " + str(house_card) )
            elif player_card > 21 and house_card <= 21 and player_soft:
                print("You went bust with soft " + str(player_card) + ", while dealer won with " + str(house_card))
            elif player_card > 21 and house_card <= 21 and house_soft:
                print("You went bust with " + str(player_card) + ", while dealer won with soft " + str(house_card))
            elif player_card > 21 and house_card <= 21:
                print("You went bust with " + str(player_card) + ", while dealer won with " + str(house_card))
            elif player_card <= 21 and house_card > 21 and player_soft and house_soft:
                print("You won with soft " + str(player_card) + ", while dealer bust with soft " + str(house_card))
            elif player_card <= 21 and house_card > 21 and player_soft:
                print("You won with soft " + str(player_card) + ", while dealer bust with " + str(house_card))
            elif player_card <= 21 and house_card > 21 and house_soft:
                print("You won with " + str(player_card) + ", while dealer bust with soft " + str(house_card))
            elif player_card <= 21 and house_card > 21:
                print("You won with " + str(player_card) + ", while dealer bust with " + str(house_card))
            elif player_card > 21 and house_card > 21 and player_soft and house_soft:
                print("You bust with soft " + str(player_card) + ", while dealer bust with soft " + str(house_card))
            elif player_card > 21 and house_card > 21 and player_soft:
                print("You bust with soft " + str(player_card) + ", while dealer bust with " + str(house_card))
            elif player_card > 21 and house_card > 21 and house_soft:
                print("You bust with " + str(player_card) + ", while dealer bust with soft" + str(house_card))
            elif player_card > 21 and house_card > 21:
                print("You bust with " + str(player_card) + ", while dealer bust with " + str(house_card))
            elif player_soft and house_soft:
                print("You both tied for soft " + str(player_card) + ", you lose.")
            elif player_soft:
                print("You finished with soft " + str(player_card) + ", dealer finished with " + str(house_card) + ", you lose.")
            elif house_soft:
                print("You finished with " + str(player_card) + ", dealer finished with soft " + str(house_card) + ", you lose.")
            else:
                print("You both tied with " + str(player_card) + ", you lose.")
            break
        elif decision == "q":
            sys.exit()
        else:
            print("Sorry, I don't understand that instruction.")
