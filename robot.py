'''
Steampede 2017
Betty H. Fairfax
Team 2844 @2017

'''
import wpilib
import magicbot
import logging

from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton
from networktables import NetworkTables
from commands.lower_arm_command import LowerArmCommand
from commands.raise_arm_command import RaiseArmCommand
from wpilib.command.scheduler import Scheduler
from robomap import PortsList
from components.drivetrain import DriveTrain
from components.shooter import Shooter
from components.geararm import GearArm
from components.loader import Loader


class SteampedeRobot(magicbot.MagicBot):
    '''robot code for steampede'''
    tankDriveTrain = TankDriveTrain
    shooter = Shooter
    gearArm = GearArm
    loader = Loader
     
    def createObjects(self):
        '''initialize logging to capture debug messages from robot'''
        logging.basicConfig(level=logging.DEBUG)

        '''initialize camera server to stream back to dashboard'''
        wpilib.CameraServer.launch()

        self.left_joystick = wpilib.Joystick(0)
        self.right_joystick = wpilib.Joystick(1)
        
        self.tankDriveTrain_lf_motor = wpilib.Victor(motors.left_front)
        self.tankDriveTrain_rf_motor = wpilib.Victor(motors.right_front)        
        self.tankDriveTrain_lr_motor = wpilib.Victor(motors.left_rear)
        self.tankDriveTrain_rr_motor = wpilib.Victor(motors.right_rear)
        self.tankDriveTrain_left_stick = self.left_joystick
        self.tankDriveTrain_right_stick = self.right_joystick

        self.shooter_motor = wpilib.Victor(motors.shooter)
        self.gearArm_motor = wpilib.Spark(motors.gear_arm)               
        self.loader_motor = wpilib.Spark(motors.loader)

    def teleopInit(self):
        '''Executed at the start of teleop mode'''
        pass
            
    def teleopPeriodic(self):
        '''Runs the motor with tank steering'''
        wpilib.scheduler.Run()


if __name__ == '__main__':
    wpilib.run(SteampedeRobot)
