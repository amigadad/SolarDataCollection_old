import sqlite3


class Database:

    """
    :TODO: Handle Solar Database
    :sqlite file: Database file path
    :returns: Object
    """

    def __init__(self, file='/media/pi/SOLARUSB/SolarMonitor/test.db'):
        """
        :TODO: Initialize Solar Database and Connect
        :sqlite file: Database file path
        :returns: None
        """
        try:
            self.connection = self.connect(file)
            self.cursor = self.connection.cursor()
            self.init()
        except Exception as e:
            print('error database connection method')
            print(e)
            raise e

    @staticmethod
    def connect(file):
        """
        :TODO: Connect to Solar Database
        :returns: Handle to Database Connection
        """
        try:
            connection = sqlite3.connect(file)
            return connection
        except Exception as e:
            print('connection method exception')
            print(e)

    def init(self):
        """
        :TODO: Initialize Database Tables
        :returns: Bool
        """
        try:
            self.cursor.execute(
                (
                    "CREATE TABLE IF NOT EXISTS 'Raw Solar Data' ("
                    "ID INTEGER PRIMARY KEY, "
                    "'Date Time' TEXT, "
                    "'Trimetric Voltage' REAL, "
                    "'Trimetric Filtered Voltage' REAL, "
                    "'Trimetric Voltage B2' REAL, "
                    "'Trimetric Amperage' REAL, "
                    "'Trimetric Filtered Amperage' REAL, "
                    "'Trimetric Amp Hours' REAL, "
                    "'Trimetric Percentage' INTEGER, "
                    "'Trimetric Watts' REAL, "
                    "'Trimetric Days Since Charged' REAL, "
                    "'Trimetric Days Since Equalized' REAL,"
                    "'Renogy Rover Battery Voltage' REAL,"
                    "'Renogy Rover Battery Percentage' INTEGER,"
                    "'Renogy Rover Battery Temperature' INTEGER,"
                    "'Renogy Rover Controller Temperature' INTEGER,"
                    "'Renogy Rover Panel Voltage' REAL,"
                    "'Renogy Rover Panel Amperage' REAL,"
                    "'Renogy Rover Panel Wattage' INTEGER,"
                    "'Renogy Rover Charging Status' INTEGER,"
                    "'Renogy Rover Charging Status Label' TEXT,"
                    "'Renogy Rover Charging Amp Hours' INTEGER,"
                    "'Renogy Rover Charging Watt Hours' INTEGER,"
                    "'Renogy Rover Discharging Amp Hours' INTEGER)"
                )
            )
            return True
        except Exception as e:
            raise e

    def add_record(self,
                   date_time="",
                   trimetric_voltage=0,
                   trimetric_filtered_voltage=0,
                   trimetric_voltage_b2=0,
                   trimetric_amperage=0,
                   trimetric_filtered_amperage=0,
                   trimetric_amp_hours=0,
                   trimetric_percentage=0,
                   trimetric_watts=0,
                   trimetric_days_since_charged=0,
                   trimetric_days_since_equalized=0,
                   renogy_rover_battery_voltage=0,
                   renogy_rover_battery_percentage=0,
                   renogy_rover_battery_temperature=0,
                   renogy_rover_controller_temperature=0,
                   renogy_rover_panel_voltage=0,
                   renogy_rover_panel_amperage=0,
                   renogy_rover_panel_wattage=0,
                   renogy_rover_charging_status=0,
                   renogy_rover_charging_status_label="",
                   renogy_rover_charging_amp_hours=0,
                   renogy_rover_charging_watt_hours=0,
                   renogy_rover_discharging_amp_hours=0
                   ):
        """
        :TODO: Add record into database
        :returns: Bool
        """
        try:
            self.connection.commit()
            return True
        except Exception as e:
            raise e

    def commit(self):
        """
        :TODO: Commit Data
        :returns: Bool
        """
        try:
            self.connection.commit()
            return True
        except Exception as e:
            raise e

    def disconnect(self):
        """
        :TODO: Disconnect from Solar Database
        :returns: Bool
        """
        try:
            self.cursor.close()
            return True
        except Exception as e:
            raise e


if __name__ == "__main__":
    solar_database = Database()
    pass
