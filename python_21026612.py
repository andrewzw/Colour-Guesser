import random
def instruction_1():
    #outputs insturction
    print('------------------------------------------[Instructions]------------------------------------------')
    print('|1) Choose how many input do you want to have                                                    |')
    print('|Example: How many inputs can you guess?[1-6]:3,                                                 |')
    print('|A hidden color arrangement will be generated                                                    |')
    print('|You will then get 3 empty brackes which you would have to key in your guesses                   |')
    print('|                    These boxes contains the hidden color arrangement:                          |')
    print('|                              \/ \/ \/ Fill in the blanks \/ \/ \/                              |')
    print('|                                      [__1__][__2__][__3__]                                     |')
    print('|                                                                                                |')
    print('|2)Then you will have the guess the arrange of colors from:                                      |')
    print('|                            [Red, Blue, Yellow, Green, Pink, Purple]                            |')
    print('|                                                                                                |')
    print('|Example: Please input a color: Yellow                                                           |')
    print('|Example: Please input a color: Blue                                                             |')
    print('|Example: Please input a color: Green                                                            |')
    print('|Example: Your Final Answer Is: [yellow, blue, green]                                            |')
    print('|Example: "yellow" Correct colour but in the wrong place                                         |')
    print('|Example: "green" is not in the arrangement -this means green is not in the answer list          |')
    print('|Example: "blue" is in correct position                                                          |')
    print('|                                                                                                |')
    print('|3)Then you will have to guess until you get the arrangement and the colors correct              |')
    print('|                                                                                                |')
    print('|-----------------------------------------------END----------------------------------------------|')
    print('')
def start_game():
    #Starts the game
    colourlist = ['red', 'red', 'red', 'red', 'red', 'red',
                  'blue', 'blue', 'blue', 'blue', 'blue', 'blue',
                  'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow',
                  'green', 'green', 'green', 'green', 'green', 'green',
                  'pink', 'pink', 'pink', 'pink', 'pink', 'pink',
                  'purple', 'purple', 'purple', 'purple', 'purple', 'purple']

    correct_Y_N = False

    while correct_Y_N == False:
        start = input('Do you want to play?[Y/N]:').lower()
        print('')
        # When input is N/No
        if start == 'n' or start == 'no':
            print("See You Again!")
            break

        # When input is Y/Yes
        elif start == 'y' or start == 'yes':
            correct_Y_N = True
            correct = False
            guess = 1
            play_again = True

            # Ask for number until correct input is entered
            while correct == False:
                number = input('How many inputs can you guess?[1-6]:')
                print('The colors in the random generated list can be repeated')
                print('')
                # Not a number
                if (number.isdigit() is False):
                    print('')
                    print('Input entered is not a number, Please Try Again!')
                    print('')

                # Number not in range
                elif (int(number) < 1) or (int(number) > 6):
                    print('Number must be in range [1-6], Please Try Again!')
                    print('')

                # Number in range
                else:
                    while play_again == True:
                        correct = True
                        number = int(number)
                        print('')
                        print('Choose from [red, blue, yellow, green, pink, purple]')
                        print('\/ \/ \/ Fill in the blanks \/ \/ \/')

                        for count in range(number):
                            print('[__' + str(count + 1) + '__]', end='')

                        # Generate random list
                        if guess == 1:
                            random_colourlist = random.choices(colourlist, k=number)
                        #print(random_colourlist)-check answer

                        print('')
                        user_input_list = []
                        for a in range(number):
                            correct_colour = False

                            # Check for colour input correctness:
                            while correct_colour == False:
                                print('')
                                user_input = input('Please input a colour:').lower()

                                if user_input in colourlist:
                                    user_input_list.append(user_input)
                                    print(user_input_list)
                                    correct_colour = True

                                else:
                                    print('')
                                    print(
                                        'Incorrect Colour, Please Try Again from [red, blue, yellow, green, pink, purple]!')

                        random_copy = random_colourlist.copy()
                        # Check if it matches the random generated list
                        print('')
                        for i in range(len(user_input_list)):

                            # Wrong Position
                            if (user_input_list[i] in random_copy) and (user_input_list[i] != random_copy[i]):
                                for a in range(len(random_copy)):
                                    if user_input_list[i] == random_copy[a]:
                                        print(f'"{user_input_list[i]}" Correct colour but in the wrong place')
                                        break
                            # Not in list
                            elif (user_input_list[i] not in random_copy):
                                print(f'"{user_input_list[i]}" is not in the arrangement')

                            # Correct Position
                            else:
                                print(f'"{user_input_list[i]}" is in correct position')

                        #Shows user their input
                        if user_input_list == random_colourlist:
                            print('')
                            print('Your Answer Is      :', user_input_list)
                            print('The Actual Answer Is:', random_colourlist)
                            print('')
                            print('You\'re Correct!')
                            print(f'You took {guess} guesses!')

                        print('')
                        #Ask if user wants to play again
                        play_again_correct_Y_N = False
                        while play_again_correct_Y_N == False:
                            play_again_promp = input('Play Again?[Y/N]:').lower()
                            if play_again_promp == 'n' or play_again_promp == 'no':
                                play_again = False
                                play_again_correct_Y_N = True
                                print('Thanks for playing! See you again!')
                                print('')

                            # User completed the game and still wants to play
                            elif (play_again_promp == 'y' or play_again_promp == 'yes') and (
                                    user_input_list == random_colourlist):
                                play_again_correct_Y_N = True
                                play_again = False
                                start_game()

                            #Ask if they would like to continue even if answer is wrong
                            elif (play_again_promp == 'y' or play_again_promp == 'yes') and (
                                    user_input_list != random_colourlist):
                                play_again_correct_Y_N = True
                                guess += 1

                            #Check if user keyed in the correct input
                            else:
                                print('')
                                print('Please enter Y or N')


        # When input is not N/No or Y/Yes
        else:
            print('Please input Y or N')
            print('')
def menu_prompt():
    #Outputs menu
    print('-----------------------[MENU]--------------------------')
    print('|                 1) How To Play                      |')
    print('|                 2) Start Game                       |')
    print('|                 3) Exit                             |')
    print('-------------------------------------------------------')

print('-------------------------------------------------------')
print('|               Welcome To Master Mind!               |')
print('|                                                     |')
print('|              Created by: Yap Zhe Wei                |')
print('|              Student ID: 21026612                   |')
print('-------------------------------------------------------')
menu_prompt()  #Outputs menu

# Map user input to a function
x = 1
while x == 1:
    menu = int(input('Choose from [1], [2] or [3]:'))
    if int(menu) == 1:
        print('')
        instruction_1()
        menu_prompt()
        x = 1

    elif int(menu) == 2:
        print('')
        start_game()
        menu_prompt()
        x = 1

    elif int(menu) == 3:
        print('See You Next Time!')
        x = 0

    else:
        print('Wrong Input')
        x = 1