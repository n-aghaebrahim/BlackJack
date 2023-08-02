try:
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import simpledialog
    from tkinter import *
except ImportError:
    import Tkinter as tk
    from Tkinter import messagebox
    from Tkinter import simpledialog
    from Tkinter import *    
import random
import time
import numbers
import os



#defining the deck class 
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



#PLAYER INFORMATION

class information:
    
    
    def __init__(self):
        self.Player_Name = None
        self.Bet_Amount = None
       
       
    def Get_Name(self):
        player_name = input('What is your name: ')
        self.player_name = player_name
        return self.player_name.upper()
  
  
                        
#getting initial bet amount
def getInputt():                                                     
    global bett     
    global display_bet
    global player_bet
    global l
    bett = entry_bet.get()
    try:
        if type(int(bett))== int:
            try:
                l.destroy()
            except NameError: 
                pass 
            entry_widget
            l1.destroy()
            b1.destroy()
            entry_widget.destroy()
            try:
                display_bet.destroy()
                root.update()
            except NameError:
                pass
            display_bet = Label(root, text = ("Player bet amount for this round:  $"+ bett))
            canvas1.create_window(1000, 150, window=display_bet)                
            player_bet = int(bett)
            root.update() 
            first_bet()
                
    except ValueError:
        try:
            l.destroy()
            root.update()
        except NameError: 
            pass
        l = Label(root, text = "PLEASE ENTER BET AMOUNT IN INTEGER")
        canvas1.create_window(600, 500, window=l)
        root.update() 

#define widgets to get initial bet amount       
def Get_Bet():
    global bett
    global player_bet
    state = False
    global l1
    l1 = Label(root, text = "how much is your bet amount? $")
    canvas1.create_window(250, 150, window=l1)
    root.update() 
    global entry_bet
    entry_bet = tk.StringVar()
    global entry_widget
    entry_widget = tk.Entry(root, textvariable=entry_bet)
    canvas1.create_window(250, 200, window=entry_widget)
    global b1
    b1 = tk.Button (root, text='Okay',command=getInputt)
    canvas1.create_window(250, 230, window=b1)
        
        
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
    global all_dealer_card
    global dealer_all_hand_label
    dealer_sum = 0
    number_of_a = 0
    global dealer_hand_value
    dealer_sum_check = 0
    while dealer_sum_check<18:
        if 'A' in dealer_hand_value or 11  in dealer_hand_value or 1  in dealer_hand_value: #act like a soft hand
            print(dealer_hand_value)
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


#MAIN GAME LOOP
def main_game():

    MsgBox = tk.messagebox.askquestion ('start Game','Press yes when you are ready to start a game',icon = 'warning')
    if MsgBox == 'yes':
        i = 1
        start_Permision = 'YES'
    else:
        display_name.destroy()
        i =0
        start()
    while i==1 :
        print('Are you ready to play? ',start_Permision)     #changed input to print   
        if start_Permision.upper() == 'YES':
            state = 1
            i =0
        elif start_Permision.upper == 'NO':
            state =0            
        else:
            print('ENTER VALID VALUE')
            state = 0  
        while state == 1:
                    print('Hi ' + player_name + ', Every 6 rounds we will shuffle the cards')
                    tk.messagebox.showinfo(title = 'info', message = ' Hi ' + player_name + '\n Every 6 rounds we will shuffle the cards')
                    global Game_Round
                    Game_Round = 1
                    global total_player_bets
                    total_player_bets = 0
                    global player_profit_loss
                    global player_win_track
                    player_profit_loss = 0
                    player_win_track = 0
                    global player_statues
                    player_statues = None
                    global player_win_ratio 
                    player_win_ratio = 0
                    Get_Bet()
                    state = 0
                        
                    
def first_bet():

    global dealer_hand
    #list of the showing dealer cards
    dealer_hand = []
    global dealer_hand_value
    #list of all cards that dealer has in numeric type 
    dealer_hand_value = []
    global all_dealer_card
    #list of all dealers cards
    all_dealer_card = []
    global player_hand_value
    #list of player cards in numeric value
    player_hand_value = []
    global dealer_hide_card
    #list of the hidden dealer card
    dealer_hide_card = []
    global player_hand
    #list of player cards
    player_hand = []
    print('bet amount is'+str(bett))
    global total_player_bets
    total_player_bets = int(bett) + total_player_bets
    print('Player Name is: '+str(player_name) + '\n' + 'player bet Amount for this round: $'+str(bett))
    global Game_Round
    global total_bet_label                   
    print('Round: ' + str(Game_Round))
    print('total player bets: '+'$'+str(total_player_bets))
    if Game_Round > 1:
        total_bet_label.destroy()
        root.update()
    try:
        total_bet_label.destroy()
        root.update
    except NameError:
        pass
    total_bet_label = Label(root, text = "total player bets is: "+'$'+str(total_player_bets))
    canvas1.create_window(1000, 200, window=total_bet_label)     
    root.update()
    global round_label
    if Game_Round == 1:
        #round_label.destroy()
        #root.update() 
        round_label = Label(root, text = "Round: "+str(Game_Round))
        canvas1.create_window(1000, 100, window=round_label)   
        root.update() 
    deck = Deck().deck()
    #shuffle in first round and also every 6 round
    global shuffled_deck
    if Game_Round%6 == 0 or Game_Round == 1:
        #first step is shuffling 
        print('start shuffling.....\n')
        shuffled_deck = Deck().shuffl(deck)
        time.sleep(1)
        print('Deck shuffled\n')
        tk.messagebox.showinfo(title = 'Deck', message = 'Deck shuffled')                        
        print(shuffled_deck)
        #second step is to dealing the cards 
    while len(dealer_hide_card) < 2 and len(player_hand) <2:
        player_hand.append(Deck().deal(shuffled_deck))
        dealer_hide_card.append(Deck().deal(shuffled_deck))
        player_hand.append(Deck().deal(shuffled_deck))
        dealer_hand.append(Deck().deal(shuffled_deck))
    all_dealer_card = dealer_hide_card + dealer_hand
    #seperate the value and kind and and add the values to the value list                 
    convert_player(player_hand)
    convert_dealer(all_dealer_card)
    print('player hand is:  ' + str(player_hand))
    global player_hand_label_f
    player_hand_label_f = Label(root, text = "Player hand is:  "+str(player_hand))
    canvas1.create_window(280, 300, window=player_hand_label_f)
    root.update() 
    print('dealer upper card is: ' + str(dealer_hand))
    global dealer_hand_label
    dealer_hand_label = Label(root, text = "Dealer upper card: "+str(dealer_hand))
    canvas1.create_window(280, 330, window=dealer_hand_label)
    root.update() 
    print('dealer hand value i:' + str(all_dealer_card))

    
    #define hitting function                                     
    def dealer_hit():
        all_dealer_card.append(Deck().deal(shuffled_deck))

          
    #Check for double down
    global dd_action
    dd_check = False
    while not dd_check:                              
        MsgBox = tk.messagebox.askquestion ('Double Down','Do you want to do Double Down?',icon = 'question')
        if MsgBox == 'yes':
            dd_action = 'YES'
            print('Do you want to do Double Down?(yes/no) '+str(dd_action))
            Get_Bet_dd()
            dd_check = True
        else:
            print('Do you want to do Double Down?(yes/no) '+'NO')
            global total_player_bets_d
            total_player_bets_d = int(bett)
            hit_stand_decision()
            dd_check = True
                               

#define function to get additional bet amount for doing double down
def getInputt_dd():                                                     
    global bett_dd     
    global display_bet
    global player_bet_dd
    global l
    global total_player_bets
    global total_player_bets_d
    bett_dd = entry_bet.get()
    total_player_bets_d = int(bett)
    try:
        if type(int(bett_dd))== int and int(bett)>int(bett_dd):              
            entry_widget
            l1.destroy()
            b1.destroy()
            try:
                display_bet.destroy()
            except NameError:
                pass
            try:
                l.destroy()
                root.update()
            except NameError:
                pass
            entry_widget.destroy()
            total_player_bets_d = total_player_bets_d + int(bett_dd)
            try:
                total_bet_label_dd.destroy()
                root.update()
            except NameError:
                pass
            total_bet_label_dd = Label(root, text = 'Player bet amount for this round:  $'+str(total_player_bets_d))
            canvas1.create_window(1000, 150, window=total_bet_label_dd)
            root.update() 
            total_player_bets = total_player_bets + int(bett_dd)
            try:
                total_bet_label.destroy()
                root.update()
            except NameError:
                pass
            total_bet_label = Label(root, text = "total player bets is: "+'$'+str(total_player_bets))
            canvas1.create_window(1000, 200, window=total_bet_label)     
            root.update()                 
            player_bet_dd = int(bett_dd)
            hit_stand_decision()
                
        if int(bett)<=int(bett_dd):
            tk.messagebox.showinfo(title = 'info', message = 'Please enter UP to your initial bet')                
                                   
    except ValueError:
        try:
            l.destroy()
            root.update()
        except NameError:
            pass
        l = Label(root, text = "PLEASE ENTER BET AMOUNT IN INTEGER")
        canvas1.create_window(600, 500, window=l)
        root.update() 

#define widget to get extrra bet for double down     
def Get_Bet_dd():
    global bett_dd
    global player_bet_dd
    global l1
    global entry_bet
    global entry_widget
    global b1    
    state = False
    l1 = Label(root, text = "how much do you want to add to your initial bet? $")
    canvas1.create_window(220, 170, window=l1)
    root.update() 
    entry_bet = tk.StringVar()
    entry_widget = tk.Entry(root, textvariable=entry_bet)
    canvas1.create_window(200, 200, window=entry_widget)
    b1 = tk.Button (root, text='Okay',command=getInputt_dd)
    canvas1.create_window(200, 250, window=b1)

#hit button to set action variable to HIT
def hit_bu():
    global action
    action = 'HIT'
    hit_stand()
    
#stand button to set action variable to STAND   
def stand_bu():
    global action
    action = 'STAND'
    hit_stand()
    
#define hit and stand buttons 
def hit_stand_decision():   
    global hit_b
    try: 
        hit_b.destroy()
        root.update() 
    except NameError:
        pass 
    hit_b = tk.Button (root, text='hit',command=hit_bu)
    canvas1.create_window(600, 500, window=hit_b)
    global stand_b
    try: 
        stand_b.destroy()
        root.update() 
    except NameError:
        pass 
    stand_b = tk.Button (root, text='stand',command=stand_bu)
    canvas1.create_window(600, 550, window=stand_b)

                              
def hit_stand():
                            
    global action
    global player_hand_value
    global player_statues
    global dealer_all_hand_label
    global dealer_hide_hand_label
    print('Do you want to do Hit or Stand? '+action)
    global result_label
    global player_hand_label
    done_check = False
    hit_track = 0
    if action.upper() == 'STAND':
        print('delaer hide card is: ' + str(dealer_hide_card))
        print('dealer all hand card is'+str(all_dealer_card))                               
        player_hand_value = []
        convert_player(player_hand)
        player_action()                                
        if player_sum> 21:
            print('PLAYER BUST')
            result_label = Label(root, text ='last hand result:\n'+ 'PLAYER BUST')
            canvas1.create_window(1000, 350, window=result_label) 
            #root.update()
            player_statues = 'Busted'
            dealer_action()               
        elif player_sum == 21:
            print('player wins\n ************BlackJack************')
            print('player wins\n dealer lose')
            result_label = Label(root, text = 'last hand result:\n'+'player wins\n ************BlackJack************')
            canvas1.create_window(1000, 350, window=result_label) 
            #root.update() 
            player_statues = 'BlackJack'
            dealer_action()                                
        else:
            dealer_action()
            if dealer_sum < player_sum and player_sum<21:
                print('player wins')
                result_label = Label(root, text = 'last hand result:\n'+'player wins')
                canvas1.create_window(1000, 350, window=result_label) 
                #root.update()                                     
                player_statues = 'win'
            elif dealer_sum <21 and player_sum<21 and dealer_sum > player_sum:
                print('Dealer wins')
                result_label = Label(root, text = 'last hand result:\n'+'Dealer wins')
                canvas1.create_window(1000, 350, window=result_label)
                #root.update() 
                player_statues = 'loss'                
            elif dealer_sum >21 and player_sum<22:
                print('dealer busted')
                result_label = Label(root, text = 'last hand result:\n'+'dealer busted')
                canvas1.create_window(1000, 350, window=result_label)
                #root.update() 
                player_statues = 'win'
            elif player_sum == 21:
                print('player wins\n ************BlackJack************')
                print('player wins\n dealer lose')
                result_label = Label(root, text = 'last hand result:\n'+'player wins\n ************BlackJack************')
                canvas1.create_window(1000, 350, window=result_label)
                #root.update() 
                player_statues = 'BlackJack'
            elif player_sum == 21 and dealer_sum ==21:
                print('even')
                print('both, blackjack') 
                result_label = Label(root, text = 'last hand result:\n'+'even, both blackjack')
                canvas1.create_window(1000, 350, window=result_label) 
                #root.update() 
                player_statues = 'even'
            elif player_sum == dealer_sum:
                print('even')
                result_label = Label(root, text = 'last hand result:\n'+'even')
                canvas1.create_window(1000, 350, window=result_label) 
                #root.update() 
                player_statues = 'even'
            elif dealer_sum == 21 and player_sum<21:
                print('Dealer wins - Blackjack')
                result_label = Label(root, text = 'last hand result:\n'+'Dealer wins - Blackjack')
                canvas1.create_window(1000, 350, window=result_label) 
                #root.update() 
                player_statues = 'Busted'                
        done_check = True  #to exit this roun
        root.update()
        last()
                                
                                
    elif action.upper() == 'HIT':     
                                
        try: 
            player_hand_label.destroy()
            root.update() 
        except NameError:
            pass         
        player_hand.append(Deck().deal(shuffled_deck))
        print('player hand after player hitted is: ' + str(player_hand))       
        player_hand_label = Label(root, text = "Player hand after hitting:  "+str(player_hand))
        canvas1.create_window(300, 500, window=player_hand_label)                                
        player_hand_value = []
        convert_player(player_hand)
        player_action()
        print('player hand value after hitting'+str(player_hand_value))
        print('player sum after hitting is: '+ str(player_sum))
        root.update()
        hit_track +=1                                
        if player_sum> 21:
            print('PLAYER BUST')
            result_label = Label(root, text = 'last hand result:\n'+'PLAYER BUST')
            canvas1.create_window(1000, 350, window=result_label) 
            root.update()                                     
            player_statues = 'lose'
            last()
            done_check = True     #to exit this round
        elif player_sum == 21:
            print('player wins\n ************BlackJack************')
            print('player wins\n dealer lose')
            result_label = Label(root, text = 'last hand result:\n'+'player wins\n ************BlackJack************')
            canvas1.create_window(1000, 350, window=result_label) 
            root.update() 
            player_statues = 'BlackJack'
            last()
            done_check = True     #to exit this roun 
        else:
            print('Do you want to do Hit or Stand? '+str(action))
            hit_stand_decision()
            done_check = False                                
    else:
        print('please enter valid value, hit or stand')
        action = input('Do you want to do Hit or Stand? ')
        done_check = False
                            


                                

def last():


    global player_profit_loss  
    global player_win_track
    #global result_label
    global player_win_track_label
    global player_profit_loss_label
    global player_win_ratio_label
    global player_hand_label
    global display_bet
    if player_statues == 'win':
        player_win_track +=1
        player_profit_loss = player_profit_loss + total_player_bets_d 
    elif player_statues == 'even':
        player_win_track +=1/2
        player_profit_loss = player_profit_loss + (1/2) * total_player_bets_d 
    elif player_statues == 'BlackJack':
        player_win_track +=1
        player_profit_loss = player_profit_loss + (3/2) * total_player_bets_d               
    else:
        player_profit_loss = player_profit_loss - total_player_bets_d
    global dealer_hide_hand_label
    dealer_hide_hand_label = Label(root, text = "Dealer hide card: "+str(dealer_hide_card))
    canvas1.create_window(280, 360, window=dealer_hide_hand_label)
    root.update() 
    global player_win_ratio
    global Game_Round
    player_win_ratio = (player_win_track/Game_Round) * 100
    print('player win ratio is ' +str(player_win_ratio)+ ' percents') 
    print('player total profit/ loss is: ' + str(player_profit_loss))
    if Game_Round > 1:
        player_win_track_label.destroy()
        root.update() 
    player_win_track_label = Label(root, text = "Player win tracker: "+str(player_win_track))
    canvas1.create_window(1000, 130, window=player_win_track_label)
    root.update()
    if Game_Round > 1:
        player_profit_loss_label.destroy()
        root.update()                            
    player_profit_loss_label = Label(root, text = 'player total profit/ loss is: ' + str(player_profit_loss))
    canvas1.create_window(1000, 250, window=player_profit_loss_label) 
    root.update()
    if Game_Round > 1:
        player_win_ratio_label.destroy()
        root.update()  
    player_win_ratio_label = Label(root, text = 'player win ratio is ' +str(player_win_ratio)+ ' percents')
    canvas1.create_window(1000, 275, window=player_win_ratio_label) 
    root.update()                               
    global dealer_all_hand_label
    dealer_all_hand_label = Label(root, text = "dealer hand, after dealer hitted is: \n"+str(all_dealer_card))
    canvas1.create_window(300, 600, window=dealer_all_hand_label)                              
    root.update()                             
    print('************************************************ NEXT ROUND ************************************************')
    Game_Round = Game_Round +1
    try:
        round_label.destroy()
        root.update()
    except NameError:
        pass
    round_label = Label(root, text = "Round: "+str(Game_Round))
    canvas1.create_window(1000, 100, window=round_label)   
    root.update() 
    try:
        display_bet.destroy()
        root.update()
    except NameError:
        pass                            
    try:
        total_bet_label_dd.destroy()
        root.update()
    except NameError:
        pass  
    b = 0
    display_bet = Label(root, text = ("Player bet amount for this round:  $"+str(b)))
    canvas1.create_window(1000, 150, window=display_bet)                            
    root.update()                                                       
    hit_b.destroy()    
    #root.update()
    stand_b.destroy()
    root.update() 
    time.sleep(3) 
    player_hand_label_f.destroy()
    #root.update()
    try: 
        result_label.destroy()
        root.update() 
    except NameError:
        pass 
    try: 
        player_hand_label.destroy()
        root.update() 
    except NameError:
        pass         
        
    try: 
        dealer_hand_label.destroy()
        root.update() 
    except NameError:
        pass 

    try: 
        dealer_hide_hand_label.destroy()
        root.update() 
    except NameError:
        pass 

    try: 
        dealer_all_hand_label.destroy()
        root.update() 
    except NameError:
        pass         
    #root.update() 
    
    #root.update() 
    
    #root.update() 
    
    root.update()                           
    Get_Bet()
   

#start USER INTERFACE
try:
    root= Tk.Tk()
except AttributeError:
    root = tk.Tk()

root.title('BlackJack')
canvas1 = tk.Canvas(root, width = 1200, height = 800)
canvas1.pack()

def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Game','Are you sure you want to exit the Game',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        tk.messagebox.showinfo('Return','You will now return to the Game screen')
        

#### get the player name 
error_track = 0
def getInput():                                                     
    global var     #### player name
    global error_track
    global display_name
    global player_name
    var = entry_var.get()
    if len(var)> 0:
        l1.destroy()
        b1.destroy()
        entry_widget.destroy()
        display_name = Label(root, text = ("Player Name is:  "+str(var)))
        player_name = var
        canvas1.create_window(140, 20, window=display_name)
        main_game()
    if len(var) == 0:
        error_track +=1
        print(error_track)
        time.sleep(0.01)
        global l
        if error_track < 2:
            l = Label(root, text = "PLEASE ENTER YOUR NAME")
            canvas1.create_window(600, 500, window=l)
    if error_track>0 and len(var)> 0:

        l.destroy()           
        l1.destroy()
        b1.destroy()
        entry_widget.destroy()
        display_name = Label(root, text = ("Player Name is:  "+str(var)))
        player_name = var
        canvas1.create_window(140, 20, window=display_name)
        main_game()
        
def start():
    var = None
    button1.destroy()
    button2.destroy()
    global l1
    l1 = Label(root, text = "Player Name")
    canvas1.create_window(600, 240, window=l1)
    global entry_var
    entry_var = tk.StringVar()
    global entry_widget
    entry_widget = tk.Entry(root, textvariable=entry_var)
    canvas1.create_window(600, 300, window=entry_widget)
    global b1
    b1 = tk.Button (root, text='submit',command=getInput)
    canvas1.create_window(600, 400, window=b1)
    

button1 = tk.Button (root, text='Exit',command=ExitApplication,bg='brown',fg='black')
button2 = tk.Button (root, text='Start Game',command=start,bg='green',fg='black')
canvas1.create_window(600, 300, window=button1)
canvas1.create_window(600, 200, window=button2)

  
root.mainloop()







