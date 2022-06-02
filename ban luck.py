##single player ban luck
from random import *
from colorama import Fore
from colorama import Style
from colorama import init

init(convert = True)

#################################################classes used within game#################################################
class player:
    def __init__(self, name):
        self._hand = []
        self._name = name
        self._money = 500
        self._bet = 0
        self._bankrupt = False
        self._evaluated = False
        self._card_header = ' _ _ _ '
        self._card_number = ['|A    |',\
                               '|2    |',\
                               '|3    |',\
                               '|4    |',\
                               '|5    |',\
                               '|6    |',\
                               '|7    |',\
                               '|8    |',\
                               '|9    |',\
                               '|10   |',\
                               '|J    |',\
                               '|Q    |',\
                               '|K    |']

        self._card_suit = ['|  ♣  |',\
                            '|  ♦  |',\
                            '|  ♥  |',\
                            '|  ♠  |',]
        self._card_footer = '|_ _ _|'
        
        
    def get_hand(self):
        return self._hand

    def set_hand(self, hand):
        self._hand = hand

    def get_name(self):
        return self._name

    def get_money(self):
        return self._money

    def add_money(self, winnings):
        self._money = self._money + winnings

    def get_bet(self):
        return self._bet

    def set_bet(self, bet):
        self._bet = bet

    def get_bankrupt(self):
        return self._bankrupt

    def set_bankrupt(self, bankrupt):
        self._bankrupt = bankrupt

    def get_evaluated(self):
        return self._evaluated

    def set_evaluated(self, evaluated):
        self._evaluated = evaluated
    
    def cards_held(self):
        return len(self._hand)
        
    def take_card(self, card):
        if card.get_number() == 0:
            self._hand = self._hand + [card]
        else:
            self._hand = [card] + self._hand
            
    def show_hand(self):                                                                    #display card in a pictorial manner
        for i in range(len(self._hand)):
            suit = self._hand[i].get_suit()
            if suit == 1 or suit == 2:
                print(f'{Fore.RED}', end = '')
            else:
                print(f'{Fore.WHITE}', end = '')
            print(self._card_header, end = '')
        print('')
        
        for i in range(len(self._hand)):
            suit = self._hand[i].get_suit()
            if suit == 1 or suit == 2:
                print(f'{Fore.RED}', end = '')
                print(self._card_number[self._hand[i].get_number()],end = '')
            else:
                print(f'{Fore.WHITE}', end = '')
                print(self._card_number[self._hand[i].get_number()],end = '')
        print('')
        
        for i in range(len(self._hand)):    
            suit = self._hand[i].get_suit()
            if suit == 1 or suit == 2:
                print(f'{Fore.RED}', end = '')
                print(self._card_suit[suit], end = '')
            else:
                print(f'{Fore.WHITE}', end = '')
                print(self._card_suit[suit], end = '')
        print('')

        for i in range(len(self._hand)):
            suit = self._hand[i].get_suit()
            if suit == 1 or suit == 2:
                print(f'{Fore.RED}', end = '')
            else:
                print(f'{Fore.WHITE}', end = '')
            print(self._card_footer, end = '')
        print(f'{Style.RESET_ALL}')
        return ''
    
    def evaluate(self):
        points = 0    
        for card in self._hand:
            if card.get_number() == 0:
                if len(self._hand) == 2:     #Ace is worth 11 points with 2 cards
                    if points <= 10:
                        points += 11
                    else:
                        points += 10
                elif len(self._hand) == 3:   #Ace is worth 10 or 1 point with 3 cards
                    if points <= 11:
                        points += 10
                    else:
                        points += 1
                else:                   #Ace is worth 1 point with more than 3 cards
                    points += 1
            else:
                points += card.get_value()
        return points   

    def draw_card(self):                                                #Returns zero if not drawing a card, returns non zero if drawing a card
        double = ['110','101']
        if len(self._hand) == 4:                                                        #checks if wu long mode needs to be activated
            return 2
        elif str(self._hand[0].get_number()) + str(self._hand[1].get_number()) == '00': #checks if there are combos in the hand (ban ban)
            print(player.get_name() + "'s hand")
            print(player.show_hand())
            return 3
        elif str(self._hand[0].get_value()) + str(self._hand[1].get_value()) in double: #ban luck
            print(player.get_name() + "'s hand")
            print(player.show_hand())
            return 4
        elif len(self._hand) == 3 and str(self._hand[0].get_number()) + str(self._hand[1].get_number()) + str(self._hand[2].get_number()) == '666':
            print(player.get_name() + "'s hand")
            print(player.show_hand())
            return 5                                                                    #triple 7                                        
        else:
            points = self.evaluate()
            if points <= 15:
                return 1
            elif points < 21:
                chance = randint(0,1)
                if chance:
                    return 1
                else:
                    return 0
            else:
                return 0
    
class banker(player):
    def __init__(self, name):
        super().__init__(name)

    def open_hand(self, player):
        player.show_hand()

class user(player):
    def __init__(self, name):
        super().__init__(name)

    def draw_card(self):
        double = ['101','110']
        if len(self._hand) == 4:                                                        #checks if wu long mode needs to be activated
            return 2
        elif str(self._hand[0].get_number()) + str(self._hand[1].get_number()) == '00': #checks if there are combos in the hand (ban ban)
            print(player.get_name() + "'s hand")
            print(player.show_hand())
            return 3
        elif str(self._hand[0].get_value()) + str(self._hand[1].get_value()) in double: #ban luck
            print(player.get_name() + "'s hand")
            print(player.show_hand())
            return 4
        elif len(self._hand) == 3 and str(self._hand[0].get_number()) + str(self._hand[1].get_number()) + str(self._hand[2].get_number()) == '666':
            print(player.get_name() + "'s hand")
            print(player.show_hand())
            return 5                                                                    #triple 7                                       
        else:
            draw = input("Do you want to draw a card? Enter 'y' or 'n'")
            if draw == 'y':
                print(player.get_name() + ' draws another card!')
                return 1
            else:
                return 0
                
class card:
    def __init__(self, suit, number, value):
        self._suit = suit
        self._number = number
        self._value = value

    def get_suit(self):
        return self._suit

    def set_suit(self, suit):
        self._suit = suit

    def get_number(self):
        return self._number

    def set_number(self, number):
        self._number = number

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

class deck:
    def __init__(self):
        self._deck = []
        
    def get_deck(self):
        return self._deck

    def set_deck(self, deck):
        self._deck = deck

    def top_card(self):
        return self._deck[0]
    
    def initialize_deck(self):
        suits = [0,1,2,3]
        values = [1,2,3,4,5,6,7,8,9,10,10,10,10]
        for suit in suits:
            for index in range(13):
                self._deck += [card(suit,index,values[index])]

    def shuffle(self):
        shuffle(self._deck)            
    
    def remove(self):
        self._deck = self._deck[1:] 

#################################################functions used within game#################################################
def distribute_cards(players):
    for i in range(0,2):
        for player in players:
            draw_card(player,deck)
    print('Banker has distributed cards!')

def draw_card(player,deck):
    player.take_card(deck.top_card())
    deck.remove()

def banker_combo(banker, players, state):
    if state == 2:                                        #if the wu long challenger is the banker itself
        if banker.evaluate() <= 21:                             #if banker win wu long challenge
            print(banker.get_name() + ' WU LONG success!')
            for player in players:
                if player.get_bankrupt() or player.get_evaluated():                       #check for bankrupt players
                    pass
                else:
                    print(player.get_name() + ' pays banker x2 of his/her bet!')
                    banker.add_money(player.get_bet() * 2)      #banker gains bet
                    player.add_money(-player.get_bet() * 2)     #player loses bet
                    player.set_evaluated(True)
        else:
            print(banker.get_name() + ' WU LONG fail!')         #if banker lose wu long challenge
            for player in players:                              #check for bankrupt players
                if player.get_bankrupt() or player.get_evaluated():
                    pass
                else:
                    print(banker.get_name() + ' pays ' + player.get_name() + ' x2 of his/her bet!')
                    player.add_money(player.get_bet() * 2)      #player gains bet
                    banker.add_money(-player.get_bet() * 2)     #banker loses bet
                    player.set_evaluated(True)
    else:
        if state == 3:                                              #if player ban ban
            print('BAN BAN! X3 each player bet')
            multiple = 3
        elif state == 4:                                            #if player ban luck
            print('BAN LUCK! X2 each player bet')
            multiple = 2
        elif state == 5:                                            #if player triple 7
            print('TRIPLE SEVEN! HUAT HUAT HUAT X7 each player bet')
            multiple = 7
        for player in players:                              #check for bankrupt players
            if player.get_bankrupt() or player.get_evaluated():
                pass
            else:
                print(player.get_name() + ' pays banker x2 of his/her bet!')
                banker.add_money(player.get_bet() * multiple)      #player gains bet
                player.add_money(-player.get_bet() * multiple)     #banker loses bet
                player.set_evaluated(True)
    banker.set_evaluated(True)

def combo(player,banker,state):
    if state == 2:
        print(player.get_name() + ' is going for the WU LONG!')
        draw_card(player,deck)
        player.show_hand()        
        if player.evaluate() <= 21:                             #if player win wu long challenge
            print(player.get_name() + ' WU LONG success!')
            print(banker.get_name() + ' pays ' + player.get_name() + ' x2 of his/her bet!')
            player.add_money(player.get_bet() * 2)              #player gains bet
            banker.add_money(-player.get_bet() * 2)             #banker loses bet
        else:                                                   #if player lose wu long challenge
            print(player.get_name() + ' WU LONG fail!')
            print(player.get_name() + ' pays banker x2 of his/her bet!')
            banker.add_money(player.get_bet() * 2)              #banker gains bet
            player.add_money(-player.get_bet() * 2)             #player loses bet
        player.set_evaluated(True)
    else:
        if state == 3:
            print('BAN BAN! X3 your bet')                       #if player ban ban
            multiple = 3
        elif state == 4:                                        #if player ban luck
            print('BAN LUCK! X2 your bet')
            multiple = 2
        elif state == 5:                                        #if player triple 7
            print('TRIPLE SEVEN! HUAT HUAT HUAT X7 your bet')  
            multiple = 7
        print(banker.get_name() + ' pays ' + player.get_name() + ' x' + str(multiple) + ' of his/her bet!')
        
        player.set_evaluated(True)
        player.add_money(player.get_bet() * multiple)                  #player gains bet
        banker.add_money(-player.get_bet() * multiple)                 #banker loses bet
              
def evaluate_winnings(banker,player):            
    if banker.evaluate() > 21:                                              #banker burst
        if player.evaluate() > 21:                                          #if draw;
            print(player.get_name() + ' burst together with the banker!\n') #nobody gains bet
        else:                                                               #else player wins bet;
            print(player.get_name() + ' won his/her bet!\n')
            player.add_money(player.get_bet())                              #player gains bet
            banker.add_money(-player.get_bet())
    else:                                                                   #banker less than or equal to 21
        if player.evaluate() > 21:                                          #if player burst;
            print(player.get_name() + ' burst!\n')
            banker.add_money(player.get_bet())                              #banker gains bet
            player.add_money(-player.get_bet())
        elif player.evaluate() == banker.evaluate():                        #if draw;
            print(player.get_name() + ' drew with the banker!\n')           #nobody gains bet
        elif player.evaluate() > banker.evaluate():                         #else if player wins bet;
            print(player.get_name() + ' won his/her bet!\n')
            player.add_money(player.get_bet())                              #player gains bet
            banker.add_money(-player.get_bet())
        elif player.evaluate() < banker.evaluate():                         #else player lost bet;
            print(player.get_name() + ' lost his/her bet!\n')
            banker.add_money(player.get_bet())                              #banker gains bet
            player.add_money(-player.get_bet())

#################################################actual implementation of game#################################################
print('Welcome to python Ban Luck!')
print('Objective of the game: Make the banker go bankrupt!')
#initialization of key items & players
player1 = player('Angela')
player2 = player('Dilip')
banker = banker('Hwee Sean')
name = input('Please enter your name: ')
user = user(name)
deck = deck()
deck.initialize_deck()

players = [player1, player2, user, banker] #initialization of players
while True:
    deck.shuffle()
    
    print('\n' + banker.get_name() + ' the banker has ' + str(banker.get_money()) + ' cents')

    for player in players[:-2]:
        if player.get_bankrupt():
            pass
        else:
            player.set_bet(randint(1,player.get_money()))                                   #players betting
            print(player.get_name() + ' has ' + str(player.get_money()) + ' cents')
            print(player.get_name() + ' bets ' + str(player.get_bet()) + ' cents\n')

    print(user.get_name() + ' has ' + str(user.get_money()) + ' cents')                     #user betting
    while True:
        try:
            bet = int(input('How much are you willing to bet in cents? '))                   
            if bet < 1 or bet > user.get_money():
                raise ValueError
            break
        except:
            print('Please enter a digit from 1 to the amount of money you have1')
    user.set_bet(bet)
    print(user.get_name() + ' bets ' + str(user.get_bet()) + ' cents\n')
    
    distribute_cards(players)
    print('Your hand:')
    user.show_hand()
    
    for player in players:                                                                  #ensure that bankrupt players are not participating
        if player.get_bankrupt():
            pass
        else:
            if player.get_name() == name:                                                   #drawing sequence for user
                draw = 1
                while True:
                    draw = player.draw_card()
                    if draw == 0:                                                           #state 0 = pass a turn
                        print(player.get_name() + ' passes turn')
                        break
                    elif draw == 1:                                                         #state 1 = draw a card
                        draw_card(player,deck)                                              #user draws a card
                        print('Your hand:')                                                 #show hand            
                        user.show_hand()
                    elif draw == 2:                                                         #state 2 = wu long mode
                        string = input('Will ' + player.get_name() + " draw another card?? Enter 'y' or 'n'!" )
                        if string == 'y':
                            player.show_hand()
                            combo(player,banker,draw)
                            break
                        else:
                            print(player.get_name() + ' passes turn')
                            break
                    elif draw == 3 or draw == 4 or draw == 5:
                        combo(player,banker,draw)      
            else:                                                                   #drawing sequence for non-users
                draw = 1
                while draw:
                    draw = player.draw_card()
                    if draw == 0:                                                   #state 0 = pass a turn
                        print(player.get_name() + ' passes turn')
                        break
                    elif draw == 1:
                        print(player.get_name() + ' draws another card!')           #state 1 = player draws a card
                        draw_card(player,deck)
                    elif draw == 2:                                                 #state 2 = wu long mode
                        if player.evaluate() >= 21:
                            print(player.get_name() + ' passes turn')
                            break
                        else:
                            string = input('Will ' + player.get_name() + ' draw another card?? Press enter key to find out!')
                            chance = randint(0,1)
                            if chance:
                                player.show_hand()
                                if player == banker:
                                    banker_combo(banker,players[:-1],draw)
                                else:
                                    combo(player,banker,draw)
                                break
                            else:
                                print(player.get_name() + ' passes turn')
                                break
                    elif draw == 3 or draw == 4 or draw == 5:
                        if player == banker:
                            banker_combo(banker,players[:-1],draw)
                        else:
                            combo(player,banker,draw)
                        break
                    
    if banker.get_evaluated():                                                  #if banker has been evaluated                   
        pass
    else:                                                                       #evaluating betting wins/losses
        print(banker.get_name() + "'s Hand: ") 
        print(banker.show_hand())
        if banker.evaluate() > 21:
            print(banker.get_name() + ' has burst!')
        else:
            print(banker.get_name() + ' has ' + str(banker.evaluate()) + ' points')
        for player in players[:-1]:
            if player.get_bankrupt() or player.get_evaluated():
                pass
            else:
                print(player.get_name() + "'s Hand: ")
                print(player.show_hand())
                evaluate_winnings(banker, player)
                if player.get_money() <= 0:
                    print(player.get_name()+ " owes " + banker.get_name() + ' ' + str(player.get_money()) + " cents.")
                else:
                    pass
    pause = input('Press enter to continue')
    evaluated = []
    deck.initialize_deck()
       
    for player in players:
        if player.get_bankrupt():
            pass
        else:
            player.set_hand([])
            player.set_evaluated(False)
            if player.get_money() <= 0:
                player.set_bankrupt(True)
                print(player.get_name() + ' has bankrupted and exited the game!')
                                                                                 #resetting
    if banker.get_bankrupt():
        print('Congratulations! The game has ended. You have won against the banker!')
        pause = input('Press enter to continue')
        break
    if user.get_bankrupt():
        print('You have bankrupted and lost the game!')
        pause = input('Press enter to continue')
        break

    pause = input('Press enter to continue')
    evaluated = []
    deck.initialize_deck()
