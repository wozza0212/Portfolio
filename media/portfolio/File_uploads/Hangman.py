import random


word_list = ['coding', 'research', 'technology', 'python', 'attempt', 'programmer']
used_letters = []
word = random.choice(word_list)


def draw_noose(count):
    noose = {
        0:
            '''
            _____
            |
            |
            |
            |
            |______
            '''
        ,
        1:
            '''
            _____
            |    |
            |
            |
            |
            |______
            ''',
        2:
            '''
            _____
            |    |
            |    O
            |
            |
            |______
            ''',
        3:
            '''
            _____
            |    |
            |    O
            |    |
            |
            |______
            ''',
        4:
            '''
            _____
            |    |
            |    O
            |   -|-
            |
            |______
            ''',
        5:
            r'''
            _____
            |    |
            |    O
            |   -|-
            |     \
            |______
            ''',
        6:
            r'''
            _____
            |    |
            |    O
            |   -|-
            |   / \
            |______
            '''
    }

    print(noose[count])


def draw_the_word():
    print('\n\n\n\n\n')
    word_single = []
    win_check = []
    for letter in word:
        word_single.append(letter)
    for x in word_single:
        if x in used_letters:
            print(x, end=' ')
        else:
            print('_', end=' ')
            win_check.append('_')
    if '_' not in win_check:
        return 'won'
    print('\n')


def guess_letter(count):
    guess_attempt = True
    while guess_attempt:
        print(f'Here are the letters that you have already used: {used_letters} \n')
        guess = input('Please guess one of the letters in the word!').lower()
        if guess in used_letters:
            print('Youv\'e already guess that letter!')
        elif guess.isdigit():
            print('Thats a fucking number idiot')
        elif len(guess) != 1:
            print('Thats more than 1 letter retard')
        else:
            guess_attempt = False
        if guess not in word:
            count += 1
    used_letters.append(guess)
    return count


count = 0

playing = True
while playing:
    draw_noose(count)
    if draw_the_word() == 'won':
        print('\nCongratulations, You have beaten the hangman\'s noose!')
        again = input('Would you like to play again? please enter y or n?')
        if again == 'y':
            used_letters = []
            word = random.choice(word_list)
            count = 0
            draw_the_word()
        else:
            playing = False
    count = guess_letter(count)
    if count >= 6:
        print('Im afraid that\'s game over, You are well and truly hung!')
        again = input('Would you like to play again? Please enter yes or no?')
        if again == 'y':
            used_letters = []
            word = random.choice(word_list)
            count = 0
            draw_the_word()
        else:
            playing = False






