#!/usr/bin/env python
# coding: utf-8

# Guess Game

# In[ ]:


import random as r 
# first imported the module 

num = r.randrange(50)
Guess = 5

while Guess >= 0:
    your_guess =int(input("Please Enter your Guess Number"))
    
    def check(x):
        #Functation is checking the Guesses
        if your_guess == x:
            print ('Winner')
        elif your_guess > x:
                print('your Guess is little close, Keep trying lower')
        else :
                print('your Guess is little close, Keep trying higher')

    if Guess > 1:
            check (num)
    elif Guess == 1:
            check(num)
            print(' but this is your last chance please choose wisely')
    else:
        print("you loose keep trying best of luck for Next time ")
    Guess = Guess - 1


# ![image.png](attachment:image.png)

# In[ ]:




