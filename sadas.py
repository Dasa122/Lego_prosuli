from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

sensors = [ColorSensor(Port.D), ColorSensor(Port.B), ColorSensor(Port.F), ColorSensor(Port.E)]

motor_l = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_r = Motor(Port.C)

def read_sensors():
    return [x.reflection() for x in sensors]

SPEED_BASE = 2

while True:
    sensor_data = read_sensors()

    left = 100 * SPEED_BASE
    right = 100 * SPEED_BASE

    if sensor_data[1] < 40:
        right += 320 * (3 if sensor_data[0] < 40 else 1) * SPEED_BASE
        left -= 100 * SPEED_BASE
    elif sensor_data[2] < 40:
        left += 320 * (3 if sensor_data[3] <  40 else 1) * SPEED_BASE
        right -= 100 * SPEED_BASE
    print("Sensor reflections:", sensor_data)

    motor_l.run(left)
    motor_r.run(right)