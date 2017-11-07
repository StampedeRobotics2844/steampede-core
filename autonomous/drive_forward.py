from robotpy_ext.autonomous import StatefulAutonomous, timed_state


class DriveForward(StatefulAutonomous):
    MODE_NAME = 'Drive Forward'

    def initialize(self):
        self.register_sd_var('drive_speed', 1)

    @timed_state(duration=5,first=True)
    def drive_forward(self):
        self.drive.tankDrive(leftValue=-0.5, rightValue=-0.5)
