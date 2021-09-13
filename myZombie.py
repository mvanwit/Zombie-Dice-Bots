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

        # Stop at 2 brains Zombie code:
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

        # Random Zombie code:

        while diceRollResults is not None:
            # Random decision
            decision = random.randint(0, 1)

            # Reroll until he has at least 2 brains then stops
            if decision == 1:
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

        # Stop at 2 shotguns Zombie code:
        shotguns = 0
        while diceRollResults is not None:
            # Count shotguns from the rolls
            shotguns += diceRollResults['shotgun']

            # Reroll until he has at least 2 brains then stops
            if shotguns < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break                

zombies = (
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    TwoBrainsZombie(name='Stop at 2 brains'),
    RandomZombie(name='Random Zombie'),
    TwoShotgunsZombie(name='Stop at 2 shotguns')
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
