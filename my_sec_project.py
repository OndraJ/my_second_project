from random import sample, randrange

LINE = '-' * 47
def presenter():
    print('','Hi there!',LINE,'I\'ve generated a random 4 digit number for you.',
          'Let\'s play a bulls and cows game.',
          'For exit a game press "q"',LINE,sep='\n')

def secret_num():
    numbers = [str(i) for i in range(1,10)]
    first_number = numbers.pop(randrange(len(numbers)))
    numbers.append('0')
    rest_numbers = sample(numbers, 3)
    secret_number = ''.join([first_number, *rest_numbers])
    return secret_number

def check_duplication(quess_number: str):
    checking_list = [i for i in quess_number]
    if len(checking_list) == len(set(checking_list)):
        return False
    else:
        return True

def guessing_number():
    while True:
        print('Enter the number: ',LINE, sep='\n')
        guess = input('>>> ')
        if guess == 'q':
            print('Terminating the program...', LINE, sep='\n')
            exit()
        elif len(guess) != 4:
            print('The number must be 4 digits long', LINE, sep='\n')
        elif guess[0] == '0':
            print('The number must not start with zero', LINE, sep='\n')
        elif not guess.isnumeric():
            print('Must be number')
        elif check_duplication(guess):
            print('The number must not contain duplicates', LINE, sep='\n')
        else:
            return guess

def evaluation(quess_num_in_str: str, sec_num_in_str: str):
    list_of_guess = [i for i in quess_num_in_str]
    list_of_number = [i for i in sec_num_in_str]
    bull = 0
    cow = 0
    for i_1, v_1 in enumerate(list_of_guess):
        for i_2, v_2 in enumerate(list_of_number):
            if v_1 == v_2 and i_1 == i_2:
                bull += 1
            elif v_1 == v_2 and i_1 != i_2:
                cow += 1
    return bull, cow

def bulls_cows(num1: int, num2: int):
    if num1 == 1 or num2 == 1:
        name_1 = 'Bull'
        name_2 = 'Cow'
    else:
        name_1 = 'Bulls'
        name_2 = 'Cows'
    print(f'{num1} {name_1}, {num2} {name_2}', LINE, sep='\n')

def game():
    sec_num = secret_num() 
    counter = 0
    while True:
        counter += 1
        guess_num = guessing_number()
        bull, cow = evaluation(guess_num,sec_num)
        bulls_cows(bull,cow)
        if bull == 4:
            print('Correct, you\'ve guessed the right number',
            f'in {counter} guesses','',sep='\n')
            break
        
def main():
    presenter()
    game()

if __name__ == '__main__':
    main()
    

