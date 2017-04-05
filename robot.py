'''
Steampede 2017
Betty H. Fairfax
Team 2844 @2017

'''
import wpilib
import logging
import robotmap
from networktables import NetworkTables
from robotpy_ext.autonomous import AutonomousModeSelector

logging.basicConfig(level=logging.DEBUG)

class SteampedeRobot(wpilib.IterativeRobot):
    ''' robot code for steampede '''

    def __init__(self):
        super().__init__()

        self.smart_dashboard = None
        self.shooter_speed = 1.0

        self.gear_arm_opening_speed = -1.0
        self.gear_arm_closing_speed = 1.0

        self.loader_speed = 1.0

        self.shooter_enabled = False
        self.loader_enabled = False
        
        self.gear_arm_opened = False
        self.gear_arm_closed = True
        self.gear_arm_opening = False
        self.gear_arm_closing = False

        self.drive_rf_motor = None
        self.drive_rr_motor = None
        self.drive_lf_motor = None
        self.drive_lr_motor = None

        self.shooter_motor = None
        self.gear_arm_motor = None
        self.loader_motor = None

        self.left_stick = None

        self.right_stick = None
        self.drive = None

    def robotInit(self):
        ''' Robot initilization function '''

        # initialize networktables
        self.smart_dashboard = NetworkTables.getTable("SmartDashboard")
        self.smart_dashboard.putNumber('shooter_speed', self.shooter_speed)
        self.smart_dashboard.putNumber('gear_arm_opening_speed', self.gear_arm_opening_speed)
        self.smart_dashboard.putNumber('gear_arm_closing_speed', self.gear_arm_closing_speed)
        self.smart_dashboard.putNumber('loader_speed', self.loader_speed)

        # initialize and launch the camera
        wpilib.CameraServer.launch()

        # object that handles basic drive operatives
        self.drive_rf_motor = wpilib.Victor(robotmap.motors.right_front)
        self.drive_rr_motor = wpilib.Victor(robotmap.motors.right_rear)
        self.drive_lf_motor = wpilib.Victor(robotmap.motors.left_front)
        self.drive_lr_motor = wpilib.Victor(robotmap.motors.left_rear)
        self.shooter_motor = wpilib.Victor(robotmap.motors.shooter)
        self.gear_arm_motor = wpilib.Spark(robotmap.motors.gear_arm)
        self.loader_motor = wpilib.Spark(robotmap.motors.loader)

        # initialize drive
        self.drive = wpilib.RobotDrive(self.drive_lf_motor, self.drive_lr_motor,
                                       self.drive_rf_motor, self.drive_rr_motor)

        self.drive.setExpiration(0.1)

        # joysticks 1 & 2 on the driver station
        self.left_stick = wpilib.Joystick(0)
        self.right_stick = wpilib.Joystick(1)

        # initialize gyro
        self.gyro = wpilib.AnalogGyro(1)

        # initialize autonomous components
        self.components = {
            'drive': self.drive
        }

        self.automodes = AutonomousModeSelector('autonomous', self.components)
        
    def teleopInit(self):
        '''Executed at the start of teleop mode'''
        self.drive.setSafetyEnabled(True)

    def teleopPeriodic(self):        
        '''Runs the motor with tank steering'''
        self.drive.tankDrive(self.left_stick, self.right_stick, True)

        if self.left_stick.getTrigger():
            self.shooter_enabled = True
            axis = self.left_stick.getAxis(wpilib.Joystick.AxisType.kZ)
            if axis != self.shooter_speed:
                self.shooter_speed = axis
                self.smart_dashboard.putNumber('shooter_speed', self.shooter_speed)
            self.shooter_motor.set(self.shooter_speed)
        else:
            self.shooter_enabled = False
            self.shooter_motor.set(0)

        if self.right_stick.getTrigger():
            self.loader_enabled = True
            axis = self.right_stick.getAxis(wpilib.Joystick.AxisType.kZ)
            if axis != self.loader_speed:
                self.loader_speed = axis
                self.smart_dashboard.putNumber('loader_speed', self.loader_speed)
            self.loader_motor.set(self.loader_speed)
        else:
            self.loader_enabled = False
            self.loader_motor.set(0)
                    
        if self.right_stick.getRawButton(2) or self.left_stick.getRawButton(2):    
            self.gear_arm_closing = True        
            self.gear_arm_motor.set(self.gear_arm_closing_speed)
        else:
            self.gear_arm_motor.set(0)
            self.gear_arm_closing = False
        
        if self.right_stick.getRawButton(3) or self.left_stick.getRawButton(3):
            self.gear_arm_opening = True
            self.gear_arm_motor.set(self.gear_arm_opening_speed)
        else:
            self.gear_arm_motor.set(0)
            self.gear_arm_opening = False

    def autonomousInit(self):
        self.drive.setSafetyEnabled(True)
    
    def autonomousPeriodic(self):
        self.automodes.run()


if __name__ == '__main__':
    wpilib.run(SteampedeRobot)
