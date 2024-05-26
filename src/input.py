import RPi.GPIO as GPIO


class Input:
    reset_button_pin = 36

    def __init__(self) -> None:
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.reset_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def check_reset_button(self) -> bool:
        state = GPIO.input(self.reset_button_pin)

        return state == 0
