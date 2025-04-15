from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port
from pybricks.tools import wait

hub = PrimeHub()

sensors = [
    ColorSensor(Port.D),  # Left
    ColorSensor(Port.B),  # Mid-left (optional)
    ColorSensor(Port.F),  # Mid-right (optional)
    ColorSensor(Port.E)   # Right
]

motor_l = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_r = Motor(Port.C)

def read_sensors():
    return [x.reflection() for x in sensors]

# this works pretty well with 3x mult
#SPEED_BASE = 350

SPEED_BASE = 500

# og was 25
THRESHOLD = 35

while True:
    sensor_data = read_sensors()
    leftleft_detect = sensor_data[0] < THRESHOLD
    rightright_detect = sensor_data[3] < THRESHOLD
    left_detect = sensor_data[1] < THRESHOLD
    right_detect = sensor_data[2] < THRESHOLD


    # If left sensor detects line, turn right until right detects too
    if (leftleft_detect or left_detect) and (not rightright_detect or right_detect):
        motor_l.run(SPEED_BASE * 0.2)
        motor_r.run(SPEED_BASE * 1.7)
        while True:
            sensor_data = read_sensors()
            if sensor_data[3] < THRESHOLD:  # Right sensor sees line
                break

    # If right sensor detects line, turn left until left detects too
    elif (rightright_detect or right_detect) and (not leftleft_detect or left_detect):
        motor_l.run(SPEED_BASE * 1.7)
        motor_r.run(SPEED_BASE * 0.2)
        while True:
            sensor_data = read_sensors()
            if sensor_data[0] < THRESHOLD:  # Left sensor sees line
                break

    # If both or none detect, go straight
    else:
        motor_l.run(SPEED_BASE * 4)
        motor_r.run(SPEED_BASE * 4)

    # print("Sensor reflections:", sensor_data)
    wait(5)
