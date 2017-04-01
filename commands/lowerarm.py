import logging
import wpilib.command


class LowerArmCommand(wpilib.command.TimedCommand):
    def __init__(self, power, duration):
        super().__init__('lower arm power', duration)

        self.power = power
        self.duration = duration

        logging.getLogger().info("lower arm")
    
    def initialize(self):
        logging.getLogger().info("initializing")

    def execute(self):
        logging.getLogger().info("execute")

    def isFinished(self):
        logging.getLogger().info("is finished")
        return super().isFinished()

    def end(self):
        logging.getLogger().info("ending")
