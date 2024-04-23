'''Serial_Sallam.py'''
import serial
import time
import csv
import serial.tools.list_ports
a=serial.tools.list_ports.comports()
print(a)
acceleration_listx = []
acceleration_listy = []
acceleration_listz = []
def get_serial():
#setting communication port with BudRate 
    serialCom = serial.Serial('COM3',9600)

#reseting arduino for fresh input
    serialCom.setDTR(False)
    time.sleep(1)
    serialCom.flushInput()
    serialCom.setDTR(True)
    k = 10000 #number of samples
    print("HOLD")
    time.sleep(5)
    print("Starting to aquirie data")
    start_time = time.time()
#aquiring data from the serial port
    for i in range(k):
        try:
            accelorometer_data = serialCom.readline()
            accelorometer_data = accelorometer_data.decode()
            accelorometer_data = accelorometer_data.strip('/r/n')
            #accelorometer_data =float(accelorometer_data)
            acceleration_listx.append(accelorometer_data)
            accelorometer_data = serialCom.readline()
            accelorometer_data = accelorometer_data.decode()
            accelorometer_data = accelorometer_data.strip('\r\n')
            #accelorometer_data =float(accelorometer_data)
            acceleration_listy.append(accelorometer_data)
            accelorometer_data = serialCom.readline()
            accelorometer_data = accelorometer_data.decode()
            accelorometer_data = accelorometer_data.strip('\r\n')
            #accelorometer_data =float(accelorometer_data)
            acceleration_listz.append(accelorometer_data)
            time.sleep(0.001)

        except:
            print("Error encountered, line was not recorded.")
    print("Data has been aquired")
    end_time = time.time()
    print("Total execution time:", end_time - start_time, "seconds")
    time.sleep(0.1)
    serialCom.close()
    print("Serial connection terminated")

#writing the data into a datasheet 
    x = open("xdata.csv","w",newline='')
    y = open("ydata.csv","w",newline='')
    z = open("zdata.csv","w",newline='')
    x.truncate()
    y.truncate()
    z.truncate()
    writer = csv.writer(x,delimiter=",")
    writer.writerow(acceleration_listx)
    writer = csv.writer(y,delimiter=",")
    writer.writerow(acceleration_listy)
    writer = csv.writer(z,delimiter=",")
    writer.writerow(acceleration_listz)

#returning data list 
def accel_listx():
    return acceleration_listx
def accel_listy():
    return acceleration_listy
def accel_listz():
    return acceleration_listz