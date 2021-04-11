def is_game_on():

    choice = 'wrong'

    while choice.lower() not in ['yes', 'no']:

        choice = input('Play again? (Yes/No): ')

        if choice.lower() not in ['yes', 'no']:
            print('I do not understand')

    return choice.lower() == 'yes'
