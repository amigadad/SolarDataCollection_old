import sqlite3


class DataBase:

    def __init__(self, file='/media/pi/SOLARUSB/SolarMonitor/test2.db'):
        self.connection = sqlite3.connect(file)
        self.c = self.connection.cursor()

    def create_table(self):
        self.c.execute(
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

    def add_record(self, d_t='1900-01-01 00:00:00', tm_v=0, tm_fv=0,
                   tm_vb2=0, tm_a=0, tm_fa=0, tm_ah=0, tm_p=0, tm_w=0,
                   tm_dsc=0, tm_dse=0, rr_bv=0, rr_bp=0, rr_bt=0, rr_ct=0,
                   rr_pv=0, rr_pa=0, rr_pw=0, rr_cs=0, rr_csl="", rr_cah=0,
                   rr_cwh=0, rr_dah=0):
        self.c.execute(
            "INSERT INTO 'Raw Solar Data'("
            "'Date Time', "
            "'Trimetric Voltage', "
            "'Trimetric Filtered Voltage', "
            "'Trimetric Voltage B2', "
            "'Trimetric Amperage', "
            "'Trimetric Filtered Amperage', "
            "'Trimetric Amp Hours', "
            "'Trimetric Percentage', "
            "'Trimetric Watts', "
            "'Trimetric Days Since Charged', "
            "'Trimetric Days Since Equalized', "
            "'Renogy Rover Battery Voltage', "
            "'Renogy Rover Battery Percentage', "
            "'Renogy Rover Battery Temperature', "
            "'Renogy Rover Controller Temperature', "
            "'Renogy Rover Panel Voltage', "
            "'Renogy Rover Panel Amperage', "
            "'Renogy Rover Panel Wattage', "
            "'Renogy Rover Charging Status', "
            "'Renogy Rover Charging Status Label', "
            "'Renogy Rover Charging Amp Hours', "
            "'Renogy Rover Charging Watt Hours', "
            "'Renogy Rover Discharging Amp Hours') "            
            "VALUES ("
            "?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                d_t,              # Date Time
                tm_v,             # Trimetric Voltage
                tm_fv,            # Trimetric Filtered Voltage
                tm_vb2,           # Trimetric Voltage B2
                tm_a,             # Trimetric Amperage
                tm_fa,            # Trimetric Filtered Amperage
                tm_ah,            # Trimetric Amp Hours
                tm_p,             # Trimetric Percentage
                tm_w,             # Trimetric Watts
                tm_dsc,           # Trimetric Days Since Charged
                tm_dse,           # Trimetric Days Since Equalized
                rr_bv,            # Renogy Rover Battery Voltage
                rr_bp,            # Renogy Rover Battery Percentage
                rr_bt,            # Renogy Rover Battery Temperature
                rr_ct,            # Renogy Rover Controller Temperature
                rr_pv,            # Renogy Rover Panel Voltage
                rr_pa,            # Renogy Rover Panel Amperage
                rr_pw,            # Renogy Rover Panel Wattage
                rr_cs,            # Renogy Rover Charging Status
                rr_csl,           # Renogy Rover Charging Status Label
                rr_cah,           # Renogy Rover Charging Amp Hours
                rr_cwh,           # Renogy Rover Charging Watt Hours
                rr_dah)           # Renogy Rover Discharging Amp Hours
                       )


if __name__ == "__main__":
    MyDataBase = DataBase('/media/pi/SOLARUSB/SolarMonitor/test3.db')
    MyDataBase.create_table()
    Date_Time = "2011-04-05 16:00:00"
    MyDataBase.add_record(tm_v=43)
    MyDataBase.connection.commit()
