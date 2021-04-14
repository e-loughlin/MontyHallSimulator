


import random

def randomizePrizeLocation():
    random_num = random.uniform(0,1)
    if random_num < 0.3333333333:
        prize_index = 0
    elif random_num < 0.66666666:
        prize_index = 1
    else:
        prize_index = 2

    doors = [1,1,1]
    doors[prize_index] = 2

    return doors

wins = 0
losses = 0
games_played = 0

class DoorState(enum):
    CLOSED_NO_PRIZE = 1
    CLOSED_WITH_PRIZE = 2
    OPEN_NO_PRIZE = 3
    OPEN_WITH_PRIZE = 4

def printRollingStats():
    print("=========")
    print("Wins: {}".format(wins))
    print("Losses: {}".format(losses))
    print("Games Played: {}".format(games_played))
    print("Win Percentage: {}".format(float(wins)/games_played))
    print("=========")

def printDoors(doorStates):
    print(" 1   2   3 ")
    for doorState in doorStates:
        if doorState == DoorState.CLOSED_NO_PRIZE or doorState == DoorState.CLOSED_WITH_PRIZE:
            print("[?] ", end='')
        elif doorState == DoorState.OPEN_NO_PRIZE:
            print("[ ] ", end='')
        elif doorState == DoorState.OPEN_WITH_PRIZE:
            print("[$] ", end='')
    print()


def main()
    print("Monty Hall Simulator!")
    keep_playing = True

    while(keep_playing):
        switch = False

        doors = randomizePrizeLocation()

        selection_made = False
        while not selection_made:
            print("Select door 1, 2, or 3!")
            printDoors(doors)
            selection = int(input())
            if selection == 1 or selection == 2 or selection == 3:
                selection_made = True
            else:
                print("Invalid selection.")

        print("OK! You've made selection {}. But wait! I'll open a different door...".format(selection))
        for i, doorState in enumerate(doors):
            if doorState == DoorState.CLOSED_NO_PRIZE:
                doors[i] = DoorState.OPEN_NO_PRIZE

        printDoors(doors)
        print("Would you like to switch doors? (y/n)")
        switch_doors = False
        switch_doors_response = input()
        if switch_doors_response == "y":
            switch_doors = True       
        if switch_doors_response == "n":
            switch_doors = False

        if switch_doors:
            for i, doorState in enumerate(doors):
                if i + 1 == selection:
                    continue
                elif doorState == DoorState.OPEN_NO_PRIZE:
                    continue
                else:
                    selection = i + 1
                    break

        games_played += 1

        print("Ok! Open door {}!".format(selection))

        # LOSE
        if doors[selection-1] == DoorState.CLOSED_NO_PRIZE:
            doors[selection-1] = DoorState.OPEN_NO_PRIZE
            losses += 1
            printDoors(doors)
            print("I'm sorry, you LOSE!")

        # WINv
        elif doors[selection-1] == DoorState.CLOSED_WITH_PRIZE
            doors[selection-1] = DoorState.OPEN_WITH_PRIZE
            win = True
            wins += 1
            printDoors(doors)
            print("You WIN!")

        printRollingStats()

        print("Keep playing? (y/n)")
        keep_playing_response = input()
        
        if keep_playing_response == "y":
            keep_playing = True       
        if keep_playing_response == "n":
            keep_playing = False

        
            



if __name__ == "__main__":
    main()