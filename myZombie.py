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
            # Count shotguns and brains from the rolls
            shotguns = diceRollResults['shotgun']
            brains = diceRollResults['brains']
            

            # Reroll until he has more shotguns than brains 
            if shotguns < brains:
                diceRollResults = zombiedice.roll() # roll again
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
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
