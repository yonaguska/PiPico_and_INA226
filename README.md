# PiPico_and_INA226

Trying to get a voltage/current sensor working on a Raspberry Pi Pico running CircuitPython. I modified an Adafruit Python driver for an INA260 to run this INA226. These two TI chips have very similar behaviors.
I get the voltage and current readings, but power always comes back as zero. I suppose I need to look deeper into the device data sheets to see if the power sampling circuits have any significant differences.
