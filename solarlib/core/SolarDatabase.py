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
            "'Renogy Rover Controller Temperature' INTEGER,"
            "'Renogy Rover Battery Voltage Min' REAL,"
            "'Renogy Rover Battery Voltage Actual' REAL,"
            "'Renogy Rover Battery Voltage Max' REAL,"
            "'Renogy Rover Battery Charging Amperage Actual' REAL,"
            "'Renogy Rover Battery Charging Amperage Max' REAL,"
            "'Renogy Rover Battery Amp Hours Generated Today' INTEGER,"
            "'Renogy Rover Battery Amp Hours Generated Total' INTEGER,"
            "'Renogy Rover Battery Watt Hours Generated Today' INTEGER,"
            "'Renogy Rover Battery Watt Hours Generated Total' INTEGER,"
            "'Renogy Rover Battery Maximum Wattage Generated' INTEGER,"
            "'Renogy Rover Battery Percentage' INTEGER,"
            "'Renogy Rover Battery Temperature' INTEGER,"
            "'Renogy Rover Battery Times Over Discharged' INTEGER,"
            "'Renogy Rover Battery Times Fully Charged' INTEGER,"
            "'Renogy Rover Solar Panel Voltage Actual' REAL,"
            "'Renogy Rover Solar Panel Amperage Actual' REAL,"
            "'Renogy Rover Solar Panel Wattage Actual' INTEGER,"
            "'Renogy Rover Charging State Number' INTEGER,"
            "'Renogy Rover Charging State Label' TEXT,"
            "'Renogy Rover Load Voltage Actual' REAL,"
            "'Renogy Rover Load Amperage Actual' REAL,"
            "'Renogy Rover Load Amperage Max' REAL,"
            "'Renogy Rover Load Wattage Actual' INTEGER,"
            "'Renogy Rover Load Wattage Max' INTEGER,"
            "'Renogy Rover Load Amp Hours Consumed Today' INTEGER,"
            "'Renogy Rover Load Amp Hours Consumed Total' INTEGER,"
            "'Renogy Rover Load Watt Hours Consumed Today' INTEGER,"
            "'Renogy Rover Load Watt Hours Consumed Total' INTEGER)"
                       )

    def add_record(self, d_t='1900-01-01 00:00:00', tm_v=0, tm_fv=0,
                   tm_vb2=0, tm_a=0, tm_fa=0, tm_ah=0, tm_p=0, tm_w=0,
                   tm_dsc=0, tm_dse=0, rr_ct=0, rr_bvmin=0, rr_bva=0, rr_bvmax=0,
                   rr_bcaa=0, rr_bcam=0, rr_bahgtdy=0, rr_bahgttl=0, rr_bwhgtdy=0, rr_bwhgttl=0,
                   rr_bmwg=0, rr_bp=0, rr_bt=0, rr_btod=0, rr_btfc=0, rr_spva=0,
                   rr_spaa=0, rr_spwa=0, rr_csn=0, rr_csl="", rr_lva=0, rr_laa=0,
                   rr_lam=0, rr_lwa=0, rr_lwm=0, rr_lahctdy=0, rr_lahcttl=0, rr_lwhctdy=0,
                   rr_lwhcttl=0):
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
            "'Renogy Rover Controller Temperature', "
            "'Renogy Rover Battery Voltage Min', "
            "'Renogy Rover Battery Voltage Actual', "
            "'Renogy Rover Battery Voltage Max', "
            "'Renogy Rover Battery Charging Amperage Actual', "
            "'Renogy Rover Battery Charging Amperage Max', "
            "'Renogy Rover Battery Amp Hours Generated Today', "
            "'Renogy Rover Battery Amp Hours Generated Total', "
            "'Renogy Rover Battery Watt Hours Generated Today', "
            "'Renogy Rover Battery Watt Hours Generated Total', "
            "'Renogy Rover Battery Maximum Wattage Generated', "
            "'Renogy Rover Battery Percentage', "
            "'Renogy Rover Battery Temperature', "
            "'Renogy Rover Battery Times Over Discharged', "
            "'Renogy Rover Battery Times Fully Charged', "
            "'Renogy Rover Solar Panel Voltage Actual', "
            "'Renogy Rover Solar Panel Amperage Actual', "
            "'Renogy Rover Solar Panel Wattage Actual', "
            "'Renogy Rover Charging State Number', "
            "'Renogy Rover Charging State Label', "
            "'Renogy Rover Load Voltage Actual', "
            "'Renogy Rover Load Amperage Actual', "
            "'Renogy Rover Load Amperage Max', "
            "'Renogy Rover Load Wattage Actual', "
            "'Renogy Rover Load Wattage Max', "
            "'Renogy Rover Load Amp Hours Consumed Today', "
            "'Renogy Rover Load Amp Hours Consumed Total', "
            "'Renogy Rover Load Watt Hours Consumed Today', "
            "'Renogy Rover Load Watt Hours Consumed Total') "            
            "VALUES ("
            "?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
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
                rr_ct,            # Renogy Rover Controller Temperature
                rr_bvmin,         # Renogy Rover Battery Voltage Min
                rr_bva,           # Renogy Rover Battery Voltage Actual
                rr_bvmax,         # Renogy Rover Battery Voltage Max
                rr_bcaa,          # Renogy Rover Battery Charging Amperage Actual
                rr_bcam,          # Renogy Rover Battery Charging Amperage Max
                rr_bahgtdy,       # Renogy Rover Battery Amp Hours Generated Today
                rr_bahgttl,       # Renogy Rover Battery Amp Hours Generated Total
                rr_bwhgtdy,       # Renogy Rover Battery Watt Hours Generated Today
                rr_bwhgttl,       # Renogy Rover Battery Watt Hours Generated Total
                rr_bmwg,          # Renogy Rover Battery Maximum Wattage Generated
                rr_bp,            # Renogy Rover Battery Percentage
                rr_bt,            # Renogy Rover Battery Temperature
                rr_btod,          # Renogy Rover Battery Times Over Discharged
                rr_btfc,          # Renogy Rover Battery Times Fully Charged
                rr_spva,          # Renogy Rover Solar Panel Voltage Actual
                rr_spaa,          # Renogy Rover Solar Panel Amperage Actual
                rr_spwa,          # Renogy Rover Solar Panel Wattage Actual
                rr_csn,           # Renogy Rover Charging State Number
                rr_csl,           # Renogy Rover Charging State Label
                rr_lva,           # Renogy Rover Load Voltage Actual
                rr_laa,           # Renogy Rover Load Amperage Actual
                rr_lam,           # Renogy Rover Load Amperage Max
                rr_lwa,           # Renogy Rover Load Wattage Actual
                rr_lwm,           # Renogy Rover Load Wattage Max
                rr_lahctdy,       # Renogy Rover Load Amp Hours Consumed Today
                rr_lahcttl,       # Renogy Rover Load Amp Hours Consumed Total
                rr_lwhctdy,       # Renogy Rover Load Watt Hours Consumed Today
                rr_lwhcttl)       # Renogy Rover Load Watt Hours Consumed Total
                       )


if __name__ == "__main__":
    SolarDatabase = DataBase('/media/pi/SOLARUSB/SolarMonitor/test3a.db')
    SolarDatabase.create_table()
    Date_Time = "2011-04-05 16:00:00"
    SolarDatabase.add_record(d_t=Date_Time, tm_v=43)
    SolarDatabase.connection.commit()
