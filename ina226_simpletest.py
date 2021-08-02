# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_ina226

i2c = board.I2C()
ina226 = adafruit_ina226.INA226(i2c)
while True:
    print(
        "Current: %.2f mA Voltage: %.2f V Power:%.2f mW"
        % (ina226.current, ina226.voltage, ina226.power)
    )
    time.sleep(1)
