from solarlib.core.BatteryMonitor import BatteryMonitor
from solarlib.core.renogy_rover import RenogyRover
from solarlib.core.SolarDatabase import DataBase
import datetime
import time


def main():
    try:
        unixtimedata = time.time()
        datetimedata = str(datetime.datetime.fromtimestamp(unixtimedata).strftime('%Y-%m-%d %H:%M:%S'))

        trimetric_data = BatteryMonitor()
        values = trimetric_data.read()
        # print('Trimetric Battery1 Voltage: ', values[0])
        # print('Trimetric Battery1 Filtered Voltage: ', values[1])
        # print('Trimetric Battery2 Voltage: ', values[2])
        # print('Trimetric Battery1 Amperage: ', values[3])
        # print('Trimetric Battery1 Filtered Amperage: ', values[4])
        # print('Trimetric Battery1 Amp Hours: ', values[5])
        # print('Trimetric Battery1 Percentage: ', values[6])
        # print('Trimetric Battery1 Wattage: ', values[7])
        # print('Trimetric Battery1 Days Since Charged: ', values[8])
        # print('Trimetric Battery1 Days Since Equalized: ', values[9])
        # print('=========================================')
        # print('=========================================')

        rover = RenogyRover('/dev/ttyUSBPort2', 1)

        # print('System Device Modbus Address: ', rover.device_address())
        # print('System Model: ', rover.model())
        # print('System Serial: ', rover.serial_number())
        # print('System Ratings - Voltage, Current: ', rover.system_voltage_current())
        # print('System Set Voltage, Recognized Voltage: ', rover.voltage_setting())
        # print('System Versions - Software, Hardware: ', rover.version())
        # print('SYSTEM CONTROLLER TEMPERATURE: ', rover.controller_temperature())
        # print('System Operating Days: ', rover.operating_days())
        # print('System Rated Discharge And Type: ', rover.system_discharge_type())
        # print('=========================================')
        #
        # print('Rover Battery Type:', rover.battery_type())
        # print('Rover Battery Capacity:', rover.battery_capacity())
        # print('ROVER BATTERY VOLTAGE (MIN):', rover.battery_min_voltage())
        # print('ROVER BATTERY VOLTAGE ACTUAL:', rover.battery_voltage())
        # print('ROVER BATTERY VOLTAGE (MAX):', rover.battery_max_voltage())
        # print('ROVER BATTERY CHARGING AMPERAGE ACTUAL:', rover.battery_current())
        # print('ROVER BATTERY CHARGING AMPERAGE (MAX):', rover.max_charging_current())
        # print('ROVER BATTERY AMP/HOURS GENERATED TODAY: ', rover.battery_charging_amp_hours_today())
        # print('ROVER BATTERY AMP/HOURS GENERATED TOTAL: ', rover.battery_charging_amp_hours_total())
        # print('ROVER BATTERY WATT/HOURS GENERATED TODAY: ', rover.power_generation_today())
        # print('ROVER BATTERY WATT/HOURS GENERATED TOTAL: ', rover.cumulative_power_generation())
        # print('ROVER BATTERY MAXIMUM WATTAGE GENERATED:', rover.max_charging_power())
        # print('ROVER BATTERY PERCENTAGE:', rover.battery_percentage())
        # print('ROVER BATTERY TEMPERATURE:', rover.battery_temperature())
        # print('ROVER BATTERY TIMES OVER DISCHARGED:', rover.battery_over_discharge())
        # print('ROVER BATTERY TIMES FULLY CHARGED:', rover.battery_full_charge())
        # print('=========================================')
        #
        # print('ROVER SOLAR PANEL VOLTAGE ACTUAL:', rover.solar_voltage())
        # print('ROVER SOLAR PANEL AMPERAGE ACTUAL:', rover.solar_current())
        # print('ROVER SOLAR PANEL WATTAGE ACTUAL:', rover.solar_power())
        # print('ROVER SOLAR PANEL CHARGING STATE NUMBER:', rover.charging_state())
        # print('ROVER SOLAR PANEL CHARGING STATE LABEL:', rover.charging_state_label())
        # print('=========================================')
        #
        # print('ROVER LOAD VOLTAGE ACTUAL:', rover.load_voltage())
        # print('ROVER LOAD AMPERAGE ACTUAL:', rover.load_current())
        # print('ROVER LOAD AMPERAGE (MAX):', rover.max_discharging_current())
        # print('ROVER LOAD WATTAGE ACTUAL:', rover.load_power())
        # print('ROVER LOAD WATTAGE (MAX):', rover.max_discharging_power())
        # print('ROVER LOAD AMP/HOURS CONSUMED TODAY:', rover.discharging_amp_hours_today())
        # print('ROVER LOAD AMP/HOURS CONSUMED TOTAL: ', rover.battery_discharging_amp_hours_total())
        # print('ROVER LOAD WATT/HOURS CONSUMED TODAY: ', rover.power_consumption_today())
        # print('ROVER LOAD WATT/HOURS CONSUMED TOTAL: ', rover.cumulative_power_consumption())
        # print('=========================================')
        # print('=========================================')

        solardatabase = DataBase('/media/pi/SOLARUSB/SolarMonitor/SolarDataCollection.db')
        solardatabase.create_table()
        # date_time = "2020-04-21 20:25:00"
        solardatabase.add_record(d_t=datetimedata, tm_v=values[0], tm_fv=values[1],
                                 tm_vb2=values[2], tm_a=values[3], tm_fa=values[4], tm_ah=values[5], tm_p=values[6],
                                 tm_w=values[7], tm_dsc=values[8], tm_dse=values[9],
                                 rr_ct=rover.controller_temperature(),
                                 rr_bvmin=rover.battery_min_voltage(),
                                 rr_bva=rover.battery_voltage(),
                                 rr_bvmax=rover.battery_max_voltage(),
                                 rr_bcaa=rover.battery_current(),
                                 rr_bcam=rover.max_charging_current(),
                                 rr_bahgtdy=rover.battery_charging_amp_hours_today(),
                                 rr_bahgttl=rover.battery_charging_amp_hours_total(),
                                 rr_bwhgtdy=rover.power_generation_today(),
                                 rr_bwhgttl=rover.cumulative_power_generation(),
                                 rr_bmwg=rover.max_charging_power(),
                                 rr_bp=rover.battery_percentage(),
                                 rr_bt=rover.battery_temperature(),
                                 rr_btod=rover.battery_over_discharge(),
                                 rr_btfc=rover.battery_full_charge(),
                                 rr_spva=rover.solar_voltage(),
                                 rr_spaa=rover.solar_current(),
                                 rr_spwa=rover.solar_power(),
                                 rr_csn=rover.charging_state(),
                                 rr_csl=rover.charging_state_label(),
                                 rr_lva=rover.load_voltage(),
                                 rr_laa=rover.load_current(),
                                 rr_lam=rover.max_discharging_current(),
                                 rr_lwa=rover.load_power(),
                                 rr_lwm=rover.max_discharging_power(),
                                 rr_lahctdy=rover.discharging_amp_hours_today(),
                                 rr_lahcttl=rover.battery_discharging_amp_hours_total(),
                                 rr_lwhctdy=rover.power_consumption_today(),
                                 rr_lwhcttl=rover.cumulative_power_consumption(),
                                 )
        solardatabase.connection.commit()

    except Exception as e:
        raise e


if __name__ in '__main__':
    main()
