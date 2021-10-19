#import assets for hangman
#Original Code by Delightful Dunlin and  Eager Elk 
# Lighting functionality written by peppe8o
#Modified 10/19/2021
import random
import peppelight.py as pep

#comment out the original way to display hangman
#def display_hangman(attempts):
#    stages = [  """
#                   --------
#                   |      |
#                   |      
#                   |     
#                   |      
#                   |     
#                   -
#                   """,
#                   """
#                   --------
#                   |      |
#                   |      O
#                   |     
#                   |      
#                   |     
#                   -
#                   """,
#                  """
#                  --------
#                  |      |
#                  |      O
#                  |      |
#                  |      |
#                   |
#                   -
#                   """,
#                   """
#                   --------
#                   |      |
#                   |      O
#                   |     /|
#                   |      |
#                   |
#                   -
#                   """,
#                   """
#                   --------
#                   |      |
#                   |      O
#                   |     /|\  
#                   |      |  
#                   |
#                   -
#                   """,
#                   """
#                   --------
#                   |      |
#                   |      O
#                   |     /|\   
#                   |      |   
#                   |     /    
#                   -
#                   """,
#                   """
#                   --------
#                  |      |
#                   |      O
#                   |     /|\-
#                   |      |
#                   |     / \  
#                   -
#                   """
#    ]
#    return stages[attempts]

#Display hangman with LEDs

def display_hangman(attempts):
    stages=[
       [["11111111"],\
       ["11111111"],\
       ["11111111"],\
       ["11111111"],\
       ["11111111"],\
       ["11111111"],\
       ["11111111"],\
       ["11111111"]],

       [["11110111"],\
       ["11101011"],\
       ["11110111"],\
       ["11111111"],\
       ["11111111"],\
       ["11111111"],\
       ["11111111"]
       ["11111111"]],

       [["11110111"],\
       ["11101011"],\
       ["11110111"],\
       ["11110111"],\
       ["11110111"],\
       ["11110111"],\
       ["11111111"]
       ["11111111"]],

       [["11110111"],\
       ["11101011"],\
       ["11110111"],\
       ["11000111"],\
       ["11110111"],\
       ["11110111"],\
       ["11111111"]
       ["11111111"]],

       [["11110111"],\
       ["11101011"],\
       ["11110111"],\
       ["11000001"],\
       ["11110111"],\
       ["11110111"],\
       ["11111111"]
       ["11111111"]],

       [["11110111"],\
       ["11101011"],\
       ["11110111"],\
       ["11000001"],\
       ["11110111"],\
       ["11110111"],\
       ["11101111"]
       ["11011111"]],

       [["11110111"],\
       ["11101011"],\
       ["11110111"],\
       ["11000001"],\
       ["11110111"],\
       ["11110111"],\
       ["11101011"]
       ["11011101"]]
            ]
       return stages[attempts]


#extract random word from the text file
def selection(name):
    file = open ("hangmanlist.txt", "r+")
    random_word = random.choice(file.read().split())
    file.close()
    return random_word

random_word=selection("hangman_list.txt")


#Display random word
def word_selected_dashed():
    word_selected_dashed = []
    for i in range(len(random_word)):
        word_selected_dashed.append('_')
    return ''.join(word_selected_dashed)

word_selected_dashed = word_selected_dashed()
print(word_selected_dashed)

chances = 7

guessed_word = list(word_selected_dashed)

while chances > 0:
    if ''.join(guessed_word) == random_word:
        print("Congraluations, you have guessed the correct word")
        break

    print('You have got '+ str(chances)+ ' wrong chances ')
    user_guessed_letter = input('Guess a letter >>>>> \n')


    if user_guessed_letter in random_word:
        print('Correct!')
        for i in range(len(random_word)):
            if list(random_word)[i] == user_guessed_letter:
                guessed_word[i] = user_guessed_letter
        print(''.join(guessed_word))

    elif user_guessed_letter not in random_word:
        print('Incorrect!')
        chances -= 1
        hang = display_hangman(attempts=(6-chances))
        print(hang)
if chances == 0 :
    print('Sorry, you have ran out of chances')
