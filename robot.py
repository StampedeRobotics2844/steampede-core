'''
Steampede 2017
Betty H. Fairfax
Team 2844 @2017

'''
import wpilib


class SteampedeRobot(wpilib.IterativeRobot):
    '''robot code for steampede'''

    def robotInit(self):
        '''Robot initilization function'''

        # object that handles basic drive operatives
        self.myRobot = wpilib.RobotDrive(6, 7, 8, 9)
        self.myRobot.setExpiration(0.1)

        # joysticks 1 & 2 on the driver station
        self.leftStick = wpilib.Joystick(0)
        self.rightStick = wpilib.Joystick(1)

    def teleopInit(self):
        '''Executed at the start of teleop mode'''
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        '''Runs the motor with tank steering'''
        self.myRobot.tankDrive(self.leftStick, self.rightStick, True)

if __name__ == '__main__':
    wpilib.run(SteampedeRobot)
