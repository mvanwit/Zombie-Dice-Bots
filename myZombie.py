import zombiedice, random
###
#Stop at 2 brains Zombie
###
class TwoBrainsZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        #Zombie code:
        brains = 0
        while diceRollResults is not None:
            #DEBUGprint("TwoBrainsZombie Turn")
            #DEBUGinput("Please press the Enter key to proceed") #DEBUG
            # Count brains from the rolls
            brains += diceRollResults['brains']

            # Reroll until he has at least 2 brains then stops
            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
###
#Stop at 2 shotguns
###
class TwoShotgunsZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        #Zombie code:
        shotguns = 0
        while diceRollResults is not None:
            #DEBUGprint("TwoShotgunsZombie Turn")
            #DEBUGinput("Please press the Enter key to proceed") #DEBUG
            # Count shotguns from the rolls
            shotguns += diceRollResults['shotgun']

            # Reroll until he has 2 shotguns then stops
            if shotguns < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break                  

###
#Randomly decide if it will continue or stop
###            
class RandomZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        #Zombie code:

        while diceRollResults is not None:
            #DEBUGprint("RandomZombie Turn")
            #DEBUGinput("Please press the Enter key to proceed") #DEBUG
            # Random decision
            decision = random.randint(0, 1)

            # Reroll if randomly decided
            if decision == 1:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
              

###
#A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
###
class OnetoFourZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        #Zombie code:
        decision = random.randint(1, 4)
        turn = 1
        shotguns = 0

        while diceRollResults is not None:
            #DEBUGprint("OnetoFourZombie Turn")
            #DEBUGinput("Please press the Enter key to proceed") #DEBUG
            # Count shotguns from the rolls
            shotguns += diceRollResults['shotgun']
            

            # Reroll until he has 2 shotguns or the number of turns decided is up 
            if shotguns < 2 and turn < decision:
                diceRollResults = zombiedice.roll() # roll again
                turn += 1
            else:
                break         

###
#A bot that stops rolling after it has rolled more shotguns than brains
###
class MoreShotgunsThanBrains:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        #Zombie code:        

        while diceRollResults is not None:
            #DEBUGprint("MoreShotgunsThanBrainsZombie Turn")
            #DEBUGinput("Please press the Enter key to proceed") #DEBUG
            # Count shotguns and brains from the rolls
            shotguns = diceRollResults['shotgun']
            brains = diceRollResults['brains']
            

            # Reroll until he has more shotguns than brains 
            if shotguns < brains:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break                        
###
#My own zombie
###
class ProZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.
        self.gameState = gameState
        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        #Zombie code:
        shotguns = 0
        brains = 0
        footsteps = {'green': 0, 'yellow': 0, 'red': 0}
        numFootsteps = 0
        cup = {'green': 6, 'yellow': 4, 'red': 3}
        diceFromCup = 0
        

        while diceRollResults is not None:
            #DEBUGprint("ProZombie Turn")
            #DEBUGprint(gameState['ORDER'])
            #DEBUGprint(gameState['SCORES'])
            
            #DEBUGinput("Please press the Enter key to proceed") #DEBUG
            numCup = 0
            # Count shotguns, brains, footsteps from the roll and dice lefts in the cup
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            for color in cup.keys():
                footsteps[color] = diceRollResults['rolls'].count((color, 'footsteps')) #count footsteps per color in current roll
                numFootsteps += footsteps[color]
                for i in range(len(diceRollResults['rolls'])):
                    cup[color] -= diceRollResults['rolls'][i][0].count(color) #count dice left in the cup per color
                numCup += cup[color]
                
            diceFromCup = 3 - numFootsteps # Count number of dice that we will need to pick in the cup if we continue
                
            #DEBUGprint(diceRollResults,'SG', shotguns,'B', brains,'FS', footsteps,'numFS', numFootsteps,'cup', cup,'numCup', numCup,'diceFromCup', diceFromCup, sep="\n") #DEBUG
            #DEBUGinput("Please press the Enter key to proceed") #DEBUG

            
            # Reroll when 0 shotgun
            if shotguns == 0:
                diceRollResults = zombiedice.roll() # roll again
            
            # Rules when 1 shotgun
            elif shotguns == 1:
                if  footsteps['green'] >= 2: #if 2 or 3 green footsteps
                    diceRollResults = zombiedice.roll() # roll again
                elif cup['yellow'] == 0 and cup['red'] == 0 and cup['green'] >= diceFromCup: #if only green dice left in the cup and enough for next roll
                    diceRollResults = zombiedice.roll() # roll again
                elif ( footsteps['red'] == 3 or ( cup['yellow'] == 0 and cup['green'] == 0 and cup['red'] >= diceFromCup ) ) and  brains < 1 : #If we must roll 3 red dice, stop at 1 brain.
                    diceRollResults = zombiedice.roll() # roll again
                elif ( ( footsteps['red'] == 2 and footsteps['yellow'] == 1 ) or cup['yellow'] > cup['green'] ) and brains < 2 : #If (rf = 2 and yf = 1) or yc > gc, stop at 2 brains
                    diceRollResults = zombiedice.roll() # roll again
                elif ( ( footsteps['red'] == 2 and footsteps['green'] == 1 ) or cup['green'] > cup['yellow'] ) and brains < 3 : #If (rf = 2 and gf = 1) or gc > yc, stop at 3 brains.
                    diceRollResults = zombiedice.roll() # roll again
                else:
                    break
                
            # Rules when 2 shotguns
            elif shotguns == 2:
                if footsteps['green'] == 3 and brains < 2:
                    diceRollResults = zombiedice.roll() # roll again
                elif brains < 1:
                    diceRollResults = zombiedice.roll() # roll again
                else:
                    break
            else:
                break



zombies = (
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    TwoBrainsZombie(name='Stop at 2 brains'),
    RandomZombie(name='Random Zombie'),
    TwoShotgunsZombie(name='Stop at 2 shotguns'),
    OnetoFourZombie(name='Stop after 1 to 4 turn or 2 shotguns'),
    MoreShotgunsThanBrains(name='Stop when more shotguns than brains'),
    ProZombie(name='My pro zombie')
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
