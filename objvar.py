# Filename: objvar.py
# A more complex example showing the properties of classes.

class Robot:
    '''Represents a robot, with a name.'''

    # A class variable, counting the number of robots.
    population = 0

    def __init__(self, name):
        '''initializes the data.'''
        self.name = name
        print('(Initializing {0})'.format(self.name))

        # Adding the count of robot population.
        Robot.population = Robot.population + 1

        
    def __del__(self):
        '''I am dying.'''
        print('{0} is being destroyed!'.format(self.name))

        Robot.population = Robot.population - 1

        if Robot.population == 0:
            print('{0} was the last of his kind.'.format(self.name))
        else:
            print('There are still {0:d} robots working'\
                  .format(Robot.population))

    def sayHi(self):
        '''Greeting by the robot.
    
        Yeah, they can do that.'''
        print('Greetings, my masters call me {0}.'.format(self.name))

    def howMany():
        '''Prints the current robot population.'''
        print('We have {0:d} robots.'.format(Robot.population))
    howMany = staticmethod(howMany)

bot1 = Robot('Bender')
bot1.sayHi()
Robot.howMany()

bot2 = Robot('Calculon')
bot2.sayHi()
Robot.howMany()

print('\nRobots can do some work in here.\n')

print('Robots have finished their work. We can destroy them.')

del bot1
del bot2

Robot.howMany()
