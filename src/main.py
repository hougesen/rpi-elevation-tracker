import time
from typing import Union

from input import Input
from sensor import PressureSensor


def calculate_elevation(
    pressure_hpa: Union[int, float], pressure0_hpa: Union[int, float]
) -> Union[int, float]:
    return 44_330 * (1 - (pressure_hpa / pressure0_hpa) ** (1 / 5.5255))


class ElevationTracker:
    sensor: PressureSensor

    input: Input

    pressure0_hpa: Union[int, float]

    def __init__(self) -> None:
        self.sensor = PressureSensor()

        self.input = Input()

        self.pressure0_hpa = self.sensor.read()

    def get_pressure(self) -> Union[int, float]:
        return self.sensor.read()

    def reset_pressure0(self) -> None:
        self.pressure0_hpa = self.sensor.read()

    def read_gpio(self) -> None:
        pass

    def run(self) -> None:
        itr = 0

        while True:
            itr += 1

            print("iteration", itr)

            pressure = self.get_pressure()

            print("pressure", pressure)

            reset_state = self.input.check_reset_button()

            print("reset_state", reset_state)

            time.sleep(1)


tracker = ElevationTracker()


tracker.run()
