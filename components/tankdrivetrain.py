'''
Drivetrain 
'''
from wpilib import RobotDrive


class TankDriveTrain:
    rf_motor = None
    rr_motor = None
    lf_motor = None
    lr_motor = None
    left_stick = None
    right_stick = None

    def setup(self):
        self.drive = RobotDrive(self.drive_lf_motor, self.drive_lr_motor, self.drive_rf_motor, self.drive_rr_motor)
        self.drive.setExpiration(0.1)
                
    def on_enabled()
        self.drive.setSafetyEnabled(True)
        self.enabled = True

    def on_disabled()
        self.enabled = False

    def execute(self):
        self.drive.tankDrive(self.left_stick, self.right_stick, True)