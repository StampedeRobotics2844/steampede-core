from wpilib.command import TimedCommand


class RaiseArmCommand(TimedCommand):
    def __init__(self, power, duration):
        super().__init__('raise arm power: {0}, duration: {1}'.format(power, duration), duration)

        self.power = power
        self.duration = duration        

    def initialize():
        print("initialize raise arm")

    def end():
        print("end")        