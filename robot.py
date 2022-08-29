# Robot Class
# -----------
# Author: Pau López Ribas (paulopezribas@gmail.com)
# Date: 2022/08/23
# Description: The robot receives text inputs and moves arroud a table.


import numpy as np
import math
from time import sleep
import table as t


class Robot:

    def __init__(self, table, isPrint=False):
        # Robot position and orientation
        self.x = None
        self.y = None
        self.f = None
        self.table = table
        self.isPrint = isPrint

    def place(self, x, y, f):
        f_index = np.where(self.table.getFaces() == f.upper())[0]

        try:
            # Prevent error when converting [x,y] to integer
            x = int(x)
            y = int(y)

            if ( (x >= 0 and x < self.table.getX()) and 
            (y >= 0 and y <= self.table.getY()) and 
            (len(f_index) > 0) ):
                self.x = x
                self.y = y
                self.f = f_index[0]
        except ValueError or TypeError:
            pass



    def move(self):
        # Move forward one step
        # Compute new carthesian coordinates based on polar coordinates where
        # the module is 1 and the argument (angle) is based on the orientation
        # (current 'face').
        # angle = 0 -> EAST, that is why it is the first item on the 'faces'
        # array.
        angle = 2*math.pi/len(self.table.getFaces()) * self.f
        x = self.x + round(math.cos(angle))
        y = self.y + round(math.sin(angle))

        # Set new coordinates within the table limits'
        new_coordinates = [x, y]
        table_max_limits = [self.table.getX(), self.table.getY()]
        for i in range(len(new_coordinates)):
            if new_coordinates[i] >= table_max_limits[i]:
                new_coordinates[i] = table_max_limits[i] - 1
            elif new_coordinates[i] < 0:
                new_coordinates[i] = 0

        # Assign updated position
        self.x = new_coordinates[0]
        self.y = new_coordinates[1]

    def left(self):
        # Turn left: increment the faces index counter and keep it between [0, #faces-1]
        self.f = (self.f + 1) % len(self.table.getFaces())

    def right(self):
        # Turn right: decrement the faces index counter and keep it between [0, #faces-1]
        self.f = (self.f - 1) % len(self.table.getFaces())

    def report(self):
        # Retur robot position (if any), i.e.: '1,2,WEST'
        if (self.isInPosition()):
            return f'{self.x},{self.y},{self.table.getFaces()[self.f]}'
        return 'not in place'
    
    def report_array(self):
        # Retur robot position (if any) as an array, i.e.: [1,2,3]
        if (self.isInPosition()):
            return [self.x,self.y,self.f]
        return []

    def isInPosition(self):
        # Evaluate if the robot has been set in a correct position
        return (self.x != None and self.y != None and self.f != None)

    def do(self, command):
        # Perform the command inputed by the user

        # Parse input as: '<action> [<new_position>]' where
        # 'new_position' = 'x,y,f' as type (int, int, str)
        args = command.split(' ')
        action = args[0].upper()

        if len(args) == 1:
            if action == 'REPORT':
                robot_position = self.report()
                if (self.isPrint):
                    print(robot_position)
                return robot_position

            elif self.isInPosition():
                if action == 'MOVE':
                    self.move()

                elif action == 'LEFT':
                    self.left()

                elif action == 'RIGHT':
                    self.right()


        elif len(args) == 2:
            if action == 'PLACE':
                # parse position
                new_position = args[1].split(',')
                if len(new_position) == 3:
                    self.place(int(new_position[0]), int(new_position[1]), \
                        new_position[2])

        # other commands will be ignored, no errors will show
        # return self.report_array()

    def run(self):
        # Start and run the robot
        # Displays command information to play arround
        if self.isPrint:
            line = '---'
            print(f'\n{line}\nWelcome!\nWe are turning on the robot for you. Please, wait...')
            sleep(1.5)

            help_message = f'\n{line}\n\
The application is a simulation of a toy robot moving on a square\
tabletop, of dimensions {self.table.getX()} units x {self.table.getY()}\
units.\n\n\
Type the following comands to place the robot, move and turn arround \
and get its position (it is not case sensitive):\n\
    PLACE X,Y,F (where F can be NORTH, SOUTH, EAST or WEST)\n\
    MOVE\n\
    LEFT\n\
    RIGHT\n\
    REPORT\n\n\
Anytime you can introduce the commands:\n\
    Q (to quit)\n\
    H (to display this help message again)\n\n\
Have fun!\
\n{line}\n'
            print(help_message)

        while(True):
            command = input()
            if (command == 'Q' or command == 'q') and self.isPrint:
                print(f'\n{line}\nTurning down the robot...')
                sleep(1.5)
                print(f'See you soon :)\n{line}\n')
                break
            elif (command == 'H' or command == 'h') and self.isPrint:
                print(help_message)
            else:
                self.do(command)


