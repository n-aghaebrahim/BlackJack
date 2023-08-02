import random
import time
import numbers
import os

#defining the deck
class Deck:

    def __init__(self):
        self.Face_Value = [2,3,4,5,6,7,8,9,10,'A','J','Q','K']
        self.Face_Img = ['Heart','Clover','Diamond','Spade']
        
    def deck(self): 
        x =[]
        for v in self.Face_Value:
            for i in self.Face_Img:
                x = x + [str(v)+','+str(i)]
        cards = x 
        return cards
    
    
    def shuffl(self,tmp):
        cards = random.sample(tmp, len(tmp))
        return cards
        
    
    def deal(self,cards):
        if len(cards)>1:
            card_distribute = cards.pop()
            return card_distribute
            

class information:
    
    def __init__(self):
        self.Player_Name = None
        self.Bet_Amount = None
        
    def Get_Name(self):
        player_name = input('What is your name: ')
        self.player_name = player_name
        return self.player_name.upper()
        
    def Get_Bet(self):
        state = False
        while not state:
            bet = input('How much is your Bet amount? $')
            try:
                if isinstance(float(bet), float):
                    state = True
                    return ('$' + str(bet))
            except ValueError:
                print('please enter numeric and correct format')
            

    
class rules:

    def hiting(cards):
        return Deck().Dealt(cards)
    
    def standing(self):
        return 1
        
i=1
while i==1 :
    start_Permision = input('Are you ready to play? (Yes/No)\n ')
    if start_Permision.upper() == 'YES':
        state = 1  
    elif start_Permision.upper == 'NO':
        state =0            
    else:
        print('ENTER VALID VALUE')
        state = 0
    while state == 1:
            player_name = information().Get_Name()
            print('Hi ' + player_name + ', every 6 rounds we will shuffle the cards')
            Game_Round = 1 
            player_profit_loss = 0
            total_player_bets = 0
            player_win_track = 0
            player_statues = None
            while Game_Round>0:
                #list of the showing dealer cards
                dealer_hand = []
                #list of the hidden dealer card
                dealer_hide_card = []
                #list of all cards that dealer has in numeric type 
                dealer_hand_value = []
                #list of all dealers cards
                all_dealer_card = []
                #list of player cards
                player_hand = []
                #list of player cards in numeric value
                player_hand_value = []
                bet = information().Get_Bet()
                total_player_bets = int(bet[1:]) + total_player_bets
                print('Player Name is: '+str(player_name) + '\n' + 'player bet Amount for this round is '+str(bet))
                print('Round: ' + str(Game_Round))
                print('total player bets is: '+'$'+str(total_player_bets))
                deck = Deck().deck()
                #shuffle in first round and also every 6 round
                if Game_Round%6 == 0 or Game_Round == 1:
                    #first step is shuffling 
                    print('start shuffling.....\n')
                    shuffled_deck = Deck().shuffl(deck)
                    time.sleep(1)
                    print('Deck shuffled\n')
                    print(shuffled_deck)
                #second step is to dealing the cards 
                while len(dealer_hide_card) < 2 and len(player_hand) <2:
                    player_hand.append(Deck().deal(shuffled_deck))
                    dealer_hide_card.append(Deck().deal(shuffled_deck))
                    player_hand.append(Deck().deal(shuffled_deck))
                    dealer_hand.append(Deck().deal(shuffled_deck))
                    
                all_dealer_card = dealer_hide_card + dealer_hand
                #seperate the value and kind and and add the values to the value list 
                #funciton to convert player hand to the  numeric value
                
                
                def convert_player(player_hand):
                    for card in player_hand:
                        value = card.split(',')
                        try: 
                            player_hand_value.append(int(value[0]))
                        except ValueError:
                            player_hand_value.append(value[0])
                    #convert club cards to the numeric value 
                    for e in player_hand_value:
                        if e == 'J':
                            player_hand_value[player_hand_value.index('J')] = 10
                        if e == 'Q':
                            player_hand_value[player_hand_value.index('Q')] = 10
                        if e == 'K':
                            player_hand_value[player_hand_value.index('K')] = 10
                            
                            
                #function to convert dealer hand to the numeric value
                
                
                def convert_dealer(all_dealer_card):
                    for card in all_dealer_card:
                        value = card.split(',')
                        try:
                            dealer_hand_value.append(int(value[0]))
                        except ValueError:
                            dealer_hand_value.append(value[0])
                    #convert club card to the numeric value
                    for e in dealer_hand_value:
                        if e == 'J':
                            dealer_hand_value[dealer_hand_value.index('J')] = 10
                        if e == 'Q':
                            dealer_hand_value[dealer_hand_value.index('Q')] = 10
                        if e == 'K':
                            dealer_hand_value[dealer_hand_value.index('K')] = 10
                    
                
                convert_player(player_hand)
                convert_dealer(all_dealer_card)
                print('player hand is:  ' + str(player_hand))
                print('dealer upper card is: ' + str(dealer_hand))
                #print('dealer hand value issss:' + str(all_dealer_card))
                
                #define hitting function
                
                
                def dealer_hit():
                        all_dealer_card.append(Deck().deal(shuffled_deck))

        
                #define function for player action
            
            
                def player_action():
                        x = 0
                        global player_sum
                        player_sum =0
                        number_of_a = 0
                        if 'A' in player_hand_value or 11  in player_hand_value or 1  in player_hand_value: #act like a soft hand
                            for v in player_hand_value:
                                    if v == 'A':
                                        player_hand_value[player_hand_value.index(v)] = 11
                                        number_of_a = number_of_a + 1
                            player_sum = 0
                            player_sum = sum(player_hand_value)
                            for i in range (number_of_a):
                                if player_sum >21:
                                    player_sum = player_sum - 10
                            print('player hand value is - soft - '+str(player_sum))
                            return player_sum
                        else:
                            for v in player_hand_value:
                                player_sum = player_sum + v
                            print('player hand value is - hard -'+str(player_sum))
                            return player_sum

                        
                            
                            
                            
                #define dealer action function that need to do
                
                
                def dealer_action():
                    x = 0
                    global dealer_sum
                    dealer_sum = 0
                    number_of_a = 0
                    global dealer_hand_value
                    dealer_sum_check = 0
                    while dealer_sum_check<18:
                            if 'A' in dealer_hand_value or 11  in dealer_hand_value or 1  in dealer_hand_value: #act like a soft hand
                                dealer_sum = 0
                                for v in dealer_hand_value:
                                    if v == 'A':
                                        dealer_hand_value[dealer_hand_value.index(v)] = 11
                                        number_of_a = number_of_a + 1
                                dealer_sum = sum(dealer_hand_value) 
                                for i in range (number_of_a):
                                    if dealer_sum > 21:
                                        dealer_sum = dealer_sum -10      
                                print('dealer sum soft hand is: '+str(dealer_sum))
                                dealer_sum_check = dealer_sum

                            else:
                                dealer_sum = 0
                                for v in dealer_hand_value:
                                    dealer_sum = dealer_sum + v
                                print('dealer sum is: ' +str(dealer_sum))                              
                                dealer_sum_check = dealer_sum
                                
                            if dealer_sum == 17 and 'A' in dealer_hand_value:
                                print('dealer is hitting on soft hand......')
                                all_dealer_card.append(Deck().deal(shuffled_deck))             #hitting function when dealer achived soft 17
                                dealer_hand_value = []
                                convert_dealer(all_dealer_card)
                            if dealer_sum == 17 and 'A' not in dealer_hand_value:
                                dealer_sum_check = 18
                            if dealer_sum < 17:
                                print('dealer is hitting...')
                                all_dealer_card.append(Deck().deal(shuffled_deck))             #hitting function when dealer achived soft 17
                                dealer_hand_value = []
                                convert_dealer(all_dealer_card)
                                print('dealer hand, after dealer hitted is: '+str (all_dealer_card))

                            
                            
                            
                #Check for double down
                dd_check = False
                while not dd_check:  
                        dd_action = input('Do you want to do Double Down?(yes/no) ')
                        if dd_action.upper() == 'YES':
                            dd_bet = input('Enter up to you this round bet: $')
                            if int(dd_bet)>int(bet[1:]):
                                print('Please enter up to this round bet')
                                dd_check = False
                            else:
                                bet = int(bet[1:]) + int(dd_bet)
                                print('$ '+str(dd_bet) + ' added to your bet, total bet is: $'+str(bet))
                                bet = '$'+str(bet)
                                dd_check = True  #to exit this roun  
                        elif dd_action.upper() == 'NO':
                            dd_check = True
                        else:
                            print('please enter valid value, yes or no.')
                            dd_check = False                    
                        
                #actions that needs to be done 
                action = input('Do you want to do Hit or Stand? ')
                done_check = False
                while not done_check:  

                        if action.upper() == 'STAND':
                            print('delaer hide card is: ' + str(dealer_hide_card))
                            print('dealer all hand card is'+str(all_dealer_card))
                            player_action()
                            if player_sum> 21:
                                print('PLAYER BUST')
                            dealer_action()
                            if dealer_sum < player_sum and player_sum<21:
                                print('player wins')
                                player_statues = 'win'
                            if dealer_sum >21 and player_sum<22:
                                print('dealer busted')
                                player_statues = 'win'
                            if player_sum == 21:
                                print('player wins\n ************BlackJack************')
                                print('player wins\n dealer lose')
                                player_statues = 'BlackJack'
                            if player_sum == 21 and dealer_sum ==21:
                                print('even')
                                print('both, blackjack') 
                                player_statues = 'even'
                            if player_sum == dealer_sum:
                                print('even')
                                player_statues = 'even'
                            done_check = True  #to exit this roun
                            
                            
                            
                        elif action.upper() == 'HIT':     
                            
    
                            player_hand.append(Deck().deal(shuffled_deck))
                            print('player hand after player hitted is: ' + str(player_hand))
                            player_hand_value = []
                            convert_player(player_hand)
                            player_action()
                            print('player hand value after hitting'+str(player_hand_value))
                            print('player sum after hitting is: '+ str(player_sum))
                            
                            if player_sum> 21:
                                print('PLAYER BUST')
                                player_statues = 'lose'
                                done_check = True     #to exit this roun
                            elif player_sum == 21:
                                print('player wins\n ************BlackJack************')
                                print('player wins\n dealer lose')
                                player_statues = 'BlackJack'
                                done_check = True     #to exit this roun 
                            else:
                                action = input('Do you want to Hit or Stand? ')
                                if action.upper() == 'HIT':
                                    done_check = False
                                elif action.upper() == 'STAND':
                                    done_check = False
                                else:
                                    print('Please enter correct value (Hit/ Stand).')
                        else:
                            print('please enter valid value, hit or stand')
                            action = input('Do you want to do Hit or Stand? ')
                            done_check = False

                                
                if player_statues == 'win':
                    player_win_track +=1
                    player_profit_loss = player_profit_loss + int(bet[1:]) 
                elif player_statues == 'even':
                    player_win_track +=1/2
                    player_profit_loss = player_profit_loss + (1/2) * int(bet[1:]) 
                elif player_statues == 'BlackJack':
                    player_win_track +=1
                    player_profit_loss = player_profit_loss + (3/2) * int(bet[1:])               
                else:
                    player_profit_loss = player_profit_loss - int(bet[1:])

                
                player_win_ratio = (player_win_track/Game_Round) * 100
                print('player win ratio is ' +str(player_win_ratio)+ ' percents') 
                print('plaeyer total profit/ loss is: ' + str(player_profit_loss))
                
                print('************************************************ NEXT ROUND ************************************************')
                Game_Round = Game_Round +1
                
                

                
                
