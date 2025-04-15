from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port
from pybricks.tools import wait

hub = PrimeHub()

sensors = [
    ColorSensor(Port.D),  # Left
    ColorSensor(Port.F),  # Mid-left (optional)
    ColorSensor(Port.E),  # Mid-right (optional)
    ColorSensor(Port.B)   # Right
]

motor_l = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_r = Motor(Port.C)

def read_sensors():
    return [x.reflection() for x in sensors]

SPEED_BASE = 100

# og was 25
THRESHOLD = 25

while sum(read_sensors()) < 100*4 - THRESHOLD*4:
    motor_l.dc(SPEED_BASE)
    motor_r.dc(SPEED_BASE)

while True:
    sensor_data = read_sensors()
    leftleft_detect = sensor_data[0] < THRESHOLD
    rightright_detect = sensor_data[3] < THRESHOLD
    left_detect = sensor_data[1] < THRESHOLD
    right_detect = sensor_data[2] < THRESHOLD


    if (leftleft_detect or left_detect) and not (rightright_detect or right_detect):
        motor_r.dc(SPEED_BASE)
        motor_l.dc(SPEED_BASE * 0.1)
        while True:
            if (sensors[2].reflection() < THRESHOLD) or (sensors[3].reflection() < THRESHOLD):  # Left sensor sees line
                break

    elif (rightright_detect or right_detect) and not (leftleft_detect or left_detect):
        motor_l.dc(SPEED_BASE)
        motor_r.dc(SPEED_BASE * 0.1)
        while True:
            if (sensors[0].reflection() < THRESHOLD) or (sensors[1].reflection() < THRESHOLD):  # Left sensor sees line
                break

    else:
        motor_l.dc(SPEED_BASE)
        motor_r.dc(SPEED_BASE)
