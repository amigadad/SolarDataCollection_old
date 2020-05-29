"""
Driver for the Renogy Rover Solar Controller using the Modbus RTU protocol
"""

import minimalmodbus

minimalmodbus.BAUDRATE = 9600
minimalmodbus.TIMEOUT = 0.5


PRODUCT_TYPE = {
    0: 'controller',
    1: 'inverter',
}

BATTERY_TYPE = {
    0: 'user',
    1: 'open',
    2: 'sealed',
    3: 'gel',
    4: 'lithium',
    5: 'self-customized'
}

CHARGING_STATE = {
    0: 'deactivated',
    1: 'activated',
    2: 'mppt',
    3: 'equalizing',
    4: 'boost',
    5: 'floating',
    6: 'current limiting'
}


class RenogyRover(minimalmodbus.Instrument):
    """
    Communicates using the Modbus RTU protocol (via provided USB<->RS232 cable)
    """

    def __init__(self, port_name, slave_address):
        minimalmodbus.Instrument.__init__(self, port_name, slave_address)

    def system_voltage_current(self):
        """
        Read the controler's maximum system voltage and charging current
        Returns a tuple of (voltage, current)
        """
        register = self.read_register(10)
        amps = register & 0x00ff
        voltage = register >> 8
        return voltage, amps

    def system_discharge_type(self):
        """
        Read the controler's rated discharging current and product type
        Returns a tuple of (current, type)
        """
        register = self.read_register(11)
        prod_type = PRODUCT_TYPE.get(register & 0x00ff)
        amps = register >> 8
        return amps, prod_type

    def model(self):
        """
        Read the controller's model information
        """
        return self.read_string(12, numberOfRegisters=8).strip()

    def version(self):
        """
        Read the controler's software and hardware version information
        Returns a tuple of (software version, hardware version)
        """
        registers = self.read_registers(20, 4)
        soft_major = registers[0] & 0x00ff
        soft_minor = registers[1] >> 8
        soft_patch = registers[1] & 0x00ff
        hard_major = registers[2] & 0x00ff
        hard_minor = registers[3] >> 8
        hard_patch = registers[3] & 0x00ff
        software_version = 'V{}.{}.{}'.format(soft_major, soft_minor, soft_patch)
        hardware_version = 'V{}.{}.{}'.format(hard_major, hard_minor, hard_patch)
        return software_version, hardware_version

    def serial_number(self):
        """
        Read the controller's serial number
        """
        registers = self.read_registers(24, 2)
        return '{}{}'.format(registers[0], registers[1])

    def device_address(self):
        """
        Read the controller/inverter modbus address
        """
        register = self.read_register(26)
        address = register & 0x00ff
        return address

    def battery_percentage(self):
        """
        Read the battery state of charge (%)
        """
        return self.read_register(256) & 0x00ff

    def battery_voltage(self):
        """
        Read the battery voltage (Voltage)
        """
        return self.read_register(257, numberOfDecimals=1)

    def battery_current(self):
        """
        Read the charging current to battery (Amperage)
        """
        return self.read_register(258, numberOfDecimals=2)

    def battery_temperature(self):
        """
        Read the battery sensor temperature (Celsius)
        """
        register = self.read_register(259)
        battery_temp_bits = register & 0x00ff
        temp_value = battery_temp_bits & 0x0ff
        sign = battery_temp_bits >> 7
        battery_degrees = -(temp_value - 128) if sign == 1 else temp_value
        return battery_degrees

    def controller_temperature(self):
        """
        Read the charge controller temperature (Celsius)
        """
        register = self.read_register(259)
        controller_temp_bits = register >> 8
        temp_value = controller_temp_bits & 0x0ff
        sign = controller_temp_bits >> 7
        controller_degrees = -(temp_value - 128) if sign == 1 else temp_value
        return controller_degrees

    def load_voltage(self):
        """
        Read load voltage (Volts)
        """
        return self.read_register(260, numberOfDecimals=1)

    def load_current(self):
        """
        Read load current (Amps)
        """
        return self.read_register(261, numberOfDecimals=2)

    def load_power(self):
        """
        Read load power (Watts)
        """
        return self.read_register(262)

    def solar_voltage(self):
        """
        Read solar panel voltage (Voltage)
        """
        return self.read_register(263, numberOfDecimals=1)

    def solar_current(self):
        """
        Read solar current (Amperage)
        """
        return self.read_register(264, numberOfDecimals=2)

    def solar_power(self):
        """
        Read solar power (Watts)
        """
        return self.read_register(265)

    def battery_min_voltage(self):
        """
        Read battery minimum voltage for today (Voltage)
        """
        return self.read_register(267, numberOfDecimals=1)

    def battery_max_voltage(self):
        """
        Read battery maximum voltage for today (Voltage)
        """
        return self.read_register(268, numberOfDecimals=1)

    def max_charging_current(self):
        """
        Read maximum charging current for today (Amperage)
        """
        return self.read_register(269, numberOfDecimals=2)

    def max_discharging_current(self):
        """
        Read maximum discharging current for today (Amperage)
        """
        return self.read_register(270, numberOfDecimals=2)

    def max_charging_power(self):
        """
        Read maximum charging power for today (Watts)
        """
        return self.read_register(271)

    def max_discharging_power(self):
        """
        Read maximum discharging power for today (Watts)
        """
        return self.read_register(272)

    def battery_charging_amp_hours_today(self):
        """
        Read charging amp hours for the current day (Amp Hours)
        """
        return self.read_register(273)

    def discharging_amp_hours_today(self):
        """
        Read discharging amp hours for the current day (Amp Hours)
        """
        return self.read_register(274)

    def power_generation_today(self):
        """
        Read power generation for the current day (Watt Hours)
        """
        return self.read_register(275)

    def power_consumption_today(self):
        """
        Read power consumption for the current day (Watt Hours)
        """
        return self.read_register(276)

    def operating_days(self):
        """
        Read the total number of operating days (Days)
        """
        return self.read_register(277)

    def battery_over_discharge(self):
        """
        Read the total number of times the battery was over discharged
        """
        return self.read_register(278)

    def battery_full_charge(self):
        """
        Read the total number of times the battery was fully charged
        """
        return self.read_register(279)

    def battery_charging_amp_hours_total(self):
        """
        Read the total number of charging amp hours of the battery (Amp Hours)
        """
        registers = self.read_registers(280, 2)
        return int(str(registers[0]) + str(registers[1]))

    def battery_discharging_amp_hours_total(self):
        """
        Read the total number of discharging amp hours of the battery (Amp Hours)
        """
        registers = self.read_registers(282, 2)
        return int(str(registers[0]) + str(registers[1]))

    def cumulative_power_generation(self):
        """
        Read the cumulative power generation (Watt Hours * 10)
        """
        registers = self.read_registers(284, 2)
        return int(str(registers[0]) + str(registers[1]))

    def cumulative_power_consumption(self):
        """
        Read the cumulative power consumption (Watt Hours * 10)
        """
        registers = self.read_registers(286, 2)
        return int(str(registers[0]) + str(registers[1]))

    def charging_state(self):
        """
        Read the charging state number from the controller
        """
        return self.read_register(288) & 0x00ff

    def charging_state_label(self):
        """
        assign text label equivalent to charging state number
        """
        return CHARGING_STATE.get(self.charging_state())

    def battery_capacity(self):
        """
        Read the nominal battery capacity (%)
        """
        return self.read_register(57346)

    def voltage_setting(self):
        """
        Read the voltage setting and recognized voltage of the controller
        """
        register = self.read_register(57347)
        setting = register >> 8
        recognized_voltage = register & 0x00ff
        return setting, recognized_voltage

    def battery_type(self):
        """
        Read the battery type setting of the controller
        """
        register = self.read_register(57348)
        return BATTERY_TYPE.get(register)

    def light_control_delay(self):
        """
        Read the light control delay
        """
        return self.read_register(57374)

    def light_control_delay_write(self, value):
        """
        Write the light control delay
        """
        return self.write_register(57374, value)

    def system_info(self):
        try:
            return {
                'model': self.model(),
                'serial_number': self.serial_number(),
                'system_voltage_current': self.system_voltage_current(),
                'system_soft_hard_version': self.version(),
                'temperature_c': self.controller_temperature(),
                'operating_days': self.operating_days(),
                'discharge_type': self.system_discharge_type()
            }
        except Exception as e:
            raise e

    def solar_status(self):
        try:
            return {
                'voltage': self.solar_voltage(),
                'current': self.solar_current(),
                'power': self.solar_power(),
                'charging_status': self.charging_state(),
                'charging_status_label': self.charging_state_label()
            }
        except Exception as e:
            raise e

    def battery_status(self):
        try:
            return {
                'percentage': self.battery_percentage(),
                'type': self.battery_type(),
                'capacity': self.battery_capacity(),
                'voltage': self.battery_voltage(),
                'voltage_min': self.battery_min_voltage(),
                'voltage_max': self.battery_max_voltage(),
                'current': self.battery_current(),
                'current_max': self.max_charging_current(),
                'amp_hrs': self.battery_charging_amp_hours_today(),
                'power_max': self.max_charging_power(),
                'watt_hrs': self.power_generation_today(),
                'temperature_c': self.battery_temperature()

            }
        except Exception as e:
            raise e

    def load_status(self):
        try:
            return {
                'voltage': self.load_voltage(),
                'current': self.load_current(),
                'current_max': self.max_discharging_current(),
                'power': self.load_power(),
                'power_max': self.max_discharging_power(),
                'amp_hrs': self.discharging_amp_hours_today(),

            }
        except Exception as e:
            raise e

    # TODO: resume at 3.10 of spec


if __name__ == "__main__":

    rover = RenogyRover('/dev/ttyUSBPort2', 1)
    print('System Info: ', rover.system_info())
    # print('Battery Status: ', rover.battery_status())
    # print('Solar Status: ', rover.solar_status())

    # print('Battery Voltage:', rover.battery_status()['voltage'])
    # print('Battery Percentage:', rover.battery_status()['percentage'])
    # print('Battery Temperature:', rover.battery_status()['temperature_c'])

    # print('Solar Voltage:', rover.solar_status()['voltage'])
    # print('Solar Current:', rover.solar_status()['current'])
    # print('Solar Wattage:', rover.solar_status()['power'])
    # print('Solar Charging Status:', rover.solar_status()['charging status'])

    print('Model: ', rover.model())
    print('Serial Number: ', rover.serial_number())
    # print('Battery %: ', rover.battery_percentage())
    # print('Battery Type: ', rover.battery_type())
    # print('Battery Capacity: ', rover.battery_capacity())
    # print('Battery Voltage: ', rover.battery_voltage())
    # battery_temp = rover.battery_temperature()
    # print('Battery Temperature (c): ', battery_temp)
    # print('Battery Temperature (f): ', battery_temp * 1.8 + 32)
    # controller_temp = rover.controller_temperature()
    # print('Controller Temperature (c): ', controller_temp)
    # print('Controller Temperature (f): ', controller_temp * 1.8 + 32)
    # print('Load Voltage: ', rover.load_voltage())
    # print('Load Current: ', rover.load_current())
    # print('Load Power: ', rover.load_power())
    # print('Charging Status: ', rover.charging_status())
    # print('Solar Voltage: ', rover.solar_voltage())
    # print('Solar Current: ', rover.solar_current())
    # print('Solar Power: ', rover.solar_power())
    # print('Power Generated Today (watt hours): ', rover.power_generation_today())
    # print('Charging Amp/Hours Today: ', rover.charging_amp_hours_today())
    # print('Discharging Amp/Hours Today: ', rover.discharging_amp_hours_today())
    # print('System Voltage Current: ', rover.system_voltage_current())
    # rover.light_control_delay_write(7)
    print('Light Control Delay: ', rover.light_control_delay())
