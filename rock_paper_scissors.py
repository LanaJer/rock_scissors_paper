from random import randint



def find_winner(choice_a, choice_b):
    """
    возвращает True, если выиграл A, ...
    """
    if choice_a == choice_b:
        return None
    elif choice_a == 'r' and choice_b == 'p':
        return True
    elif choice_a == 'r' and choice_b == 's':
        return True
    elif choice_a == 's' and choice_b == 'r':
        return False
    elif choice_a == 's' and choice_b == 'p':
        return True
    elif choice_a == 'p' and choice_b == 'r':
        return True
    elif choice_a == 'p' and choice_b == 's':
        return False
    else:
        raise ValueError('It does not correct text.')


def find_winner_alternative(choice_a, choice_b, alphabet):
    index_a = alphabet.index(choice_a)
    index_b = alphabet.index(choice_b)
    if index_a == index_b:
        return None
    if index_a == 0 and index_b == len(alphabet):
        return False
    if index_b == 0 and index_a == len(alphabet):
        return True

    return index_a < index_b


def rock_scissors_paper_round(latter):
    """Игра камень-ножницы-бумага."""
    variant_list = ['r', 's', 'p']
    x = randint(0, 2)
    choice = variant_list[x]
    print('...' + latter + ' vs ' + choice)
    result = find_winner(latter, choice)
    return result


def get_result_text(result):
    """Получаем результат текстом."""
    if result is True:
        return 'You score!'
    elif result is False:
        return 'Computer scores!'
    elif result is None:
        return 'Draw!'


def rock_scissors_paper_game_three():
    """Игра камень-ножницы-бумага в три раунда."""
    computer_wins = 0
    human_wins = 0
    while True:
        msg = input('Please tell me a latter:')
        try:
            resalt = rock_scissors_paper_round(msg)
        except ValueError:
            print('Please try again.')
            continue
        if resalt is True:
            human_wins += 1
            print('You score! ' + str(human_wins) + ':' + str(computer_wins))
        elif resalt is False:
            computer_wins += 1
            print('Computer scores! ' + str(human_wins) + ':' + str(computer_wins))
        elif resalt is None:
            print('Draw!')
            continue
        if computer_wins == 3:
            print('You lose!')
            break
        if human_wins == 3:
            print('You win!')
            break


def get_user_score():
    """Запоминает счет пользователя."""
    context.user_data = {}
    round_score = 1
    context.user_data['user_score'] = context.user_data.get('user_score', 0) + round_score

if __name__ == '__main__':
    rock_scissors_paper_game_three()
