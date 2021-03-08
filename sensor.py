import time
import RPi.GPIO as GPIO

# Pin of Input
GPIOpin = -1


def initialize_inductive_pin(pin):
    """
    Initializes the input pin required for the sensor.

    Args:
        pin: int; GPIO pin

    Returns:
        None
    """

    global GPIOpin

    GPIOpin = pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIOpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    print("Finished Initiation")
    print(GPIOpin)


def detect_metal():
    """
    Method which checks sensor input for detecting metal.

    Args:
        None

    Returns:
        None
    """

    if(GPIOpin != -1):
        state = GPIO.input(GPIOpin)

        if state:
            print("Metal!")
        else:
            print("No metal!")
    else:
        print("Initialize input ports")


def main():
    pin = 18
    initialize_inductive_pin(pin)

    while True:
        detect_metal()
        time.sleep(0.2)


if __name__ == '__main__':
    main()
