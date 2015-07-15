import random

# Ex D.1: -->
def make_random_code():
    '''
    Creates a random 4-letter code. 
    
    Arguments:       None. 
    
    Return value:    A random 4-letter string
    '''
    choice = ['R','G','B','Y','O','W'] 
    code = ''
    for i in range(4):
         code += random.choice(choice)
    return code

# Ex D.2: -->
def count_exact_matches(co, gu):
    '''
    Counts the number of colors in the guess code that are in the same
    location as the secret code. 
    
    Arguments:        co: Secret code string
                      gu: Guess code string
                      
    Return value:     An integer representing exact number of matches
    '''
    code1 = list(co)
    guess1 = list(gu)
    n = 0 
    for i in range(4):
        if code1[i] == guess1[i]:
            n += 1
    return n

# Ex D.3: -->
def count_letter_matches(cod, gue):
    '''
    Counts the number of colors common between the secret and guess codes, 
    without taking into account their location. 
    
    Arguments:       cod: secret code string
                     gue: guess code string
                    
    Return value:    An integer representing number of color code matches
                     in the two strings
    '''
    code2 = list(cod)
    guess2 = list(gue)
    n = 0
    for i in code2:
        if i in guess2:
            n += 1
            guess2.remove(i)
    return n
    #for i in range(4):
        #for j in range(4):
            #if code2[i] == guess2[j]:
                #n += 1
                #guess2[j] = '-'
                #break
    #return n

# Ex D.4: -->
def compare_codes(code, guess):
    '''
    Compares the secret and guess codes for number of exact matches-'b' (color 
    and location), color matches-'w' (without location), and no matches-'-'.
    
    Arguments:        code: secret code string
                      guess: guess code string
                      
    Return value:     4-letter string representing how well the two codes match
    '''
    b = count_exact_matches(code,guess)
    w = count_letter_matches(code,guess) - b
    bl = 4 - b - w
    return (b * 'b') + (w * 'w') + (bl * '-')
    
# Ex D.5: -->
def run_game():
    '''
    Runs the Mastermind board game. 
    
    Arguments:       None 
    
    Return value:    4-letter string that tells you how well the codes match
    '''
    print 'New game'
    secret_code = make_random_code()
    n = 0
    while True:
        user_guess = raw_input("Enter your guess: ")
        evl = compare_codes(secret_code, user_guess)
        print 'Result: %s' %evl
        n += 1
        if evl == 'bbbb':
            print 'Congratulations! You cracked the code in %d moves' %n
            break
    print 'Game over!'