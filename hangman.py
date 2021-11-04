#import assets for hangman
#Original Code by Delightful Dunlin and  Eager Elk 
#Change lighting to use sense hat
#Modified 10/19/2021
#Changes since as of Nov 2: Import in letters.py as replacment for light funtion
#Letters permits cycling through a list while displaying it o the pi
import random
import letters.py as alp
import hangman_stages as display_hangman

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
sense.show_message(word_selected_dashed)

chances = 7

guessed_word = list(word_selected_dashed)

while chances > 0:
    if ''.join(guessed_word) == random_word:
        sense.show_message("Congraluations, you have guessed the correct word", text_colour=[0,255,0])
        break

    sense.show_message('You have got '+ str(chances)+ ' wrong chances ', text_colour=[255,0,0])
    user_guessed_letter = input('Guess a letter >>>>> \n')


    if user_guessed_letter in random_word:
        sense.show_message('Correct!', text_colour=[0,255,0])
        for i in range(len(random_word)):
            if list(random_word)[i] == user_guessed_letter:
                guessed_word[i] = user_guessed_letter
        sense.show_message(''.join(guessed_word))

    elif user_guessed_letter not in random_word:
        sense.show_message('Incorrect!', text_colour=[0,255,0])
        chances -= 1
        hang = display_hangman(attempts=(6-chances))
        sense.show_message(hang)
if chances == 0 :
    sense.show_message('Sorry, you have run out of chances', text_colour=[255,0,0])
