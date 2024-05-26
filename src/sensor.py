from typing import Union

from bme680 import (
    BME680,
    ENABLE_GAS_MEAS,
    FILTER_SIZE_3,
    I2C_ADDR_PRIMARY,
    I2C_ADDR_SECONDARY,
    OS_2X,
    OS_4X,
    OS_8X,
)


STANDARD_ATMOSPHERE_PA = 1013.25


class PressureSensor:
    sensor: BME680

    def __init__(self) -> None:
        try:
            self.sensor = BME680(I2C_ADDR_PRIMARY)
        except (RuntimeError, IOError):
            self.sensor = BME680(I2C_ADDR_SECONDARY)

        self.sensor.set_humidity_oversample(OS_2X)
        self.sensor.set_pressure_oversample(OS_4X)
        self.sensor.set_temperature_oversample(OS_8X)
        self.sensor.set_filter(FILTER_SIZE_3)
        self.sensor.set_gas_status(ENABLE_GAS_MEAS)

    def read(self) -> Union[int, float]:
        if self.sensor.get_sensor_data():
            return self.sensor.data.pressure

        return STANDARD_ATMOSPHERE_PA
