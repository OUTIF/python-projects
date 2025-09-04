import random
CARDS=[11,2,3,4,5,6,7,8,9,10,10,10,10]
class Card():
    def __init__(self):
        self.deck = []
        self.score = 0

    def card_generator(self, x, name):
        for card in range(x):
            new_card=random.choice(CARDS)
            self.deck.append(new_card)
            self.score += new_card
        print(f'the {name} deck:{tuple(self.deck)},total score:{self.score}')

    def score_check(self,name):
        if self.score==21:
            print('you win')
            return 1
        elif (self.score>21 and (CARDS[0]in self.deck)):
            index = self.deck.index(CARDS[0])
            self.deck[index] = 1
            self.score -= 10
            print(f'{name} wins with total score:{self.score}')
            if self.score == 21:
                print(f'{name} wins with total score:{self.score}')
        elif self.score>21:
            print(f'{name} lose with total score of :{self.score}')
            return False
