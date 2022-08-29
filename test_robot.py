# Testing
# -------
# Author: Pau López Ribas (paulopezribas@gmail.com)
# Date: 2022/08/24
# Description: Main tests to assess the operability of the system.


import unittest
import robot as r
import table as t

class TestTable(unittest.TestCase):
    def test_getX(self):
        table = t.Table(5,5)
        self.assertEqual(table.getX(), 5)

    def test_getY(self):
        table = t.Table(5,25)
        self.assertEqual(table.getY(), 25)

class TestRobotUnit(unittest.TestCase):

    # All tests use REPORT to evaluate them

    # Testing PLACE command
    def test_place_correct(self):
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.place(3,4,'WEST')
        robot_position = robot.report()
        self.assertEqual(robot_position, '3,4,WEST')

    def test_place_incorrect_number(self):
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.place(3,6,'WEST')
        robot_position = robot.report()
        self.assertEqual(robot_position, 'not in place')

    def test_place_incorrect_face(self):
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.place(3,6,'WE')
        robot_position = robot.report()
        self.assertEqual(robot_position, 'not in place')

    def test_place_incorrect_text(self):
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.place(3,'my','WEST')
        robot_position = robot.report()
        self.assertEqual(robot_position, 'not in place')

    # Testing MOVE command
    def test_move_x(self):
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.place(0,0,'EAST')
        robot.move()
        robot.move()
        robot_position = robot.report()
        self.assertEqual(robot_position, '2,0,EAST')
        
    def test_move_y(self):
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.place(0,0,'NORTH')
        robot.move()
        robot.move()
        robot_position = robot.report()
        self.assertEqual(robot_position, '0,2,NORTH')

    def test_move_border(self):
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.place(0,0,'SOUTH')
        robot.move()
        robot.move()
        robot_position = robot.report()
        self.assertEqual(robot_position, '0,0,SOUTH')

    # Testing RIGHT command
    def test_right(self):
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.place(1,1,'NORTH')
        
        robot.right()
        robot_position = robot.report()
        self.assertEqual(robot_position, '1,1,EAST')

        robot.right()
        robot_position = robot.report()
        self.assertEqual(robot_position, '1,1,SOUTH')

        robot.right()
        robot_position = robot.report()
        self.assertEqual(robot_position, '1,1,WEST')

        robot.right()
        robot_position = robot.report()
        self.assertEqual(robot_position, '1,1,NORTH')
    
    # Testing LEFT command
    def test_left(self):
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.place(1,1,'NORTH')
        
        robot.left()
        robot_position = robot.report()
        self.assertEqual(robot_position, '1,1,WEST')

        robot.left()
        robot_position = robot.report()
        self.assertEqual(robot_position, '1,1,SOUTH')

        robot.left()
        robot_position = robot.report()
        self.assertEqual(robot_position, '1,1,EAST')

        robot.left()
        robot_position = robot.report()
        self.assertEqual(robot_position, '1,1,NORTH')



class TestRobotIntegration(unittest.TestCase):

    def test_1(self):
        """
        TEST 1: ignores commands before robot is put into place
        """
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.do('MOVE')
        robot.do('LEFT')
        robot.do('RIGHT')
        robot_position = robot.do('REPORT')
        self.assertEqual(robot_position, 'not in place')

    def test_2(self):
        """
        TEST 2: place robot on a given position
        """
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.do('PLACE 1,2,NORTH')
        robot_position = robot.do('REPORT')
        self.assertEqual(robot_position, '1,2,NORTH')

    def test_3(self):
        """
        TEST 3: robot is not placed in an invalid position
        """
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.do('PLACE 9,9,NORTH')
        robot_position = robot.do('REPORT')
        self.assertEqual(robot_position, 'not in place')

    def test_4(self):
        """
        TEST 4: robot rotates right
        """
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.do('PLACE 1,1,NORTH')
        
        robot.do('RIGHT')
        robot_position = robot.do('REPORT')
        self.assertEqual(robot_position, '1,1,EAST')

        robot.do('RIGHT')
        robot_position = robot.do('REPORT')
        self.assertEqual(robot_position, '1,1,SOUTH')

        robot.do('RIGHT')
        robot_position = robot.do('REPORT')
        self.assertEqual(robot_position, '1,1,WEST')

        robot.do('RIGHT')
        robot_position = robot.do('REPORT')
        self.assertEqual(robot_position, '1,1,NORTH')

    def test_5(self):
        """
        TEST 5: robot rotates left
        """
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.do('PLACE 1,1,NORTH')
        
        robot.do('LEFT')
        robot_position = robot.do('REPORT')
        self.assertEqual(robot_position, '1,1,WEST')
        
        robot.do('LEFT')
        robot_position = robot.do('REPORT')
        self.assertEqual(robot_position, '1,1,SOUTH')
        
        robot.do('LEFT')
        robot_position = robot.do('REPORT')
        self.assertEqual(robot_position, '1,1,EAST')
        
        robot.do('LEFT')
        robot_position = robot.do('REPORT')
        self.assertEqual(robot_position, '1,1,NORTH')

    def test_6(self):
        """
        TEST 6: robot is able to move in all four cardinal directions
        """
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.do('PLACE 1,1,NORTH')
        
        robot.do('MOVE')
        robot.do('RIGHT')
        robot_position = robot.do('REPORT')
        self.assertEqual(robot_position, '1,2,EAST')
        
        robot.do('MOVE')
        robot.do('RIGHT')
        robot_position = robot.do('REPORT')
        self.assertEqual(robot_position, '2,2,SOUTH')
        
        robot.do('MOVE')
        robot.do('RIGHT')
        robot_position = robot.do('REPORT')
        self.assertEqual(robot_position, '2,1,WEST')
        
        robot.do('MOVE')
        robot.do('RIGHT')
        robot_position = robot.do('REPORT')
        self.assertEqual(robot_position, '1,1,NORTH')

    def test_7(self):
        """
        TEST 7: robot won't fall off the table
        """
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.do('PLACE 4,4,NORTH')
        robot.do('MOVE')
        robot.do('MOVE')
        robot.do('MOVE')
        robot.do('MOVE')
        robot.do('MOVE')
        robot_position = robot.do('REPORT')
        self.assertEqual(robot_position, '4,4,NORTH')

    def test_8(self):
        """
        TEST 8: robot will ignore invalid commands
        """
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.do('AUTODESTRUCT')
        robot.do('TAKEOFF')
        robot.do('KILL')
        robot_position = robot.do('REPORT')
        self.assertEqual(robot_position, 'not in place')

    def test_9(self):
        """
        TEST 9: The commands are not case sensitive
        """
        table = t.Table(5,5)
        robot = r.Robot(table)
        robot.do('PLACE 3,0,NORTH')
        robot.do('move')
        robot.do('Left')
        robot.do('Move')
        robot.do('Right')
        robot.do('MOVE')
        robot_position = robot.do('REpoRT')
        self.assertEqual(robot_position, '2,2,NORTH')


if __name__ == '__main__':
    unittest.main()