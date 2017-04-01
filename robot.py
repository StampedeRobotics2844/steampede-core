'''
Steampede 2017
Betty H. Fairfax
Team 2844 @2017

'''
import wpilib
from networktables import NetworkTables


class SteampedeRobot(wpilib.IterativeRobot):
    '''robot code for steampede'''

    def robotInit(self):
        '''Robot initilization function'''
        '''initialize networktables'''
        self.sd = NetworkTables.getTable("SmartDashboard")

        self.shooter_speed = 1.0
        self.sd.putNumber('shooter_speed', self.shooter_speed)

        '''initialize the camera'''
        wpilib.CameraServer.launch()

        '''object that handles basic drive operatives'''
        self.drive_rf_motor = wpilib.Victor(6)
        self.drive_rr_motor = wpilib.Victor(7)
        self.drive_lf_motor = wpilib.Victor(8)
        self.drive_lr_motor = wpilib.Victor(9)
        self.shooter_motor = wpilib.Victor(0)
        self.gear_arm_motor = wpilib.Spark(1)
        self.loader_motor= wpilib.Spark(2)

        self.myRobot = wpilib.RobotDrive(self.drive_lf_motor, self.drive_lr_motor, self.drive_rf_motor, self.drive_rr_motor)
        self.myRobot.setExpiration(0.1)

        '''joysticks 1 & 2 on the driver station'''
        self.leftStick = wpilib.Joystick(0)
        self.rightStick = wpilib.Joystick(1)

        self.shooter_enabled = False

    def teleopInit(self):
        '''Executed at the start of teleop mode'''
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        '''Runs the motor with tank steering'''
        self.myRobot.tankDrive(self.leftStick, self.rightStick, True)

        if self.leftStick.getTrigger():
            self.shooter_enabled = True
            self.shooter_motor.set(self.leftStick.getAxis(wpilib.Joystick.AxisType.kZ))
        else:
            self.shooter_enabled = False
            self.shooter_motor.set(0)

if __name__ == '__main__':
    wpilib.run(SteampedeRobot)
