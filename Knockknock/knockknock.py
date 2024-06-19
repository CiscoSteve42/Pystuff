#!/usr/bin/env python3

import sys, random


def main():
    jokes = [
        ('Ligma ', 'LIGMA BALLZZZZ'),
        ('Doctor ', 'I\'m a Tom Baker fan, myself.'),
        ('Pikach ', 'Sorry, I don\'t speak Pokemon.'), 
        ('Sunz ', 'The Art of War! Good read.'),
        ('GNU' , 'Definitely not UNIX!'),
        ('Woo' , 'What are we celebrating?'),
        ('Nobody ', 'NOBODY EXPECTS THE SPANISH INQUISITION!'),
        ('Gok ', 'KAKOROT!!!!!!11'),
        ('Have you head the news of? ', 'Our Lord and Savior, Cthulu'),
        ('Bustin ', 'Usually in your mom.'),
        ('Amnesia patient', 'Seriously, no clue'),
        ('Sh ', 'Well screw you too buddy!'),
        ('The ', 'RIP Keith Moon'),
        ('Boo ', 'Quit whining, geez.')
        #seriously, if you've got anything better add it here
    ]

    while True:
        setup, punchline = random.choice(jokes)

        knock = input('Knock knock: ').strip().lower()

        if knock in ['whos there', 'who\'s there?', 'whos there?', 'who\'s there', 'who dis']:
            answer = (f'{setup}')
            print(answer)
            response = input('You: ')
            if response.endswith('who') or response.endswith('?'):
                print(punchline)
            else:
                print('You\'re supposed to ask WHO it is FFS.')
        else:
            print('I SAID KNOCK KNOCK MOTHERFUCKER')
            continue


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('\nGET OFF MY LAWN! Damn kids.')
