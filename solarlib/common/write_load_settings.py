from solarlib.core.renogy_rover import RenogyRover


def main(arg1):
    try:
        rover = RenogyRover('/dev/ttyUSBPort2', 1)
        rrwlcd = rover.light_control_delay_write(arg1)
        # rrbc = rover.battery_capacity()
        # rrbt = rover.battery_type()
        # rrhvd = rover.high_voltage_disconnect()
        # rrclv = rover.charge_limit_voltage()
        # rrecv = rover.equalize_charge_voltage()
        # rrbcv = rover.boost_charge_voltage()
        # rrfcv = rover.float_charge_voltage()
        # rrbcrv = rover.boost_charge_return_voltage()
        # rrodcrv = rover.over_discharge_return_voltage()
        # rrlva = rover.low_voltage_alarm()
        # rrodv = rover.over_discharge_voltage()
        # rrdlv = rover.discharge_limit_voltage()
        # rroddt = rover.over_discharge_delay_time()
        # rrect = rover.equalize_charge_time()
        # rrbct = rover.boost_charge_time()
        # rreci = rover.equalize_charge_interval()
        # rrtc = rover.temperature_compensation()

        print(rrwlcd)

    except Exception as e:
        raise e


if __name__ in '__main__':
    main(5)
