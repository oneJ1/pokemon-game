# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 18:01:10 2021

@author: Jaewon
"""

import time

import pandas as pd

import sys

import random

#CE Project by Jaewon Kim

#My take on the classic Gameboy Game, Pokemon, it simplifies a lot of mechanics as it would be too complicated to implement everything
#Hopefully there are no gamebreaking bugs :)

#Step 1 - Using pandas to import both data sets of Pokemon & movesets

df = pd.read_csv("FirstGenPokemon.csv")

All_Moveset = pd.read_csv("All_Moves.csv")

Loc_Moveset = All_Moveset.loc[(All_Moveset.Gen < 2) & (All_Moveset.Category != 'Status') & (All_Moveset.Power != '-')]

Moveset = Loc_Moveset[['Name', 'Type', 'Power']]
   
#Creating Arrays

Party_array = []

#Aesthetic functions

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
        
def space():
    print('')
    print('')

#Step 2 

class Bag:
    def __init__(self, Money, Pokeballs, Potions, Badges):
        self.Money = Money
        self.Pokeballs = Pokeballs
        self.Potions = Potions
        self.Badges = Badges
        
    def losePotion(self):
        self.Potions -= 1
        
    def losePokeball(self):
        self.Pokeballs -= 1
        
    def gymWin(self):
        self.Badges += 1
        
    def Win(self, otherLv):
        
        print("You gained:", 20*otherLv, "$")               
        self.Money += 20*otherLv
        
    def Pokecenter(self):
            
        space()
            
        print_slow("Welcome to the Pokecenter!")
            
        space()
            
        print_slow("What interests you here?")
            
        space()
            
        print("Pokeballs - Potions - Heal - Exit")
            
        while True:
            user_input = input("Input: ")
        
            space()
                
            if user_input == 'Pokeballs':
            
                print_slow("Pokeballs are 120$. How many Pokeballs would you like to buy?")
            
                space()
            
                print("Money:", self.Money)
            
                while True:
                    
                    user_input_2 = input("Input: ")
                                
                    space()
                    
                    if user_input_2.isalpha():
                        print("Please enter a round integer.")
                
                    else: 
                        if self.Money - int(user_input_2)*120 >= 0:
                        
                            self.Pokeballs += int(user_input_2)
                        
                            self.Money -= int(user_input_2)*120
                        
                            return print_slow("Thanks for shopping!")
                      
                        else:
                            print("You don't have enough money for that! Shoo!")
                            
                            return

                                
            elif user_input == 'Potions':
            
                print_slow("Potions (+50 HP) are 80$. How many Potions would you like to buy?")
            
                space()
            
                print("Money:", self.Money)
            
                while True:
                    user_input_2 = input("Input: ")
                
                    space()
                
                    if user_input_2.isalpha():
                        print("Please enter a round integer.")
                    
                    else: 
                        if self.Money - int(user_input_2)*80 >= 0:
                        
                            self.Potions += int(user_input_2)
                        
                            self.Money -= int(user_input_2)*80
                        
                            return print_slow("Thanks for shopping!")

                        else:
                            print("You don't have enough money for that! Shoo!")
                            
                            return
                        
            elif user_input == 'Heal':
                
                print('.')
                time.sleep(1)
            
                print('.')
                time.sleep(1)
            
                print('.')
                time.sleep(1)
                
                space()
                
                if len(Party_array) == 1:
                
                    Party_array[0].maxHP = Party_array[0].Lv * Party_array[0].HP
        
                elif len(Party_array) == 2:
                    
                    Party_array[0].maxHP = Party_array[0].Lv * Party_array[0].HP
                    Party_array[1].maxHP = Party_array[1].Lv * Party_array[1].HP
        
                elif len(Party_array) == 3:
                    
                    Party_array[0].maxHP = Party_array[0].Lv * Party_array[0].HP
                    Party_array[1].maxHP = Party_array[1].Lv * Party_array[1].HP
                    Party_array[2].maxHP = Party_array[2].Lv * Party_array[2].HP
        
                elif len(Party_array) == 4:
                
                    Party_array[0].maxHP = Party_array[0].Lv * Party_array[0].HP
                    Party_array[1].maxHP = Party_array[1].Lv * Party_array[1].HP
                    Party_array[2].maxHP = Party_array[2].Lv * Party_array[2].HP
                    Party_array[3].maxHP = Party_array[3].Lv * Party_array[3].HP
        
                elif len(Party_array) == 5:
                
                    Party_array[0].maxHP = Party_array[0].Lv * Party_array[0].HP
                    Party_array[1].maxHP = Party_array[1].Lv * Party_array[1].HP
                    Party_array[2].maxHP = Party_array[2].Lv * Party_array[2].HP
                    Party_array[3].maxHP = Party_array[3].Lv * Party_array[3].HP
                    Party_array[4].maxHP = Party_array[4].Lv * Party_array[4].HP
        
                else:
                
                    Party_array[0].maxHP = Party_array[0].Lv * Party_array[0].HP
                    Party_array[1].maxHP = Party_array[1].Lv * Party_array[1].HP
                    Party_array[2].maxHP = Party_array[2].Lv * Party_array[2].HP
                    Party_array[3].maxHP = Party_array[3].Lv * Party_array[3].HP
                    Party_array[4].maxHP = Party_array[4].Lv * Party_array[4].HP
                    Party_array[5].maxHP = Party_array[5].Lv * Party_array[5].HP
                
                print_slow("All your Pokemon are now fully healed!")
                
                space()
                time.sleep(1)
                
                return
                            
            elif user_input == 'Exit':
                
                print_slow("See you next time!")
                
                time.sleep(1)
                
                return
                                
            else:
                print("Please enter a valid input.")
                
    def displayBag(self):
        
        print("You have", self.Money, "$")
        
        print("You have", self.Pokeballs, "Pokeballs")
            
        print("You have", self.Potions, "Potions")
        
        print("You have", self.Badges, "Badges")
        
Player_Bag = Bag(200,5,0,0)
    
def SuperEffective(move):  
    if move > 1.5:
        print_slow("It's super effective!")
        
        time.sleep(1)
        space()

    elif move > 0.4 and move < 0.6:
        print_slow("It's not very effective...")
        
        time.sleep(1)
        space()

    elif move < 0.1:
        print_slow("There was no effect!")
        
        time.sleep(1)
        space()
    
def addParty(PK):
    
    if len(Party_array) < 6:
        Party_array.append(PK)
        
        space()
        time.sleep(1)
        
        print(PK.Name, 'has been added to your Party.')
        
        time.sleep(1)
        
        return
    
    else:
        print_slow("Your Party is full!")
        
        space()
        
        print_slow("Would you like to release one of your Pokemon?")
        
        space()
        time.sleep(1)
        
        print_slow("Your choices are:")
    
        time.sleep(1)
        space()

        print('Yes - No')
        
        while True:
            user_input = input('Input: ')
            
            if user_input == 'Yes':
                
                space()
                
                print_slow("Which Pokemon would you like to release?")
                
                space()
                
                print_slow("Your choices are:")
    
                time.sleep(1)
                space()

                print('1.', Party_array[0].Name, '2.', Party_array[1].Name, '3.', Party_array[2].Name, '4.', Party_array[3].Name, '5.', Party_array[4].Name, '6.', Party_array[5].Name)
                
                while True:
                    user_input = input("Input your Pokemon's position: ")
                    
                    if user_input == '1':
                        
                        print_slow("Goodbye...")
                        
                        time.sleep(1)
                        print('')
                        
                        print_slow(Party_array[0].Name)
                        
                        Party_array[0] = PK
                        
                        return
          
                    elif user_input == '2':
                        
                        print_slow("Goodbye...")
                        
                        time.sleep(1)
                        print('')
                        
                        print_slow(Party_array[1].Name)
                        
                        Party_array[1] = PK
                        
                        return
                        
                    elif user_input == '3':
                        
                        print_slow("Goodbye...")
                        
                        time.sleep(1)
                        print('')
                        
                        print_slow(Party_array[2].Name)
                        
                        Party_array[2] = PK
                        
                        return
                        
                    elif user_input == '4':
                        
                        print_slow("Goodbye...")
                        
                        time.sleep(1)
                        print('')
                        
                        print_slow(Party_array[3].Name)
                        
                        Party_array[3] = PK
                        
                        return
                        
                    elif user_input == '5':
                        
                        print_slow("Goodbye...")
                        
                        time.sleep(1)
                        print('')
                        
                        print_slow(Party_array[4].Name)
                        
                        Party_array[4] = PK
                        
                        return
                        
                    elif user_input == '6':
                        
                        print_slow("Goodbye...")
                        
                        time.sleep(1)
                        print('')
                        
                        print_slow(Party_array[5].Name)
                        
                        Party_array[5] = PK
                        
                        return
                        
                    else:
                        print("Please enter a valid input.")
                
            elif user_input == 'No':
                return print_slow("The Pokemon you caught was freed back into the Wild.")
            
                space()
                
            else:
                print("Please enter a valid input.")

class Pokemon:
    def __init__(self, Name, Type1, Capt_Rate, HP, Lv, exp, moves):
        self.Name = Name
        self.Type = Type1
        self.Capt_Rate = (Capt_Rate/300)*100
        self.HP = HP
        self.Lv = Lv
        self.exp = 0
        self.moves = moves
        self.maxHP = self.Lv * self.HP
        
    def displaymoves(self):
        
        if len(self.moves) == 1:
            print('1:', self.moves[0].Name, 'Type:', self.moves[0].Type, 'Power:', self.moves[0].Power)
        
        elif len(self.moves) == 2:
            print('1:', self.moves[0].Name, 'Type:', self.moves[0].Type, 'Power:', self.moves[0].Power)
            print('2:', self.moves[1].Name, 'Type:', self.moves[1].Type, 'Power:', self.moves[1].Power)
            
        elif len(self.moves) == 3:
            print('1:', self.moves[0].Name, 'Type:', self.moves[0].Type, 'Power:', self.moves[0].Power)
            print('2:', self.moves[1].Name, 'Type:', self.moves[1].Type, 'Power:', self.moves[1].Power)
            print('3:', self.moves[2].Name, 'Type:', self.moves[2].Type, 'Power:', self.moves[2].Power)
            
        elif len(self.moves) == 4:
            print('1:', self.moves[0].Name, 'Type:', self.moves[0].Type, 'Power:', self.moves[0].Power)
            print('2:', self.moves[1].Name, 'Type:', self.moves[1].Type, 'Power:', self.moves[1].Power)
            print('3:', self.moves[2].Name, 'Type:', self.moves[2].Type, 'Power:', self.moves[2].Power)
            print('4:', self.moves[3].Name, 'Type:', self.moves[3].Type, 'Power:', self.moves[3].Power)
        
        
    def Exp(self, Wild_Lv):
        
        Exp_required = 100*(self.Lv)
    
        if self.Lv >= 2*(Wild_Lv):
            return print_slow("Your Pokemon is overleveled, it gained 0 exp.")
    
        elif Wild_Lv > self.Lv:
            
            print("Your Pokemon gained", 50*(Wild_Lv), 'exp.')
            
            self.exp += 50*(Wild_Lv)
        
        elif Wild_Lv == self.Lv:
            
            print("Your Pokemon gained", 25*(Wild_Lv), 'exp.')
            
            self.exp += 25*(Wild_Lv)
        
        elif self.Lv > Wild_Lv:
            
            print("Your Pokemon gained", 10*(Wild_Lv), 'exp.')
            
            self.exp += 10*(Wild_Lv)
    
        if self.exp >= Exp_required:
            self.exp = self.exp - Exp_required
        
            print('.')
            time.sleep(1)
            
            print('.')
            time.sleep(1)
            
            print('.')
            time.sleep(1)
        
            print_slow("Your Pokemon Leveled up!")
        
            self.Lv += 1
        
            if self.Lv % 4 == 0:
            
                print('.')
                time.sleep(1)
            
                print('.')
                time.sleep(1)
            
                print('.')
                time.sleep(1)
            
                print_slow("Your Pokemon learned a new move!") 
                
                space()
                time.sleep(1)
                
                new_move = Moveset.loc[Moveset.Type == self.Type]
            
                move = new_move.sample(1).reset_index().iloc[0]
                
                space()
                print(move.Name, 'Power:', move.Power)
                
                if len(self.moves) < 4:
                    (self.moves).append(move)
                    
                    return
     
                else:
                    print_slow("Oh no, your Pokemon already has 4 moves learned, do you wish to replace a move with the new one?")
                    
                    space()
                    time.sleep(1)
                          
                    while True:
                        user_input = input("Yes or No: ")
                        
                        if user_input == 'Yes':
                            
                            space()
                            
                            print_slow("Which move?")
                            
                            space()
                            time.sleep(1)
                            
                            self.displaymoves()
                            
                            space()
                            time.sleep(1)
                            
                            while True:
                                user_input_num = input("Input the move's position: ")
                                
                                space()
                                
                                if user_input_num == '1':
                                    self.moves[0] = move
                                    
                                    return print("Your Pokemon learned", move.Name,'!')
                                    
                                elif user_input_num == '2':
                                    self.moves[1] = move
                                    
                                    return print("Your Pokemon learned", move.Name,'!')
                                    
                                elif user_input_num == '3':
                                    self.moves[2] = move
                                    
                                    return print("Your Pokemon learned", move.Name,'!')
                                    
                                elif user_input_num == '4':
                                    self.moves[3] = move
                                    
                                    return print("Your Pokemon learned", move.Name,'!')
                                    
                                else:
                                    print("Please enter a valid input.")
                                    
                        elif user_input == 'No':
                            
                            print_slow("Your Pokemon didn't learn the new move.")
                            
                            return
                        
                        else:
                            print("Please enter a valid input.")
        
                
    def Battle(self, otherPK):
        
        space()
        
        print_slow("////////////")
        space()
        
        print(self.Name)
        print('Type:', self.Type)
        print('HP:', self.maxHP)
        print('Lv:', self.Lv)
        
        time.sleep(2)
        
        print('')
        
        print_slow("/////VS/////")      
        space()
        
        print(otherPK.Name)
        print('Type:', otherPK.Type)
        print('HP:', otherPK.maxHP)
        print('Lv:', otherPK.Lv)
        
        print('')
        
        print_slow("////////////")      
        space()
        
        time.sleep(2)
        
        space()
        
        print_slow("Would you like to fight, switch or heal your Pokemon?")
        
        space()
        
        while True:
            choice = input("Fight, Switch, or Heal: ")
            
            space()
            
            if choice == 'Switch':
                return          
            elif choice == 'Heal':
                if Player_Bag.Potions > 0:
                    
                    print_slow("Which Pokemon would you like to heal?")
                    
                    time.sleep(1)
                    space()
                    
                    displayParty()
                    
                    while True:
                        user_input = input("Input your Pokemon's position: ")
                
                        if int(user_input) > 0 and int(user_input) < 7 :

                            Player_Bag.losePotion()
                            
                            position = int(user_input) - 1
                            
                            time.sleep(1)
                            space()
                            
                            if Party_array[position].Lv * Party_array[position].HP - Party_array[position].maxHP < 50:
                                
                                heal = Party_array[position].Lv * Party_array[position].HP - Party_array[position].maxHP
                                
                                Party_array[position].maxHP += heal
                                
                                print(Party_array[position].Name, 'gained', heal, 'HP.')
                                space()
                                time.sleep(1)
                                return
                                
                            else:     
                                Party_array[position].maxHP += 50
                            
                                print(Party_array[position].Name, 'gained 50 HP.')
                                space()
                                time.sleep(1)
                            
                                return
                        
                        else:
                            print("Please enter a valid input.")

                else:
                    print_slow("You don't have any Potions!")
                    space()
                    return
                
            elif choice == 'Fight':
                while True:   
                    print_slow("Which move would you like to use?")
        
                    time.sleep(1)
                    space()
            
                    self.displaymoves()
        
                    time.sleep(1)
                    space()
            
                    user_input = input("Input the move's position: ")
            
                    if int(user_input) < 5 and int(user_input) > 0:
                
                        move_pos = int(user_input) - 1
                
                        time.sleep(1)
                        space()
                
                        print(self.Name, "used", self.moves[move_pos].Name, '!')
                
                        time.sleep(1)
                        space()
                
                        movetype = self.moves[move_pos].Type
                
                        move_power = float(self.moves[move_pos].Power)
                
                        #Finding the row of the Wild Pokemon being damaged
                
                        move_loc = df.loc[df.Name == otherPK.Name]
                
                        #Finding the multiplier value of the damage taken
                
                        move_multi = move_loc[movetype]
                
                        multiplier = float(move_multi.values)
                
                        SuperEffective(multiplier)
                
                        otherPK.maxHP = otherPK.maxHP - multiplier*(move_power)*(self.Lv/2)
                
                        print(otherPK.Name, 'HP:', otherPK.maxHP)
                
                        space()
                        time.sleep(1)
                
                        if otherPK.maxHP > 0:
                     
                            random_num = random.randint(0,3)
                    
                            Wild_move = otherPK.moves[random_num]
                    
                            Wild_movetype = Wild_move.Type
                    
                            Wild_Power = float(Wild_move.Power)
                    
                            #Finding the row of the Wild Pokemon being damaged
                    
                            Wild_loc = df.loc[df.Name == self.Name]
                                      
                            #Finding the multiplier value of the damage taken
                
                            Wild_multi = Wild_loc[Wild_movetype]    
                    
                            print(otherPK.Name, 'used', Wild_move.Name, '!')
                        
                            time.sleep(1)
                            space()
                    
                            Wild_multiplier = float(Wild_multi.values)
                    
                            SuperEffective(Wild_multiplier)
                    
                            self.maxHP = self.maxHP - Wild_multiplier*(Wild_Power)*(otherPK.Lv/2)
                    
                            print(self.Name, 'HP:', self.maxHP)
                    
                            space()
                            time.sleep(1)
                    
                            if self.maxHP < 0:
                        
                                print_slow("Oh no, your Pokemon fainted!")
                                space()
                        
                                return   
                            
                            break
                        
                        else:               
                            print_slow("The Pokemon you were battling fainted!")
                    
                            time.sleep(1)
                            space()
                    
                            Player_Bag.Win(otherPK.Lv)
                    
                            time.sleep(1)
                            space()
                    
                            Pokemon.Exp(self, otherPK.Lv)
                    
                            return                           
                    else:
                        print("Please enter a valid input.")
            
            else:
                print("Please enter a valid input.")
                          
#################################################################################################

class Gym_leader:
    def __init__(self, Name, Type, Party):
        self.Name = Name
        self.Type = Type
        self.Party = Party
        
    def gymFight(self):
        
        i = 0
        
        while (self.Party[i]).maxHP > 0:
            
            init_money = Player_Bag.Money
            
            dead = 0
                
            space()
            time.sleep(1)
                
            print(self.Name, 'sent', (self.Party[i]).Name, 'to fight.')
                
            space()
            time.sleep(1)
                
            print((self.Party[i]).Name, 'Type:', (self.Party[i]).Type, 'HP:', (self.Party[i]).maxHP, 'Lv:', (self.Party[i]).Lv)
                
            space()
            time.sleep(1)
                
            print_slow("Choose a Pokemon from your Party:")
        
            space()
            time.sleep(1)
            
            displayParty()
            
            space()
            time.sleep(1)
            
            user_input = input("Input a number: ")
                    
            if user_input == '1':
                        
                PK_Battle = Party_array[0]
            
                if PK_Battle.maxHP < 1:
                    print_slow("This Pokemon is fainted, it cannot fight!")
                
                    time.sleep(1)
                    space()
                
                else:
                    PK_Battle.Battle(self.Party[i])

            elif user_input == '2':
                        
                PK_Battle = Party_array[1]
            
                if PK_Battle.maxHP < 1:
                    print_slow("This Pokemon is fainted, it cannot fight!")
                
                    time.sleep(1)
                    space()
                
                else:
                    PK_Battle.Battle(self.Party[i])
                        
            elif user_input == '3':
                        
                PK_Battle = Party_array[2]
            
                if PK_Battle.maxHP < 1:
                    print_slow("This Pokemon is fainted, it cannot fight!")
                
                    time.sleep(1)
                    space()
                
                else:
                    PK_Battle.Battle(self.Party[i])
                        
            elif user_input == '4':
                        
                PK_Battle = Party_array[3]
            
                if PK_Battle.maxHP < 1:
                    print_slow("This Pokemon is fainted, it cannot fight!")
                
                    time.sleep(1)
                    space()
                    
                else:
                    PK_Battle.Battle(self.Party[i])
                     
            elif user_input == '5':
                        
                PK_Battle = Party_array[4]
            
                if PK_Battle.maxHP < 1:
                    print_slow("This Pokemon is fainted, it cannot fight!")
                
                    time.sleep(1)
                    space()
                    
                else:
                    PK_Battle.Battle(self.Party[i])
                        
            elif user_input == '6':
                        
                PK_Battle = Party_array[5]
            
                if PK_Battle.maxHP < 1:
                    print_slow("This Pokemon is fainted, it cannot fight!")
                    
                    time.sleep(1)
                    space()
                
                else:
                    PK_Battle.Battle(self.Party[i])
            else:
                print("Please enter a valid input.")
                space() 
                            
            if init_money < Player_Bag.Money:   
                i += 1
                
            space()
                
            if i == len(self.Party):
                break
                
            for a in range(0, len(Party_array)):      
                
                if Party_array[a].maxHP <= 0:
                    dead += 1
                
                if dead == len(Party_array):
                    print_slow("Your whole Party fainted!")
                
                    return
                    
                    
                    
        print_slow("Congratulations, you defeated the Gym leader!")       
        
        space()
        time.sleep(1)
        
        Player_Bag.gymWin()      
        return

def fight(Wild_PK):
    
    while True:
        #Choosing a Pokemon from your Party
        
        init_money = Player_Bag.Money
        
        time.sleep(1)
    
        print_slow("You can choose a Pokemon from your party, decide to Run, or try to catch the Wild Pokemon.")
        
        space()
        time.sleep(1)
            
        displayParty()
            
        space()
        time.sleep(1)
        
        user_input = input("Input a number, Run or Catch: ")
                    
        if user_input == '1':
                        
            PK_Battle = Party_array[0]
            
            if PK_Battle.maxHP < 1:
                print_slow("This Pokemon is fainted, it cannot fight!")
                
                time.sleep(1)
                space()
                
            else:
                PK_Battle.Battle(Wild_PK)

        elif user_input == '2':
                        
            PK_Battle = Party_array[1]
            
            if PK_Battle.maxHP < 1:
                print_slow("This Pokemon is fainted, it cannot fight!")
                
                time.sleep(1)
                space()
                
            else:
                PK_Battle.Battle(Wild_PK)
                        
        elif user_input == '3':
                        
            PK_Battle = Party_array[2]
            
            if PK_Battle.maxHP < 1:
                print_slow("This Pokemon is fainted, it cannot fight!")
                
                time.sleep(1)
                space()
                
            else:
                PK_Battle.Battle(Wild_PK)
                        
        elif user_input == '4':
                        
            PK_Battle = Party_array[3]
            
            if PK_Battle.maxHP < 1:
                print_slow("This Pokemon is fainted, it cannot fight!")
                
                time.sleep(1)
                space()
                
            else:
                PK_Battle.Battle(Wild_PK)
                     
        elif user_input == '5':
                        
            PK_Battle = Party_array[4]
            
            if PK_Battle.maxHP < 1:
                print_slow("This Pokemon is fainted, it cannot fight!")
                
                time.sleep(1)
                space()
                
            else:
                PK_Battle.Battle(Wild_PK)
                        
        elif user_input == '6':
                        
            PK_Battle = Party_array[5]
            
            if PK_Battle.maxHP < 1:
                print_slow("This Pokemon is fainted, it cannot fight!")
                
                time.sleep(1)
                space()
                
            else:
                PK_Battle.Battle(Wild_PK)
            
        elif user_input == 'Run':
            
            space()
            print_slow("You fled safely...")
            
            time.sleep(1)
            space()
            return
        
        elif user_input == 'Catch':
            
            if Player_Bag.Pokeballs > 0:
                
                space()
                print_slow("You throw a Pokeball at the Wild Pokemon-")
                    
                Player_Bag.losePokeball()
                    
                print('')
                print('.')
                time.sleep(1)
            
                print('.')
                time.sleep(1)
            
                print('.')
                time.sleep(1)
                    
                random_chance = random.randint(1,100)
                    
                catch_chance = Wild_PK.Capt_Rate
                    
                if catch_chance >= random_chance:
                    print_slow("You caught the Wild Pokemon!")
                        
                    space()
                    time.sleep(1)
                        
                    addParty(Wild_PK)
                    
                    space()
                    time.sleep(1)
                        
                    return
                    
                else:
                    print_slow("Oh no, the Pokemon broke free!")
                    space()
 
            else:
                print_slow("You don't have any Pokeballs!")    
                space()
            
        else:
            print("Please enter a valid input.")
            space()
         
        if init_money < Player_Bag.Money:
            space()
            time.sleep(1)
                
            return
    
#################################################################################################
    
def displayParty():
    
    if len(Party_array) == 1:
                
        print('1:', Party_array[0].Name, 'Type:', Party_array[0].Type, 'HP:', Party_array[0].maxHP, 'Lv:', Party_array[0].Lv, 'exp:', Party_array[0].exp)
        
        return
        
    elif len(Party_array) == 2:
        
        print('1:', Party_array[0].Name, 'Type:', Party_array[0].Type, 'HP:', Party_array[0].maxHP, 'Lv:', Party_array[0].Lv, 'exp:', Party_array[0].exp)
        print('2:', Party_array[1].Name, 'Type:', Party_array[1].Type, 'HP:', Party_array[1].maxHP, 'Lv:', Party_array[1].Lv, 'exp:', Party_array[1].exp)
        return
        
    elif len(Party_array) == 3:
        
        print('1:', Party_array[0].Name, 'Type:', Party_array[0].Type, 'HP:', Party_array[0].maxHP, 'Lv:', Party_array[0].Lv, 'exp:', Party_array[0].exp)
        print('2:', Party_array[1].Name, 'Type:', Party_array[1].Type, 'HP:', Party_array[1].maxHP, 'Lv:', Party_array[1].Lv, 'exp:', Party_array[1].exp)
        print('3:', Party_array[2].Name, 'Type:', Party_array[2].Type, 'HP:', Party_array[2].maxHP, 'Lv:', Party_array[2].Lv, 'exp:', Party_array[2].exp)

        return
        
    elif len(Party_array) == 4:
                
        print('1:', Party_array[0].Name, 'Type:', Party_array[0].Type, 'HP:', Party_array[0].maxHP, 'Lv:', Party_array[0].Lv, 'exp:', Party_array[0].exp)
        print('2:', Party_array[1].Name, 'Type:', Party_array[1].Type, 'HP:', Party_array[1].maxHP, 'Lv:', Party_array[1].Lv, 'exp:', Party_array[1].exp)
        print('3:', Party_array[2].Name, 'Type:', Party_array[2].Type, 'HP:', Party_array[2].maxHP, 'Lv:', Party_array[2].Lv, 'exp:', Party_array[2].exp)
        print('4:', Party_array[3].Name, 'Type:', Party_array[3].Type, 'HP:', Party_array[3].maxHP, 'Lv:', Party_array[3].Lv, 'exp:', Party_array[3].exp)
          
        return
        
    elif len(Party_array) == 5:
                
        print('1:', Party_array[0].Name, 'Type:', Party_array[0].Type, 'HP:', Party_array[0].maxHP, 'Lv:', Party_array[0].Lv, 'exp:', Party_array[0].exp)
        print('2:', Party_array[1].Name, 'Type:', Party_array[1].Type, 'HP:', Party_array[1].maxHP, 'Lv:', Party_array[1].Lv, 'exp:', Party_array[1].exp)
        print('3:', Party_array[2].Name, 'Type:', Party_array[2].Type, 'HP:', Party_array[2].maxHP, 'Lv:', Party_array[2].Lv, 'exp:', Party_array[2].exp)
        print('4:', Party_array[3].Name, 'Type:', Party_array[3].Type, 'HP:', Party_array[3].maxHP, 'Lv:', Party_array[3].Lv, 'exp:', Party_array[3].exp)
        print('5:', Party_array[4].Name, 'Type:', Party_array[4].Type, 'HP:', Party_array[4].maxHP, 'Lv:', Party_array[4].Lv, 'exp:', Party_array[4].exp)
         
        return
        
    else:
                
        print('1:', Party_array[0].Name, 'Type:', Party_array[0].Type, 'HP:', Party_array[0].maxHP, 'Lv:', Party_array[0].Lv, 'exp:', Party_array[0].exp)
        print('2:', Party_array[1].Name, 'Type:', Party_array[1].Type, 'HP:', Party_array[1].maxHP, 'Lv:', Party_array[1].Lv, 'exp:', Party_array[1].exp)
        print('3:', Party_array[2].Name, 'Type:', Party_array[2].Type, 'HP:', Party_array[2].maxHP, 'Lv:', Party_array[2].Lv, 'exp:', Party_array[2].exp)
        print('4:', Party_array[3].Name, 'Type:', Party_array[3].Type, 'HP:', Party_array[3].maxHP, 'Lv:', Party_array[3].Lv, 'exp:', Party_array[3].exp)
        print('5:', Party_array[4].Name, 'Type:', Party_array[4].Type, 'HP:', Party_array[4].maxHP, 'Lv:', Party_array[4].Lv, 'exp:', Party_array[4].exp)
        print('6:', Party_array[5].Name, 'Type:', Party_array[5].Type, 'HP:', Party_array[5].maxHP, 'Lv:', Party_array[5].Lv, 'exp:', Party_array[5].exp)

        return

def start():
    
    #Creating Gym_Leaders
        
    #Brock
            
    Brock1 = df.loc[df.Name == 'Geodude']
    Brock_1 = Brock1.sample(1).reset_index().iloc[0]
    
    Brock1_Moveset = Moveset.loc[Moveset.Type == Brock_1['Type1']]
                
    Brock1_move_1 = Brock1_Moveset.sample(1).reset_index().iloc[0]
    Brock1_move_2 = Brock1_Moveset.sample(1).reset_index().iloc[0]
    Brock1_move_3 = Brock1_Moveset.sample(1).reset_index().iloc[0]
    Brock1_move_4 = Brock1_Moveset.sample(1).reset_index().iloc[0]
    
    Brock_1st = Pokemon(Brock_1['Name'], Brock_1['Type1'], Brock_1['Capt_Rate'], Brock_1['HP'], 6, 0, [Brock1_move_1, Brock1_move_2, Brock1_move_3, Brock1_move_4])
    
    Brock2 = df.loc[df.Name == 'Onix']
    Brock_2 = Brock2.sample(1).reset_index().iloc[0]
    
    Brock2_Moveset = Moveset.loc[Moveset.Type == Brock_2['Type1']]
                
    Brock2_move_1 = Brock2_Moveset.sample(1).reset_index().iloc[0]
    Brock2_move_2 = Brock2_Moveset.sample(1).reset_index().iloc[0]
    Brock2_move_3 = Brock2_Moveset.sample(1).reset_index().iloc[0]
    Brock2_move_4 = Brock2_Moveset.sample(1).reset_index().iloc[0]
    
    Brock_2nd = Pokemon(Brock_2['Name'], Brock_2['Type1'], Brock_2['Capt_Rate'], Brock_2['HP'], 7, 0, [Brock2_move_1, Brock2_move_2, Brock2_move_3, Brock2_move_4])
            
    Brock = Gym_leader('Brock', 'Rock', [Brock_1st, Brock_2nd])
    
    #Misty
    
    Misty1 = df.loc[df.Name == 'Staryu']
    Misty_1 = Misty1.sample(1).reset_index().iloc[0]
    
    Misty1_Moveset = Moveset.loc[Moveset.Type == Misty_1['Type1']]
                
    Misty1_move_1 = Misty1_Moveset.sample(1).reset_index().iloc[0]
    Misty1_move_2 = Misty1_Moveset.sample(1).reset_index().iloc[0]
    Misty1_move_3 = Misty1_Moveset.sample(1).reset_index().iloc[0]
    Misty1_move_4 = Misty1_Moveset.sample(1).reset_index().iloc[0]
    
    Misty_1st = Pokemon(Misty_1['Name'], Misty_1['Type1'], Misty_1['Capt_Rate'], Misty_1['HP'], 10, 0, [Misty1_move_1, Misty1_move_2, Misty1_move_3, Misty1_move_4])
    
    Misty2 = df.loc[df.Name == 'Starmie']
    Misty_2 = Misty2.sample(1).reset_index().iloc[0]
    
    Misty2_Moveset = Moveset.loc[Moveset.Type == Misty_2['Type1']]
                
    Misty2_move_1 = Misty2_Moveset.sample(1).reset_index().iloc[0]
    Misty2_move_2 = Misty2_Moveset.sample(1).reset_index().iloc[0]
    Misty2_move_3 = Misty2_Moveset.sample(1).reset_index().iloc[0]
    Misty2_move_4 = Misty2_Moveset.sample(1).reset_index().iloc[0]
    
    Misty_2nd = Pokemon(Misty_2['Name'], Misty_2['Type1'], Misty_2['Capt_Rate'], Misty_2['HP'], 11, 0, [Misty2_move_1, Misty2_move_2, Misty2_move_3, Misty2_move_4])
            
    Misty = Gym_leader('Misty', 'Water', [Misty_1st, Misty_2nd])
    
    
    #Erika
    
    Erika1 = df.loc[df.Name == 'Victreebel']
    Erika_1 = Erika1.sample(1).reset_index().iloc[0]
    
    Erika1_Moveset = Moveset.loc[Moveset.Type == Erika_1['Type1']]
                
    Erika1_move_1 = Erika1_Moveset.sample(1).reset_index().iloc[0]
    Erika1_move_2 = Erika1_Moveset.sample(1).reset_index().iloc[0]
    Erika1_move_3 = Erika1_Moveset.sample(1).reset_index().iloc[0]
    Erika1_move_4 = Erika1_Moveset.sample(1).reset_index().iloc[0]
    
    Erika_1st = Pokemon(Erika_1['Name'], Erika_1['Type1'], Erika_1['Capt_Rate'], Erika_1['HP'], 14, 0, [Erika1_move_1, Erika1_move_2, Erika1_move_3, Erika1_move_4])
    
    Erika2 = df.loc[df.Name == 'Tangela']
    Erika_2 = Erika2.sample(1).reset_index().iloc[0]
    
    Erika2_Moveset = Moveset.loc[Moveset.Type == Erika_2['Type1']]
                
    Erika2_move_1 = Erika2_Moveset.sample(1).reset_index().iloc[0]
    Erika2_move_2 = Erika2_Moveset.sample(1).reset_index().iloc[0]
    Erika2_move_3 = Erika2_Moveset.sample(1).reset_index().iloc[0]
    Erika2_move_4 = Erika2_Moveset.sample(1).reset_index().iloc[0]
    
    Erika_2nd = Pokemon(Erika_2['Name'], Erika_2['Type1'], Erika_2['Capt_Rate'], Erika_2['HP'], 14, 0, [Erika2_move_1, Erika2_move_2, Erika2_move_3, Erika2_move_4])
    
    Erika3 = df.loc[df.Name == 'Vileplume']
    Erika_3 = Erika3.sample(1).reset_index().iloc[0]
    
    Erika3_Moveset = Moveset.loc[Moveset.Type == Erika_3['Type1']]
                
    Erika3_move_1 = Erika3_Moveset.sample(1).reset_index().iloc[0]
    Erika3_move_2 = Erika3_Moveset.sample(1).reset_index().iloc[0]
    Erika3_move_3 = Erika3_Moveset.sample(1).reset_index().iloc[0]
    Erika3_move_4 = Erika3_Moveset.sample(1).reset_index().iloc[0]
    
    Erika_3rd = Pokemon(Erika_3['Name'], Erika_3['Type1'], Erika_3['Capt_Rate'], Erika_3['HP'], 16, 0, [Erika3_move_1, Erika3_move_2, Erika3_move_3, Erika3_move_4])
            
    Erika = Gym_leader('Erika', 'Grass', [Erika_1st, Erika_2nd, Erika_3rd])
    
    
    #Blaine
    
    Blaine1 = df.loc[df.Name == 'Growlithe']
    Blaine_1 = Blaine1.sample(1).reset_index().iloc[0]
    
    Blaine1_Moveset = Moveset.loc[Moveset.Type == Blaine_1['Type1']]
                
    Blaine1_move_1 = Blaine1_Moveset.sample(1).reset_index().iloc[0]
    Blaine1_move_2 = Blaine1_Moveset.sample(1).reset_index().iloc[0]
    Blaine1_move_3 = Blaine1_Moveset.sample(1).reset_index().iloc[0]
    Blaine1_move_4 = Blaine1_Moveset.sample(1).reset_index().iloc[0]
    
    Blaine_1st = Pokemon(Blaine_1['Name'], Blaine_1['Type1'], Blaine_1['Capt_Rate'], Blaine_1['HP'], 18, 0, [Blaine1_move_1, Blaine1_move_2, Blaine1_move_3, Blaine1_move_4])
    
    Blaine2 = df.loc[df.Name == 'Ponyta']
    Blaine_2 = Blaine2.sample(1).reset_index().iloc[0]
    
    Blaine2_Moveset = Moveset.loc[Moveset.Type == Blaine_2['Type1']]
                
    Blaine2_move_1 = Blaine2_Moveset.sample(1).reset_index().iloc[0]
    Blaine2_move_2 = Blaine2_Moveset.sample(1).reset_index().iloc[0]
    Blaine2_move_3 = Blaine2_Moveset.sample(1).reset_index().iloc[0]
    Blaine2_move_4 = Blaine2_Moveset.sample(1).reset_index().iloc[0]
    
    Blaine_2nd = Pokemon(Blaine_2['Name'], Blaine_2['Type1'], Blaine_2['Capt_Rate'], Blaine_2['HP'], 19, 0, [Blaine2_move_1, Blaine2_move_2, Blaine2_move_3, Blaine2_move_4])
    
    Blaine3 = df.loc[df.Name == 'Rapidash']
    Blaine_3 = Blaine3.sample(1).reset_index().iloc[0]
    
    Blaine3_Moveset = Moveset.loc[Moveset.Type == Blaine_3['Type1']]
                
    Blaine3_move_1 = Blaine3_Moveset.sample(1).reset_index().iloc[0]
    Blaine3_move_2 = Blaine3_Moveset.sample(1).reset_index().iloc[0]
    Blaine3_move_3 = Blaine3_Moveset.sample(1).reset_index().iloc[0]
    Blaine3_move_4 = Blaine3_Moveset.sample(1).reset_index().iloc[0]
    
    Blaine_3rd = Pokemon(Blaine_3['Name'], Blaine_3['Type1'], Blaine_3['Capt_Rate'], Blaine_3['HP'], 21, 0, [Blaine3_move_1, Blaine3_move_2, Blaine3_move_3, Blaine3_move_4])
    
    Blaine4 = df.loc[df.Name == 'Arcanine']
    Blaine_4 = Blaine4.sample(1).reset_index().iloc[0]
    
    Blaine4_Moveset = Moveset.loc[Moveset.Type == Blaine_4['Type1']]
                
    Blaine4_move_1 = Blaine4_Moveset.sample(1).reset_index().iloc[0]
    Blaine4_move_2 = Blaine4_Moveset.sample(1).reset_index().iloc[0]
    Blaine4_move_3 = Blaine4_Moveset.sample(1).reset_index().iloc[0]
    Blaine4_move_4 = Blaine4_Moveset.sample(1).reset_index().iloc[0]
    
    Blaine_4th = Pokemon(Blaine_4['Name'], Blaine_4['Type1'], Blaine_4['Capt_Rate'], Blaine_4['HP'], 24, 0, [Blaine4_move_1, Blaine4_move_2, Blaine4_move_3, Blaine4_move_4])
            
    Blaine = Gym_leader('Blaine', 'Fire', [Blaine_1st, Blaine_2nd, Blaine_3rd, Blaine_4th])
    
    #The game starts here
    
    space()

    print_slow("Welcome to Kanto!")
    
    space()
    
    print_slow("Here you will catch and train creatures called Pokemon in order to defeat 4 Gyms to win the game!")
    
    space()
    
    print_slow("To begin your adventures, Professor Oak will give you a choice of 3 starter Pokemon.")
    
    space()

    starter1 = df.loc[df.Name == 'Bulbasaur']
    starter_1 = starter1.sample(1).reset_index().iloc[0]

    starter2 = df.loc[df.Name == 'Charmander']
    starter_2 = starter2.sample(1).reset_index().iloc[0]
    
    starter3 = df.loc[df.Name == 'Squirtle']
    starter_3 = starter3.sample(1).reset_index().iloc[0]
    
    Tackle_Loc = Moveset.loc[Moveset.Name == 'Tackle']
    Tackle = Tackle_Loc.sample(1).reset_index().iloc[0]
                     
    print_slow("Your choices are:")
    
    time.sleep(1)
    space()

    print('Bulbasaur - Charmander - Squirtle')
    
    time.sleep(1)
    
    while True:
        user_input = input('Input: ')
        
        if user_input == 'Bulbasaur':
            
            print('')
            
            print_slow("Great! You will begin your adventure with Bulbasaur, a grass type Pokemon.")
            
            Party_1 = Pokemon(starter_1['Name'], starter_1['Type1'], starter_1['Capt_Rate'], starter_1['HP'], 3, 0, [Tackle])
            
            break
        
        elif user_input == 'Charmander':
            
            print('')
            
            print_slow("Great! You will begin your adventure with Charmander, a fire type Pokemon.")
            
            Party_1 = Pokemon(starter_2['Name'], starter_2['Type1'], starter_2['Capt_Rate'], starter_2['HP'], 3, 0, [Tackle])
            
            break
        
        elif user_input == 'Squirtle':
            
            print('')
            
            print_slow("Great! You will begin your adventure with Squirtle, a water type Pokemon.")
            
            Party_1 = Pokemon(starter_3['Name'], starter_3['Type1'], starter_3['Capt_Rate'], starter_3['HP'], 3, 0, [Tackle])
            
            break
        
        else:
            print("Please input the name of one of the starters.")
        
        
    addParty(Party_1)
    
    print_slow("Professor Oak also gives you 200$ along with 5 Pokeballs to begin.")
    
    space()
    time.sleep(1)
    
    print_slow("Professor Oak: Don't forget, Pokemon learn new moves every 4 levels!")
        
    space()
    time.sleep(1)
    
    print_slow("In every city, there are three places to choose from:")
        
    space()
        
    print_slow("Going to the Wild, Going to the Pokecenter, or Challenging the Gym.")
    
    time.sleep(2)
    space()
        
    print_slow("The Wild contains catchable Wild Pokemon that you can defeat to train your own Pokemon.")
    
    time.sleep(2)
    space()
    
    print_slow("The Pokecenter is used to heal your Pokemon and buy Pokeballs/Potions.")
    
    time.sleep(2)
    space()
    
    print_slow("Finally, it is necessary to defeat the city's Gym in order to progress to the next city.")

    time.sleep(2)
    space()
    
#########################################################################################################################################
    
    print_slow("Now, Welcome to Pewter City! You will meet Brock at the Gym who mainly uses Rock-type Pokemon.")
    
    time.sleep(1)
    space()
    
    while True:
        
        print_slow("Your choices are:")
    
        time.sleep(1)
        space()
        
        print('Wild - Pokecenter - Gym - Party - Bag')
        
        user_input = input('Input: ')
        
        space()
        
        if user_input == 'Wild':

            print_slow("You have entered Veridian Forest.")
            
            Pokemon_list_1 = df[(df.Number > 9) & (df.Number < 27)]
            
            random_Pokemon = Pokemon_list_1.sample(1).reset_index().iloc[0]
            
            Wild_Moveset = Moveset.loc[Moveset.Type == random_Pokemon['Type1']]
            
            Wild_move_1 = Wild_Moveset.sample(1).reset_index().iloc[0]
            Wild_move_2 = Wild_Moveset.sample(1).reset_index().iloc[0]
            Wild_move_3 = Wild_Moveset.sample(1).reset_index().iloc[0]
            Wild_move_4 = Wild_Moveset.sample(1).reset_index().iloc[0]
            
            Wild_Pokemon = Pokemon(random_Pokemon['Name'], random_Pokemon['Type1'], random_Pokemon['Capt_Rate'], random_Pokemon['HP'], random.randint(2,5) , 0, [Wild_move_1, Wild_move_2, Wild_move_3, Wild_move_4])
            
            time.sleep(1)
            space()
            
            print('.')
            time.sleep(1)
            
            print('.')
            time.sleep(1)
            
            print('.')
            time.sleep(1)
            
            space()
            
            print_slow("You encountered a wild Pokemon!") 
            
            space()
            
            print(Wild_Pokemon.Name, 'Type:', Wild_Pokemon.Type, 'HP:', Wild_Pokemon.maxHP, 'Lv:', Wild_Pokemon.Lv, 'Capture Rate:', Wild_Pokemon.Capt_Rate, '%')

            space()
            time.sleep(1)
            
            fight(Wild_Pokemon) 


        elif user_input == 'Pokecenter':
            
            Player_Bag.Pokecenter()
            
            space()
            time.sleep(2)
                    
        elif user_input == 'Gym':
            
            print_slow("Brock: In this big world of ours, there must be many tough Trainers. Let's both keep training and making ourselves stronger!")
            
            Brock.gymFight()
            
            #Rehealing the Gym_Leader's Pokemon in case of party fainting
            
            Brock_1st.maxHP = Brock_1st.Lv*Brock_1st.HP
            Brock_2nd.maxHP = Brock_2nd.Lv*Brock_2nd.HP
            
            if Player_Bag.Badges > 0:
                break
            
            space()
            time.sleep(1)
            
        elif user_input == 'Party':
            
            displayParty()
                
            space()
            time.sleep(1)
            
        elif user_input == 'Bag':

            Player_Bag.displayBag()
            
            space()
            time.sleep(1)
            
        else:
            
            print("Please enter a valid input.")
            space()
            
#########################################################################################################################################
    
    print_slow("Now, Welcome to Cerulean City! You will meet Misty at the Gym who mainly uses Water-type Pokemon.")
    
    time.sleep(1)
    space()
    
    while True:
        
        print_slow("Your choices are:")
    
        time.sleep(1)
        space()
        
        print('Wild - Pokecenter - Gym - Party - Bag')
        
        user_input = input('Input: ')
        
        space()
        
        if user_input == 'Wild':

            print_slow("You have entered Mt. Moon.")
            
            Pokemon_list_1 = df[(df.Number > 26) & (df.Number < 52)]
            
            random_Pokemon = Pokemon_list_1.sample(1).reset_index().iloc[0]
            
            Wild_Moveset = Moveset.loc[Moveset.Type == random_Pokemon['Type1']]
            
            Wild_move_1 = Wild_Moveset.sample(1).reset_index().iloc[0]
            Wild_move_2 = Wild_Moveset.sample(1).reset_index().iloc[0]
            Wild_move_3 = Wild_Moveset.sample(1).reset_index().iloc[0]
            Wild_move_4 = Wild_Moveset.sample(1).reset_index().iloc[0]
            
            Wild_Pokemon = Pokemon(random_Pokemon['Name'], random_Pokemon['Type1'], random_Pokemon['Capt_Rate'], random_Pokemon['HP'], random.randint(6,9) , 0, [Wild_move_1, Wild_move_2, Wild_move_3, Wild_move_4])
            
            time.sleep(1)
            space()
            
            print('.')
            time.sleep(1)
            
            print('.')
            time.sleep(1)
            
            print('.')
            time.sleep(1)
            
            space()
            
            print_slow("You encountered a wild Pokemon!") 
            
            space()
            
            print(Wild_Pokemon.Name, 'Type:', Wild_Pokemon.Type, 'HP:', Wild_Pokemon.maxHP, 'Lv:', Wild_Pokemon.Lv, 'Capture Rate:', Wild_Pokemon.Capt_Rate, '%')

            space()
            time.sleep(1)
            
            fight(Wild_Pokemon) 


        elif user_input == 'Pokecenter':
            
            Player_Bag.Pokecenter()
            
            space()
            time.sleep(2)
                    
        elif user_input == 'Gym':
        
            print_slow("Misty: I’m going to keep training here at this Gym. When I get better, I’d love to hit the road and travel.")
            
            Misty.gymFight()
            
            #Rehealing the Gym_Leader's Pokemon in case of party fainting
            
            Misty_1st.maxHP = Misty_1st.Lv*Misty_1st.HP
            Misty_2nd.maxHP = Misty_2nd.Lv*Misty_2nd.HP
            
            if Player_Bag.Badges > 1:
                break
            
            space()
            time.sleep(1)
            
        elif user_input == 'Party':
            
            displayParty()
                
            space()
            time.sleep(1)
            
        elif user_input == 'Bag':

            Player_Bag.displayBag()
            
            space()
            time.sleep(1)
            
        else:
            
            print("Please enter a valid input.")
            space()
            
#########################################################################################################################################
        
    print_slow("Now, Welcome to Celadon City! You will meet Erika at the Gym who mainly uses Grass-type Pokemon.")
    
    time.sleep(1)
    space()
    
    while True:
        
        print_slow("Your choices are:")
    
        time.sleep(1)
        space()
        
        print('Wild - Pokecenter - Gym - Party - Bag')
        
        user_input = input('Input: ')
        
        space()
        
        if user_input == 'Wild':

            print_slow("You have entered Route 7.")
            
            Pokemon_list_1 = df[(df.Number > 51) & (df.Number < 86)]
            
            random_Pokemon = Pokemon_list_1.sample(1).reset_index().iloc[0]
            
            Wild_Moveset = Moveset.loc[Moveset.Type == random_Pokemon['Type1']]
            
            Wild_move_1 = Wild_Moveset.sample(1).reset_index().iloc[0]
            Wild_move_2 = Wild_Moveset.sample(1).reset_index().iloc[0]
            Wild_move_3 = Wild_Moveset.sample(1).reset_index().iloc[0]
            Wild_move_4 = Wild_Moveset.sample(1).reset_index().iloc[0]
            
            Wild_Pokemon = Pokemon(random_Pokemon['Name'], random_Pokemon['Type1'], random_Pokemon['Capt_Rate'], random_Pokemon['HP'], random.randint(10,13) , 0, [Wild_move_1, Wild_move_2, Wild_move_3, Wild_move_4])
            
            time.sleep(1)
            space()
            
            print('.')
            time.sleep(1)
            
            print('.')
            time.sleep(1)
            
            print('.')
            time.sleep(1)
            
            space()
            
            print_slow("You encountered a wild Pokemon!") 
            
            space()
            
            print(Wild_Pokemon.Name, 'Type:', Wild_Pokemon.Type, 'HP:', Wild_Pokemon.maxHP, 'Lv:', Wild_Pokemon.Lv, 'Capture Rate:', Wild_Pokemon.Capt_Rate, '%')

            space()
            time.sleep(1)
            
            fight(Wild_Pokemon) 


        elif user_input == 'Pokecenter':
            
            Player_Bag.Pokecenter()
            
            space()
            time.sleep(2)
                    
        elif user_input == 'Gym':
            
            print_slow("Erika: I am so glad that there are strong Trainers like you. That awareness alone inspires and motivates me to try harder.")
            
            Erika.gymFight()
            
            #Rehealing the Gym_Leader's Pokemon in case of party fainting
            
            Erika_1st.maxHP = Erika_1st.Lv*Erika_1st.HP
            Erika_2nd.maxHP = Erika_2nd.Lv*Erika_2nd.HP
            Erika_3rd.maxHP = Erika_3rd.Lv*Erika_3rd.HP
            
            if Player_Bag.Badges > 2:
                break
            
            space()
            time.sleep(1)
            
        elif user_input == 'Party':
            
            displayParty()
                
            space()
            time.sleep(1)
            
        elif user_input == 'Bag':

            Player_Bag.displayBag()
            
            space()
            time.sleep(1)
            
        else:
            
            print("Please enter a valid input.")
            space()
            
#########################################################################################################################################
    
    print_slow("Now, Welcome to Cinnabar Island! You will meet Blaine at the Gym who mainly uses Fire-type Pokemon.")
    
    time.sleep(1)
    space()
    
    while True:
        
        print_slow("Your choices are:")
    
        time.sleep(1)
        space()
        
        print('Wild - Pokecenter - Gym - Party - Bag')
        
        user_input = input('Input: ')
        
        space()
        
        if user_input == 'Wild':

            print_slow("You have entered Seafoam Islands.")
            
            Pokemon_list_1 = df[(df.Number > 85) & (df.Number < 152)]
            
            random_Pokemon = Pokemon_list_1.sample(1).reset_index().iloc[0]
            
            Wild_Moveset = Moveset.loc[Moveset.Type == random_Pokemon['Type1']]
            
            Wild_move_1 = Wild_Moveset.sample(1).reset_index().iloc[0]
            Wild_move_2 = Wild_Moveset.sample(1).reset_index().iloc[0]
            Wild_move_3 = Wild_Moveset.sample(1).reset_index().iloc[0]
            Wild_move_4 = Wild_Moveset.sample(1).reset_index().iloc[0]
            
            Wild_Pokemon = Pokemon(random_Pokemon['Name'], random_Pokemon['Type1'], random_Pokemon['Capt_Rate'], random_Pokemon['HP'], random.randint(14,20) , 0, [Wild_move_1, Wild_move_2, Wild_move_3, Wild_move_4])
            
            time.sleep(1)
            space()
            
            print('.')
            time.sleep(1)
            
            print('.')
            time.sleep(1)
            
            print('.')
            time.sleep(1)
            
            space()
            
            print_slow("You encountered a wild Pokemon!") 
            
            space()
            
            print(Wild_Pokemon.Name, 'Type:', Wild_Pokemon.Type, 'HP:', Wild_Pokemon.maxHP, 'Lv:', Wild_Pokemon.Lv, 'Capture Rate:', Wild_Pokemon.Capt_Rate, '%')

            space()
            time.sleep(1)
            
            fight(Wild_Pokemon) 


        elif user_input == 'Pokecenter':
            
            Player_Bag.Pokecenter()
            
            space()
            time.sleep(2)
                    
        elif user_input == 'Gym':
            
            print_slow("Blaine: My Fire Pokemon! They'll become even more powerful!")
            
            Blaine.gymFight()
            
            #Rehealing the Gym_Leader's Pokemon in case of party fainting
            
            Blaine_1st.maxHP = Blaine_1st.Lv*Blaine_1st.HP
            Blaine_2nd.maxHP = Blaine_2nd.Lv*Blaine_2nd.HP
            Blaine_3rd.maxHP = Blaine_3rd.Lv*Blaine_3rd.HP
            Blaine_4th.maxHP = Blaine_4th.Lv*Blaine_4th.HP
            
            if Player_Bag.Badges > 3:
                break
            
            space()
            time.sleep(1)
            
        elif user_input == 'Party':
            
            displayParty()
                
            space()
            time.sleep(1)
            
        elif user_input == 'Bag':

            Player_Bag.displayBag()
            
            space()
            time.sleep(1)
            
        else:
            
            print("Please enter a valid input.")
            space()
            
            
    space()
    time
    print_slow("Congratulations, you beat the game!")

start()