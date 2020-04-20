#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import time

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
          'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


        


# In[2]:


class Deck:
    def __init__(self):
        self.deck = []
        for i in suits:
            for j in ranks:
                self.deck.append([i,j])
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def printdeck(self):
        for i,j in enumerate(self.deck):
            print(i,j)
    
    def popcard(self):
        return self.deck.pop()
        
            
        
        


# In[3]:


class Hand:
    def __init__(self):
        self.player_cards = []
        self.dealer_cards = []
        
        self.player_values = [0]
        self.dealer_values = [0]
        


    def distribute(self,a,b,c,d):
        self.player_cards.extend([a,c])
        self.dealer_cards.extend([b,d])
        
    

    def add_values(self,val,player):
        self.val = val
        self.player = player
        
        if self.player == 0 :
            
            self.player_values.append(self.val)
        else:
            self.dealer_values.append(self.val)
            
    def add_card(self,a):
        self.player_cards.append(a)
    def add_card_d(self,a):
        self.dealer_cards.append(a)
        
    def get_values(self,player):
        if player == 0:
            return self.player_values
        else:
            return self.dealer_values




            
    
    def printcard(self,hide_card = False):
        
        self.hide_card = hide_card
        
        print("\nPlayers Cards :-\n")
        
        for j,i in enumerate (self.player_cards):
            print(f"{i[1]} of {i[0]} : {self.player_values[j+1]}")
        print(f"Total : {sum(self.player_values)}")
        
        print("_________________________")
        
        print("\nDealers Cards :-\n")
                
        for j,i in enumerate (self.dealer_cards):
            if self.hide_card and j == 0 :
                print("Hidden Card")#hide it
            else:
                print(f"{i[1]} of {i[0]} : {self.dealer_values[j+1]}")
        if self.hide_card == False :
            print(f"Total : {sum(self.dealer_values)}")
                
        
        
        print("********************************************************************")
            
            
        
        
    


# In[4]:


def value_evaluator(a,player,han):
    for key in values:
        if a == key:
            if key == 'Ace':
                player_sum=sum(han.get_values(player))
                if (player_sum + 11) > 21 and 1 not in han.get_values(player):
                    return 1
                else:
                    return 11
                
            else:
                return values[key]


# In[5]:


class Chip:
    def __init__(self,money):
        self.account = money
        
    def bet(self,wage):
        self.wage = wage
        self.account = self.account - self.wage
                
    def show_account_balance(self):
        return self.account
    
    def player_win(self):        
        self.account = self.account + (self.wage * 2)
        
    def push(self):
        self.account = self.account + self.wage
        


# In[6]:


def win_or_burst(chips,han,natural=False,p1c=False,p2c = False):
    p1=han.get_values(0)
    p2=han.get_values(1)
    
    if p1c == True:
        if sum(p1) == 21 and sum(p2) == 21 and natural == True:
            print("PUSH")
            chips.push()
            return False
        elif sum(p1) == 21 and sum(p2) < 21 and natural == True:
            print("Natural Win : Player")
            chips.player_win()
            return False
        elif sum(p1) == 21 and sum(p2) < 21:
            print("Win : Player")
            chips.player_win()
            return False
        elif sum(p1) > 21:
            if 11 == p1[1] and 1 not in p1:
                p1[1] = 1
                if sum(p1)<21:
                    return True
                elif sum(p1) == 21:
                    print("Win : Player")
                    chips.player_win()
                    return False
                else:
                    print("Burst : Player")
                    return False
            elif 11 ==p1[2] and 1 not in p1:
                p1[2] = 1
                if sum(p1)<21:
                    return True
                elif sum(p1) == 21:
                    print("Win : Player")
                    chips.player_win()
                    return False
                else:
                    print("Burst : Player")
                    
                    return False

                
                
            else:
                print("Burst : Player")
                return False
                
        else:
            return True
    
    if p2c == True:
        

        if sum(p2) > 21:
            if 11 == p2[1] and 1 not in p2 :
                p2[1] = 1
                if sum(p2)<21:
                    return True
                elif sum(p2) == 21:
                    print("Win : Dealer")                    
                    return False
                else:
                    print("Burst : Dealer")
                    chips.player_win()
                    return False
            elif 11 == p2[2] and 1 not in p2:
                p2[2] = 1
                if sum(p2)<21:
                    return True
                elif sum(p2) == 21:
                    print("Win : Dealer")                    
                    return False
                else:
                    print("Burst : Dealer")
                    chips.player_win()
                    return False                                
            else:
                print("Burst : Dealer")
                chips.player_win()
                return False
            
        elif sum(p2) > sum(p1):
            print("Win : Dealer")
            return False
        elif sum(p2) == 21 and sum(p1) < sum(p2):
            print("Win : Dealer")
            return False
        elif sum(p1)>17 and sum(p2)>=17 and sum(p2)<sum(p1):
            print("Win : Player")
            chips.player_win() 
            return False
        elif sum(p1)>=17 and sum(p2)>=17 and sum(p2)==sum(p1):
            print("Push")
            chips.push() 
            return False
        elif sum(p2) < 17 and sum (p1) >17:
            return True
        elif sum(p2)>= 17 and sum(p1) > sum(p2):
            print("Win : Player")
            chips.player_win()
            return False
        
        else:
            return True
        
        
    


# In[7]:


def stand(chips,dec,han):
    p1=han.get_values(0)
    p2=han.get_values(1)
    r = True
    

    
    while r == True  :
        r=win_or_burst(chips,han,False,False,True)
        if r == False:
            return

        a=dec.popcard()
        han.add_card_d(a)
        a1=value_evaluator(a[1],1,han)
        han.add_values(a1,1)
        print("Dealer takes card..")
        han.printcard()


        


    
    return
            
        


# In[8]:


def hit(chips,dec,han):

    
        
    a=dec.popcard()
    han.add_card(a)
    a1=value_evaluator(a[1],0,han)
    han.add_values(a1,0)
    

    
    han.printcard(True)
    r=win_or_burst(chips,han,False,True)
    
    return r
    
    


# In[9]:


def main(chips,dec,han):
    r=True
    while r == True:
        move=int(input("Press [1] to Hit\nPress [2] to Stand\n"))
        if move == 1:
            r = hit(chips,dec,han)
        else:
            break
    if r == True:
        
        stand(chips,dec,han)
        
    han.printcard(False)
        
    
        
    
    
    return
        
        
    
    
    
    
    

    
    
    


# In[ ]:


if __name__=="__main__":
    
    new_game = True
    
    while new_game == True:
        print("BLACKJACK")
        dec = Deck()
        o=1
        new_round = True
        
        while new_round == True:
            
            print("Shuffling..")
            dec.shuffle()
            if o == 1:
                money = int(input("Enter total amount of chips : "))    
                chips = Chip(money)
                o=o+1
            print("Balance : ",chips.show_account_balance())
            t = True
            while  t ==True:
                wage = int(input("Bet wage : "))
                if wage <= chips.show_account_balance():
                    chips.bet(wage)
                    t = False
                else:
                    t=True
                    print("OOPs you dont have enough chips!")




            # Distribute 2 cards per player
            a=dec.popcard()
            b=dec.popcard()
            c=dec.popcard()
            d=dec.popcard()

            han  = Hand() 
            han.distribute(a,c,b,d) # add cards

            a1=value_evaluator(a[1],0,han)
            b1=value_evaluator(b[1],0,han)# evaluate card value
            c1=value_evaluator(c[1],1,han)    
            d1=value_evaluator(d[1],1,han)



            han.add_values(a1,0)
            han.add_values(b1,0)  #add card values
            han.add_values(c1,1)
            han.add_values(d1,1)




            v1=win_or_burst(chips,han,True,True)
            han.printcard(True)

            if v1 == False :
                pass
            else:

                main(chips,dec,han)
                print("Balance : ",chips.show_account_balance())
            if chips.show_account_balance() == 0:
                print("You ran out of Chips\nMatch Ends")
                new_round = False
            else:
                
                
                nr=int(input("Continue Match? [1]\nEnd Match [2]"))
                if nr == 1:
                    new_round =True
                else:
                    new_round = False

        ng=int(input("Start new game [1]\nEnd game [2]\n"))
        if ng == 1:
            new_game = True
        else:
            break
            
            
    
    print("FIN.")


        
        


# In[ ]:





# In[ ]:




