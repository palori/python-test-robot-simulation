# Robot Application
# -----------------
# Author: Pau López Ribas (paulopezribas@gmail.com)
# Date: 2022/08/24
# Description: Example to play arround with the robot inputing
# commands from the terminal.

import robot as r
import table as t

if __name__ == "__main__":
    table = t.Table(5,5)
    robot = r.Robot(table, isPrint=True)
    robot.run()