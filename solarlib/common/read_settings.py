from solarlib.core.renogy_rover import RenogyRover


def main():
    try:
        rover = RenogyRover('/dev/ttyUSBPort2', 1)
        rrvs = rover.voltage_setting()

        print(rrvs)

    except Exception as e:
        raise e


if __name__ in '__main__':
    main()
