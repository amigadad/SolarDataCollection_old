import serial
import re


class BatteryMonitor:

    def __init__(self, path='/dev/ttyUSBPort1', baud=2400, timeout=3):
        try:
            self.connection = self.connect(path, baud, timeout)
            self.reg_v = re.compile(r'(?<=,V=)-?\d+.\d+(?=,)')
            self.reg_fv = re.compile(r'(?<=,FV=)-?\d+\.\d+(?=,)')
            self.reg_v2 = re.compile(r'(?<=,V2=)-?\d+\.\d+(?=,)')
            self.reg_a = re.compile(r'(?<=,A=)-?\d+\.?\d+(?=,)')
            self.reg_fa = re.compile(r'(?<=,FA=)-?\d+\.?\d+(?=,)')
            self.reg_ah = re.compile(r'(?<=,AH=)-?\d+\.?\d+?(?=,)')
            self.reg_p = re.compile(r'(?<=,%=)-?\d+(?=,)')
            self.reg_w = re.compile(r'(?<=,W=)-?\d+\.?\d+?(?=,)')
            self.reg_dsc = re.compile(r'(?<=,DSC=)-?\d+\.?\d+(?=,)')
            self.reg_dse = re.compile(r'(?<=,DSE=)-?\d+\.?\d+?(?=,)')
        except Exception as e:
            raise e

    @staticmethod
    def connect(path, baud, timeout):
        try:
            connection = serial.Serial(path, baudrate=baud, timeout=timeout)
            return connection
        except Exception as e:
            raise e

    def read(self, number_bytes=100):
        try:
            read_data = self.connection.read(number_bytes)
            return self.parse(read_data)
        except Exception as e:
            raise e

    def parse(self, parse_data):
        try:
            data = parse_data.decode('utf-8')
            volts = filtered_volts = volts2 = amps = filtered_amps = 0
            amp_hours = battery_percentage = watts = dsc = dse = 0
            if bool(re.search(self.reg_v, data)):
                volts = float(re.search(self.reg_v, data).group(0))
            if bool(re.search(self.reg_fv, data)):
                filtered_volts = float(re.search(self.reg_fv, data).group(0))
            if bool(re.search(self.reg_v2, data)):
                volts2 = float(re.search(self.reg_v2, data).group(0))
            if bool(re.search(self.reg_a, data)):
                amps = float(re.search(self.reg_a, data).group(0))
            if bool(re.search(self.reg_fa, data)):
                filtered_amps = float(re.search(self.reg_fa, data).group(0))
            if bool(re.search(self.reg_ah, data)):
                amp_hours = float(re.search(self.reg_ah, data).group(0))
            if bool(re.search(self.reg_p, data)):
                battery_percentage = int(re.search(self.reg_p, data).group(0))
            if bool(re.search(self.reg_w, data)):
                watts = float(re.search(self.reg_w, data).group(0))
            if bool(re.search(self.reg_dsc, data)):
                dsc = float(re.search(self.reg_dsc, data).group(0))
            if bool(re.search(self.reg_dse, data)):
                dse = float(re.search(self.reg_dse, data).group(0))
            data = [volts, filtered_volts, volts2, amps, filtered_amps,
                    amp_hours, battery_percentage, watts, dsc, dse]
            return data
        except Exception as e:
            raise e


if __name__ == "__main__":
    Trimetric_Data = BatteryMonitor()
    values = Trimetric_Data.read()
    print('Battery Voltage: ', values[0])
    print('Battery Filtered Voltage: ', values[1])
    print('Battery2 Voltage: ', values[2])
    print('Battery Amperage: ', values[3])
    print('Battery Filtered Amperage: ', values[4])
    print('Battery Amp Hours: ', values[5])
    print('Battery Percentage: ', values[6])
    print('Battery Wattage: ', values[7])
    print('Days Since Charged: ', values[8])
    print('Days Since Equalized: ', values[9])
    print(values)
