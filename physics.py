from pyfrc.physics import drivetrains


class PhysicsEngine:
    '''
    Simulate a motor 
    '''
    def __init__(self, physics_controller):
        self.physics_controller = physics_controller
        self.physics_controller.add_analog_gyro_channel(1)

    def update_sim(self, hal_data, now, tm_diff):
        '''
        called when the simulation parameters for the program need to be updated
        '''
        lr_motor = hal_data['pwm'][9]['value']
        rr_motor = hal_data['pwm'][7]['value']
        lf_motor = hal_data['pwm'][8]['value']
        rf_motor = hal_data['pwm'][6]['value']

        speed, rotation = drivetrains.four_motor_drivetrain(lr_motor, rr_motor, lf_motor, rf_motor)
        self.physics_controller.drive(speed, rotation, tm_diff)
 