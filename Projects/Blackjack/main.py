from cards import Card
player = Card()
computer = Card()
game_on = True
while game_on:
    player.card_generator(2, "player")
    computer.card_generator(1, "computer")
    game_on = False
    # ask the player if he wants a card ?

    if player.score==21:
        while computer.score<18:
            computer.card_generator(1,'computer')
            computer.score_check('computer')
    else:
        card_asking = True
        while card_asking == True:
            user_wish = input('Do You want another card?').lower()
            if user_wish != 'yes':
                card_asking = 0
                while computer.score < 18:
                    computer.card_generator(1, 'computer')
                    if computer.score > player.score:
                        print(f'computer wins with total score of {computer.score}')
                    else:
                        print(f'You win with total score of {player.score}')

            else:
                player.card_generator(1, 'player')
                if player.score_check('player')==False:
                    card_asking=0
