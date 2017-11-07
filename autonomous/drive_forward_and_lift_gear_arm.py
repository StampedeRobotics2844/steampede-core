from robotpy_ext.autonomous import StatefulAutonomous, timed_state


class DriveForwardAndLiftGearArm(StatefulAutonomous):
    MODE_NAME = 'Drive Forward'
    MODE_NAME = 'Lift GearArm'
    MODE_NAME = 'Drive Backwords'
    MODE_NAME = 'Lower GearArm'
    def initialize(self):
        self.register_sd_var('drive_speed', -1)
        self.register_sd_var('reverse_drive_speed', 1)
        self.register_sd_var('lift_gear_arm_speed', -.5)
        self.register_sd_var('lower_gear_arm_speed', .5)

    @timed_state(duration=3, next_state='lift_gear_arm',first=True)
    def drive_forward(self):
        self.drive.tankDrive(leftValue=self.drive_speed, rightValue=self.drive_speed)

    @timed_state(duration=.5, next_state='drive_backwards')
    def lift_gear_arm(self):
        self.drive.tankDrive(leftValue=0, rightValue=0)
        self.gear_arm_motor.set(self.lift_gear_arm_speed)

    @timed_state(duration=3, next_state='lower_gear_arm')
    def drive_backwards(self):
        self.gear_arm_motor.set(0)
        self.drive.tankDrive(leftValue=self.reverse_drive_speed, rightValue=self.reverse_drive_speed)
    
    @timed_state(duration=.5, next_state='stop')
    def lower_gear_arm(self):
        self.drive.tankDrive(leftValue=0, rightValue=0)
        self.gear_arm_motor.set(self.lower_gear_arm_speed)

    @timed_state(duration=1)
    def stop(self):
        self.gear_arm_motor.set(0)