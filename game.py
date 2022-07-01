import time 
import random



class Player():

    def __init__(self):
        self.score = 0
        self.options = { 0:'r', 1:'p', 2:'s'}
    
    def shoot(self):
        return self.options[random.randrange(3)]



def who_won(player_choice, tod_choice):
    '''determins and returns win, loss, or tie'''
    #tie
    if player_choice == tod_choice:
        return 'tie'

        #rock
    if player_choice == 'r':
        if tod_choice == 's':
            return 'won'
        if tod_choice == 'p':
            return 'loss'

        #paper
    if player_choice == 'p':
        if tod_choice == 's':
            return 'loss'
        if tod_choice == 'r:':
            return 'won'

        #sissors
    if player_choice == 's':
        if tod_choice == 'r':
            return 'loss'
        if tod_choice == 'p:':
            return 'won'


#initialize variables we will be using
tod = Player()
player = Player()
continue_question = lambda inpit:  inpit == 'q'
scoreboard = lambda score1, score2: f'Tod the Computer: {score1} | You: {score2}'
running = True
results = lambda you, tod: f"Your shoot: {you} Tod's shoot: {tod}"


print('Lets play a game of rock paper sisors!')
print('we will play best of three. \nType "start" if you are ready to start a new game\nType "quit" when you want to leave')

while running == True:
    re = input().lower()
    if re == 'start':
        tod = Player()
        player = Player()
        game = True
        while game == True:
            print('\nAfter seeing the word shoot, \n you will have one second to respond with the letters \n"r" for rock, "p" for paper, or "s" for sisors.\n \n ')
            time.sleep(3)
            print('\nfailure to respond within one second, with a priviously specified character\nwill result in you forfeiting the round.\n \n')
            time.sleep(3)
            print('Here we go!')
            time.sleep(0.5)
            print('Rock... ')
            time.sleep(0.5)
            print('Paper...')
            time.sleep(0.3)
            print('sisors...')
            time.sleep(0.25)
            print('shoot!')
            
            start = time.time()
            choice = input('you chose:')
            end = time.time()
            time_took = end - start
            print('\n \n \n')

            if choice == 'r' or choice == 's' or choice == 'p' : 
                tods_shoot = tod.shoot()
                win = who_won(choice, tods_shoot)

                if win == 'won':
                    player.score += 1
                    print("You won this round\n \n ")
                    print(scoreboard(tod.score, player.score))
                    print(results(choice, tods_shoot))
                    if player.score == 2:
                        print('you won!!')  
                        print('final score:')
                        print(scoreboard(tod.score, player.score))
                        game = False
                        
                    if continue_question(input('enter q to quit or anything else to continue')):
                        game = False

                if win == 'loss':
                    tod.score += 1
                    print('you lost this round\n \n')
                    print(results(choice, tods_shoot))
                    print(scoreboard(tod.score, player.score))
                    if tod.score == 2:
                        print('\n \nyou lost :(')  
                        print('final score:')
                        print(scoreboard(tod.score, player.score))  
                        game = False
                    if continue_question(input('enter q to quit or anything else to continue')):
                        game = False

                if win == 'tie':
                    print('Tie! no ponts awarded')
                    print(results(choice, tods_shoot))
                    print(scoreboard(tod.score, player.score))
                    if continue_question(input('enter q to quit or anything else to continue')):
                        game = False

            if (end - start) > 1 or choice != 'r' and choice != 'p' and choice != 's':
                print('You forfieted this match \n \n')
                print(f'you took {float(time_took)} seconds')
                tod.score += 1
                print(scoreboard(tod.score, player.score))
                print(results(choice, tods_shoot))
                if tod.score == 2:
                        print('\n \nyou lost :(')  
                        print('final score:')
                        print(scoreboard(tod.score, player.score))  
                        game = False
                if continue_question(input('enter q to quit or anything else to continue')):
                    game = False
            

    if re == 'quit':
        running = False
    if re != 'quit' and re != 'start':
        print('Type "start" if you are ready to start a game\nType "quit" when you want to leave')

print('\n \nThanks for playing!')
