'''
Steampede 2017
Betty H. Fairfax
Team 2844 @2017

'''
import wpilib
from networktables import NetworkTables


class SteampedeRobot(wpilib.IterativeRobot):
    ''' robot code for steampede '''

    def __init__(self):
        super().__init__()

        self.smart_dashboard = None
        self.shooter_speed = 1.0
        self.shooter_enabled = False
        self.loader_enabled = False
        self.gear_arm_up = False
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

        # initialize and launch the camera
        wpilib.CameraServer.launch()

        # object that handles basic drive operatives
        self.drive_rf_motor = wpilib.Victor(6)
        self.drive_rr_motor = wpilib.Victor(7)
        self.drive_lf_motor = wpilib.Victor(8)
        self.drive_lr_motor = wpilib.Victor(9)
        self.shooter_motor = wpilib.Victor(0)
        self.gear_arm_motor = wpilib.Spark(1)
        self.loader_motor = wpilib.Spark(2)

        self.drive = wpilib.RobotDrive(self.drive_lf_motor, self.drive_lr_motor,
                                       self.drive_rf_motor, self.drive_rr_motor)

        self.drive.setExpiration(0.1)

        # joysticks 1 & 2 on the driver station
        self.left_stick = wpilib.Joystick(0)
        self.right_stick = wpilib.Joystick(1)

    def teleopInit(self):
        '''Executed at the start of teleop mode'''
        self.drive.setSafetyEnabled(True)

    def teleopPeriodic(self):
        '''Runs the motor with tank steering'''
        self.drive.tankDrive(self.left_stick, self.right_stick, True)

        if self.left_stick.getTrigger():
            self.shooter_enabled = True
            self.shooter_motor.set(self.left_stick.getAxis(wpilib.Joystick.AxisType.kZ))
        else:
            self.shooter_enabled = False
            self.shooter_motor.set(0)

        if self.right_stick.getTrigger():
            self.loader_enabled = True
            self.loader_motor.set(self.right_stick.getAxis(wpilib.Joystick.AxisType.kZ))
        else:
            self.loader_enabled = False
            self.loader_motor.set(0)


if __name__ == '__main__':
    wpilib.run(SteampedeRobot)
