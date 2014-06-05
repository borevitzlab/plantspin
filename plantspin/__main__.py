from Phidgets.PhidgetException import (
        PhidgetErrorCodes,
        PhidgetException,
        )
from Phidgets.Events.Events import (
        AttachEventArgs,
        DetachEventArgs,
        ErrorEventArgs,
        InputChangeEventArgs,
        OutputChangeEventArgs,
        SensorChangeEventArgs,
        )
from Phidgets.Devices.InterfaceKit import InterfaceKit
from sys import (
        exit,
        )
from docopt import docopt

CLI_OPTS = """
Usage:
    plantscan [-n N_IMGAGES -m MOTOR_PIN -c CAM_PIN] -d DB_FILE

Options:
    -n N_IMGAGES    Number of images per rotation. [default:  59]
    -d DB_FILE      CSV plant database.
    -m MOTOR_PIN    GPIO output pin for motor. [Default:  1]
    -c CAM_PIN      GPIO output pin for camera. [Default:  0]
"""


def get_interface_kit():
    try:
        ik = InterfaceKit()
    except RuntimeError as e:
        print("Runtime Exception: %s" % e.details)
        exit(-1)
    try:


def do_photography(opts):
    num = int(opts["-n"])

    wait_for_motor_start(opts)
    for i in xrange(num):
        take_photo(opts, i)

    wait_for_motor_stop(opts)

def time_rotate_motor(n, opts):
    ik = get_interface_kit()
    ik.setOuputState(int(opts["-m")))
    




def main(opts):
    setup_gpio_phidget(opts)
    setup_relay_phidget(opts)

    register_plant_db(opts)

    speed = time_rotate_motor(1)

    while True:
        try:
            plant_id = scan_barcode()
            fnames = make_file_names(plant_id)
            do_photography(opts)
        except KeyboardInterrupt:
            break

    # clean up everything
    close_phidgets()

