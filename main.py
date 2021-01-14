import random, math

all_options = {'rock': 0, 'fire': 1, 'scissors': 2, 'snake': 3, 'human': 4, 'tree': 5, 'wolf': 6,
               'sponge': 7, 'paper': 8, 'air': 9, 'water': 10, 'dragon': 11, 'devil': 12,
               'lightning': 13, 'gun': 14}

user_name = input('Enter your name: ')
print(f'Hello, {user_name}')

choices = input('Enter options you want to play with or leave empty to use defaults: ').split(',')
defaults = ['rock', 'scissors', 'paper']

print("Okay, let's start")

ratings = [line.split() for line in open('rating.txt', 'r').readlines()]
ratings = {name: int(score) for name, score in ratings}

if user_name not in ratings:
    ratings.update({user_name: 0})

user_score = ratings[user_name] if user_name in ratings else 0


def match(user_choice: str, computer_choice: str, options_length: int):
    if user_choice == computer_choice:
        print(f'There is a draw ({computer_choice}).\n')
        return 50
    elif all_options[user_choice] + math.ceil(options_length / 2) > options_length:
        if all_options[user_choice] < all_options[computer_choice]:
            print(f'Well done. The computer chose {computer_choice} and failed.\n')
            return 100
        if all_options[user_choice] + math.ceil(options_length / 2) - options_length > all_options[computer_choice]:
            print(f'Well done. The computer chose {computer_choice} and failed.\n')
            return 100
        print(f'Sorry, but the computer chose {computer_choice}.\n')
        return 0
    elif all_options[user_choice] + math.ceil(options_length / 2) > all_options[computer_choice] > all_options[user_choice]:
        print(f'Well done. The computer chose {computer_choice} and failed.\n')
        return 100
    else:
        print(f'Sorry, but the computer chose {computer_choice}.\n')
        return 0


def get_score(username: str):
    with open('rating.txt', 'r') as rating_txt:
        for line in rating_txt.readlines():
            if username in line.split():
                return line.split()[1]
    return 0


def update_score(username: str, addition: int):
    ratings[username] += addition
    with open('rating.txt', 'w') as rating_txt:
        for user in ratings:
            print(f'{user} {ratings[user]}', file=rating_txt, flush=True)


while True:
    user_choice = input('Choose your option: ')
    computer_choice = random.choice(choices) if choices != [''] else random.choice(defaults)

    if user_choice == '!exit':
        print('Bye!')
        break
    elif user_choice == '!rating':
        print(f'Your rating: {get_score(user_name)}\n')
        continue
    elif user_choice not in all_options:
        print('Invalid input.\n')
        continue

    result = match(user_choice, computer_choice, len(all_options))
    update_score(user_name, result)
