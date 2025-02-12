"""
projekt_2.py: Bulls and Cows game

author: Tobias Svasek
email: 1143@student.itgymnazium.cz
"""

import random

def initiation():

    print('Welcome to the Cows and Bulls Game!')
    print('--' * 20)
    print('I have generated a random 4 digit number \nfor you. Lets play Bulls and Cows!')
    print('--' * 20)
    guess_log = ['']
    answer = random.randint(0, 9999)
    answer = '{0:04d}'.format(answer)
    return guess_log, answer


def get_guess(guess_log):

    guess = input('Enter a number:')
    print('--' * 20)
    guess_log.append(guess)
    return guess_log


def compare(guess, answer):

    cow = 0
    bull = 0
    guess_checked = [False] * 4
    answer_checked = [False] * 4

    # First pass: count cows
    for i in range(4):
        if guess[i] == answer[i]:
            cow += 1
            guess_checked[i] = True
            answer_checked[i] = True

    # Second pass: count bulls
    for i in range(4):
        if not guess_checked[i]:
            for j in range(4):
                if not answer_checked[j] and guess[i] == answer[j]:
                    bull += 1
                    answer_checked[j] = True
                    break

    return cow, bull


def main():
    guess_log, answer = initiation()
    while guess_log[-1] != answer:
        guess_log = get_guess(guess_log)
        cow, bull = compare(guess_log[-1], answer)
        print('{} cows, {} bulls'.format(cow, bull))
    print('Correct! After {} guess(es) you finally got it!\nYour logs:'.format(len(guess_log) - 1),
          guess_log[1:])


if __name__ == "__main__":
    main()