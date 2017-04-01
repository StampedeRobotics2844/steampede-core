'''
Gear Arm Lower/Raise
'''
class GearArm:
    power = tunable(default=1.0)
    duration = tunable(default=1.0)
    motor = None
    
    def __init__(self):
        pass