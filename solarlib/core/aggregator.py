from solarlib.core import database
from solarlib.core import BatteryMonitor
from solarlib.core import ChargeController


class Aggregator:

    def __init__(self,
                 sqlitefile='/tmp2/solar.db',
                 serialpath='/dev/ttyUSBPort1',
                 serialbaud=2400,
                 serialtimeout=3,
                 modbusmethod='rtu',
                 modbuspath='/dev/ttyUSBPort2',
                 modbusparity='N',
                 modbusstopbits=1,
                 ):
        try:
            self.database = database.Database(file=sqlitefile)
            #self.serialconnection = serial.Serial(path=serialpath, baud=serialbaud, timeout=serialtimeout)
            #self.modbusconnection = modbus.Modbus(method=modbusmethod, path=modbuspath, parity=modbusparity,
            #                                      stopbits=modbusstopbits, bytesize=8, baudrate=9600, timeout=3)
        except Exception as e:
            'Could not find or create database'
            raise e

    def collect(self, serialbytes=100, modbusreg=3):
        try:
            serial_data = self.serialconnection.read(serialbytes)
            modbus_data = self.modbusconnection.read(modbusreg)

        except Exception as e:
            raise e

    @staticmethod
    def parse(serial_data, modbus_data):
        try:
            sqlitedata = []
            return sqlitedata
        except Exception as e:
            raise e