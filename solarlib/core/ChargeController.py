from pymodbus.client.sync import ModbusSerialClient as ModbusClient


class ChargeController:

    def __init__(self,
                 method='rtu',
                 path='/dev/ttyUSBPort2',
                 parity='N',
                 stop_bits=1,
                 byte_size=8,
                 baud_rate=9600,
                 timeout=3):
        try:
            self.connection = self.connect(method,
                                           path,
                                           parity,
                                           stop_bits,
                                           byte_size,
                                           baud_rate,
                                           timeout)
        except Exception as e:
            raise e

    @staticmethod
    def connect(method, path, parity, stop_bits, byte_size, baud_rate, timeout):
        try:
            connection = ModbusClient(method=method,
                                      port=path,
                                      parity=parity,
                                      stopbits=stop_bits,
                                      bytesize=byte_size,
                                      baudrate=baud_rate,
                                      timeout=timeout)
            connection.connect()
            if connection.connect():
                return connection
            raise Exception(
                'Modbus Connection failed to open {path}'.format(
                    path=path
                )
            )
        except Exception as e:
            raise e

    def read(self, count=10, address=0x100, unit=0x01):
        try:
            holding = self.connection.read_holding_registers(address=address, count=count, unit=unit)
            read_data = holding.registers
            return self.parse(read_data)
        except Exception as e:
            raise e

    @staticmethod
    def parse(parse_data):
        try:
            # do parsing here
            return parse_data
        except Exception as e:
            raise e
