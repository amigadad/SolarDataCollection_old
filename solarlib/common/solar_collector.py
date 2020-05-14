from solarlib.core.aggregator import Aggregator


def main():
    try:
        #TrailerSolar = Aggregator(sqlitefile='/media/pi/SOLARUSB/SolarMonitor/SolarDataCollectionTest2.db')
        create_database = Aggregator()
        #print(create_database)
    except Exception as e:
        raise e


if __name__ in '__main__':
    main()
