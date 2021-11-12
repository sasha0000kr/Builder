#!python3.9
import os
import sys
import glob
import zipfile
#import time

terminalmode = False
silentmode = False

#keys
if len (sys.argv) >= 2:

    key = sys.argv [1]

    if key == "-s":
        silentmode = True
    if key == "--silent":
        silentmode = True



if silentmode == False:
    print ("Orbicraft builder ver: " + "0.98" + " beta" + " " + "by Alexandr Krasnow")

if len (sys.argv) == 3:
    #print ("Enter the path to your program without a file name, if you want to use the current path, then specify the -h key")

    path = sys.argv [2]

    checkpath = os.path.exists(path)
    if checkpath == True:
        checkpath = os.path.isfile(path)
        if checkpath == False:
            os.chdir (path)
            terminalmode = True
        else:
            if silentmode == False:
                print ("\nWARNING!!!")
                print ("Do not specify the file name\n")
            quit ()
    else:
        if silentmode == False:
            print ("\nWARNING!!!")
            print ("Path not found\n")
        quit ()
file = 0

for file in glob.glob("*.c"):
    if silentmode == False:
        print ("\nUsing file:")
        print (file)
        print ("Extracting a short file name..." )
    file = file.lower ()
    shortfile = file [::-1]
    shortfile = shortfile [2:]
    shortfile = shortfile [::-1]
    if silentmode == False:
        print ("OK  Shortname: %s\n" % shortfile )

        print ("Building 'libschsat.h' ...")
    f = open ("libschsat.h", 'wt')
    f.write ("/* This file was automatically generated.  Do not edit! */\n")
    f.write ("#ifndef LIBSCHSAT_H_\n")
    f.write ("#define LIBSCHSAT_H_\n")
    f.write ("#include <stdlib.h>\n")
    f.write ("#include <stdio.h>\n")
    f.write ("#include <stdint.h>\n")
    f.write ("#include <string.h>\n")
    f.write ("#include <math.h>\n")
    f.write ("#include <sys/time.h>\n")
    f.write ("#define LSS_OK 0\n")
    f.write ("#define LSS_ERROR 1\n")
    f.write ("#define LSS_BREAK 2\n")
    f.write ("float battery_get_charge(void);\n")
    f.write ("float battery_get_charging_current(void);\n")
    f.write ("float battery_get_discharging_current(void);\n")
    f.write ("int accelerometer_get_state(uint16_t num);\n")
    f.write ("int accelerometer_request_raw(uint16_t num,int16_t *pRAW_dataX,int16_t *pRAW_dataY,int16_t *pRAW_dataZ);\n")
    f.write ("int accelerometer_request_reset(uint16_t num);\n")
    f.write ("int accelerometer_turn_off(uint16_t num);\n")
    f.write ("int accelerometer_turn_on(uint16_t num);\n")
    f.write ("int arm_get_state(uint16_t num);\n")
    f.write ("int arm_request_reset(uint16_t num);\n")
    f.write ("int arm_set_value(uint16_t num,uint8_t value,uint8_t *confirm);\n")
    f.write ("int arm_turn_off(uint16_t num);\n")
    f.write ("int arm_turn_on(uint16_t num);\n")
    f.write ("int bus_setup(void);\n")
    f.write ("int camera_get_state(void);\n")
    f.write ("int camera_take_photo(uint16_t num);\n")
    f.write ("int camera_turn_off(void);\n")
    f.write ("int camera_turn_on(void);\n")
    f.write ("int cobs_command(const uint8_t *z,int n);\n")
    f.write ("int cobs_request(const uint8_t *z,int n,uint8_t **zz,int *nn);\n")
    f.write ("int cobs_single_request(const uint8_t *z,int n,uint8_t **zz,int *nn);\n")
    f.write ("int coil_get_state(uint16_t num);\n")
    f.write ("int coil_request_reset(uint16_t num);\n")
    f.write ("int coil_set_value(uint16_t num,int16_t PWM,int16_t *confirm);\n")
    f.write ("int coil_turn_off(uint16_t num);\n")
    f.write ("int coil_turn_on(uint16_t num);\n")
    f.write ("int engine_get_state(uint16_t num);\n")
    f.write ("int engine_request_reset(uint16_t num);\n")
    f.write ("int engine_set_value(uint16_t num,int16_t value,int16_t *confirm);\n")
    f.write ("int engine_turn_off(uint16_t num);\n")
    f.write ("int engine_turn_on(uint16_t num);\n")
    f.write ("int fan_get_state(uint16_t num);\n")
    f.write ("int fan_request_reset(uint16_t num);\n")
    f.write ("int fan_request_speed(uint16_t num,int16_t *pRPM);\n")
    f.write ("int fan_set_speed(uint16_t num,int16_t RPM,int16_t *confirm);\n")
    f.write ("int fan_turn_off(uint16_t num);\n")
    f.write ("int fan_turn_on(uint16_t num);\n")
    f.write ("int gyro_get_state(uint16_t num);\n")
    f.write ("int gyro_request_raw(uint16_t num,int16_t *pRAW_dataX,int16_t *pRAW_dataY,int16_t *pRAW_dataZ);\n")
    f.write ("int gyro_request_reset(uint16_t num);\n")
    f.write ("int gyro_turn_off(uint16_t num);\n")
    f.write ("int gyro_turn_on(uint16_t num);\n")
    f.write ("int hyro_get_state(uint16_t num);\n")
    f.write ("int hyro_request_raw(uint16_t num,int16_t *pRAW_dataX,int16_t *pRAW_dataY,int16_t *pRAW_dataZ);\n")
    f.write ("int hyro_request_reset(uint16_t num);\n")
    f.write ("int hyro_turn_off(uint16_t num);\n")
    f.write ("int hyro_turn_on(uint16_t num);\n")
    f.write ("int instrument_attach(const char *name,uint16_t port);\n")
    f.write ("int instrument_detach(void);\n")
    f.write ("int instrument_measure(char *buf,int len,char **pa,int *pi,int secs);\n")
    f.write ("int light_sensor_get_state(uint16_t num);\n")
    f.write ("int light_sensor_request_maxraw(uint16_t num,uint16_t *pMAXRAW_data);\n")
    f.write ("int light_sensor_request_raw(uint16_t num,uint16_t *pRAW_data);\n")
    f.write ("int light_sensor_request_reset(uint16_t num);\n")
    f.write ("int light_sensor_set_calibrate(uint16_t num,uint8_t mode);\n")
    f.write ("int light_sensor_set_minvalue(uint16_t num,uint16_t value);\n")
    f.write ("int light_sensor_turn_off(uint16_t num);\n")
    f.write ("int light_sensor_turn_on(uint16_t num);\n")
    f.write ("int magnetometer_get_state(uint16_t num);\n")
    f.write ("int magnetometer_request_raw(uint16_t num,int16_t *pRAW_dataX,int16_t *pRAW_dataY,int16_t *pRAW_dataZ);\n")
    f.write ("int magnetometer_request_reset(uint16_t num);\n")
    f.write ("int magnetometer_turn_off(uint16_t num);\n")
    f.write ("int magnetometer_turn_on(uint16_t num);\n")
    f.write ("int motor_get_state(uint16_t num);\n")
    f.write ("int motor_request_reset(uint16_t num);\n")
    f.write ("int motor_request_speed(uint16_t num,int16_t *pRPM);\n")
    f.write ("int motor_set_speed(uint16_t num,int16_t RPM,int16_t *confirm);\n")
    f.write ("int motor_turn_off(uint16_t num);\n")
    f.write ("int motor_turn_on(uint16_t num);\n")
    f.write ("int sun_sensor_get_state(uint16_t num);\n")
    f.write ("int sun_sensor_request_maxraw(uint16_t num,uint16_t *pMAXRAW_data1,uint16_t *pMAXRAW_data2);\n")
    f.write ("int sun_sensor_request_raw(uint16_t num,uint16_t *pRAW_data1,uint16_t *pRAW_data2);\n")
    f.write ("int sun_sensor_request_reset(uint16_t num);\n")
    f.write ("int sunsensors_angle(uint16_t positive,uint16_t negative,uint16_t ambient,double *angle);\n")
    f.write ("int sun_sensor_set_minvalue(uint16_t num,uint16_t value);\n")
    f.write ("int sun_sensor_turn_off(uint16_t num);\n")
    f.write ("int sun_sensor_turn_on(uint16_t num);\n")
    f.write ("int transceiver_get_state(uint16_t num);\n")
    f.write ("int transceiver_request_buff(uint16_t num,uint8_t *data);\n")
    f.write ("int transceiver_request_reset(uint16_t num);\n")
    f.write ("int transceiver_send(uint16_t tx_num,uint16_t rx_num,const uint8_t *data,uint16_t len);\n")
    f.write ("int transceiver_turn_off(uint16_t num);\n")
    f.write ("int transceiver_turn_on(uint16_t num);\n")
    f.write ("int transmitter_get_state(uint16_t num);\n")
    f.write ("int transmitter_request_reset(uint16_t num);\n")
    f.write ("int transmitter_transmit_photo(uint16_t num,uint16_t nPhoto);\n")
    f.write ("int transmitter_turn_off(uint16_t num);\n")
    f.write ("int transmitter_turn_on(uint16_t num);\n")
    f.write ("void dump_buffer(uint8_t *buf,size_t len);\n")
    f.write ("void mSleep(int msec);\n")
    f.write ("void Sleep(int sec);\n")
    f.write ("#endif")
    f.close ()
    
    if silentmode == False:
        print ("OK  Building complite\n")
        print ("Reading file...")
        f = open ("libschsat.h", 'rt')
        print ("libschsat.h".center (65, "-"))
        print ("")
        print (    f.read ())
        print ("-".center (65, "-"))
        print ("")
        f.close ()


        print ("Building main file...")
    f = open ("main", 'wt')
    f.write ("#! /bin/bash\n"); 
    f.write ('cd "$(dirname "${0}")"\n');
    f.write ('trap "pkill -u user1 -f %s; kill -9 $$" SIGINT\n'% shortfile );
    f.write ('TIFS=$IFS\n');
    f.write ("IFS='"'&'"'\n");
    f.write ('OPTIONS=($QUERY_STRING)\n');
    f.write ('IFS=$TIFS\n');
    f.write ("./%s -t 5 -f ftp://192.168.42.42/ ${OPTIONS[@]} /dev/ttyUSB0\n" % shortfile);
    f.close ()

    if silentmode == False:
        print ("OK  Building complite\n")
        print ("Reading file...")
        f = open ("main", 'rt')
        print ("Main File".center (65, "-"))
        print ("")
        print (    f.read ())
        print ("-".center (65, "-"))
        print ("")
        f.close ()


        print ("Building Makefile...")
    f = open ("Makefile", 'wt')
    f.write ("CFLAGS = -Wall -I. -fpic -g -O2 -rdynamic\n"); 
    f.write ("LDFLAGS = -lm -lschsat -lschsat-dev -ldl\n\n");
    f.write ('%s: %s\n\n' %(shortfile, file))
    f.write ("clean:\n");
    f.write ("\trm -f %s\n" % shortfile);
    f.close ()

    if silentmode == False:
        print ("OK  Building complite\n")
        print ("Reading file...")
        f = open ("Makefile", 'rt')
        print ("Makefile".center (65, "-"))
        print ("")
        print (    f.read ())
        print ("-".center (65, "-"))
        print ("")
        f.close ()


        print ("Make zip archive...")
    zip = zipfile.ZipFile (shortfile + '.zip', 'w', compression=zipfile.ZIP_DEFLATED)

    if silentmode == False:
        print ("Building archive...")
    zip.write (file)
    zip.write ('libschsat.h')
    zip.write ("main")
    zip.write ("Makefile")
    zip.close ()

    if silentmode == False:
        print ("Ok   Buildi complite\n")

        print ("Checking zip archive...")
        print (zipfile.is_zipfile(shortfile + '.zip'))
        print ("")


    if silentmode == False:
        print ("Testing zip archive...")
        print ("ZIP".center (65, "-"))
        print ("")
        zip = zipfile.ZipFile (shortfile + '.zip', 'r')
        print (zip.    printdir ())
        print ("-".center (65, "-"))
        print ("")
        zip.close ()


    if silentmode == False:
        print ("Cleaning build files...\n")

        print ("Remove main file")
    if os.path.isfile('main'):
        os.remove ('main')
        if silentmode == False:
            print ("OK")

    if silentmode == False:
        print ("Remove libschsat.h head file")
    if os.path.isfile('libschsat.h'):
        os.remove ('libschsat.h')
        if silentmode == False:
            print ("OK")

    if silentmode == False:
        print ("Remove Makefile")
    if os.path.isfile('Makefile'):
        os.remove ('Makefile')
        if silentmode == False:
            print ("OK")

if file == 0:
    if silentmode == False:
        print ("\nWARNING!!!")
        print ("Your program file was not found!")
        print ("Make sure that builder is launched from the right place and the program has the .c file extension\n")
    if terminalmode == True:
        quit ()


if terminalmode == False:
    if silentmode == False:
        input ("--------------------\nPress Enter for exit\n")
else:
    if silentmode == False:
        print ("\n")