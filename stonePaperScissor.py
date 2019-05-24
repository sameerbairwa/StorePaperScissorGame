#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:22:26 2019

@author: Sameer Bairwa
"""

import random 
def print_menu():
    
    print("Enter 1 for stone")
    print("Enter 2 for paper")
    print("Enter 3 for scissor")

print("Enter 1 to Play")
x = int(input())
if(x==1):  
    score1=score2=0 
    while(score1 < 5 and score2 < 5):
        try:
            print_menu()
            user = int(input("Enter your choice: "))
            computer = random.randint(1,3)
            choice = [1,2,3]
            if(user in choice):
                if(user == 1):
                    print("You choose stone")
                elif(user == 2):
                    print("You choose paper")
                else:
                    print("You choose scissor")
                if(computer == 1):
                    print("Computer choose stone")
                elif(computer == 2):
                    print("Computer choose paper")
                else:
                    print("Computer choose scissor")
                if(user==computer):
                    print("draw")
                elif(user==1 and computer==2):
                    print("Uggh!! I Lost this round")
                    score2 = score2 +1
                elif(user==1 and computer==3):
                    score1 = score1 +1
                    print("Yes!!! I win this round")
                elif(user==2 and computer==3):
                    score2 = score2 + 1
                    print("Uggh!! I Lost this round")
                elif(user==2 and computer==1):
                    score1 = score1 +1
                    print("Yes!!! I win this round")
                elif(user==3 and computer==1):
                    score2 = score2 + 1
                    print("Uggh!! I Lost this round")
                elif(user==3 and computer==2):
                    score1 = score1 +1
                    print("Yes!!! I win this round")
                print("---Scores---")
                print("User:",score1)
                print("Computer:",score2)
                print("------------------")
            else:
                print("Please Enter right choice")
        except:
            print("Please try again")
  
    if(score1==5):
        print("You won the match")
    else:
        print("You lost the match")
    