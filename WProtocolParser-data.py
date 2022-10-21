import time
import os
from datetime import datetime
from bitstring import Bits
from configparser import ConfigParser

config = ConfigParser()

def DEF_CONFIG():
    config.write(open('config.ini', 'w'))

#DEFAULT config
if not os.path.exists('config.ini'):
        config['Taiga'] = {'DEBUG_MODE':''}
        DEF_CONFIG()
        quit()
else:
        file = 'config.ini'
        config.read(file)

DEBUG_MODE = config['MQTT']['DEBUG_MODE']

curret_time = datetime.utcnow()
current_date_string = curret_time.strftime('%m.%d.%y %H:%M:%S')

current_date_string_logs = curret_time.strftime('%m.%d.%y_%H-%M-%S')
log_name = 'logs/' + current_date_string_logs + '_(UTC)' + '_logs.txt'

def MyfileWrite(string):
        file = open(log_name,'a')
        file.write(string)
        file.close()

if not os.path.exists('logs/'):
    os.makedirs('logs/')
file = open(log_name,'w+')

print('Logging to: %s'%(str(log_name)))
MyfileWrite('Logging to: %s'%(str(log_name)))

def pars(message):
    
    message = message
    
    print("\n%s (UTC) message received: %s"%(current_date_string,message))
    MyfileWrite("\n\n%s (UTC) message received: %s"%(current_date_string,message))
    if len(message) < 3:
        return

    ########DIFINE########
    TEN_DEC = 10
    TWELVE_DEC = 12
    BASE_16 = 16

    SIZE_0_BYTE = 0
    SIZE_0DOT1_BYTE = 1
    SIZE_1_BYTE = 2
    SIZE_1DOT5_BYTE=3
    SIZE_2_BYTE = SIZE_1_BYTE+SIZE_1_BYTE
    SIZE_3_BYTE = SIZE_2_BYTE+SIZE_1_BYTE
    SIZE_4_BYTE = SIZE_3_BYTE+SIZE_1_BYTE
    SIZE_5_BYTE = SIZE_4_BYTE+SIZE_1_BYTE
    SIZE_6_BYTE = SIZE_5_BYTE+SIZE_1_BYTE
    SIZE_7_BYTE = SIZE_6_BYTE+SIZE_1_BYTE
    SIZE_8_BYTE = SIZE_7_BYTE+SIZE_1_BYTE
    SIZE_9_BYTE = SIZE_8_BYTE+SIZE_1_BYTE
    SIZE_10_BYTE = SIZE_9_BYTE+SIZE_1_BYTE
    SIZE_11_BYTE = SIZE_10_BYTE+SIZE_1_BYTE
    SIZE_12_BYTE = SIZE_11_BYTE+SIZE_1_BYTE
    SIZE_13_BYTE = SIZE_12_BYTE+SIZE_1_BYTE
    SIZE_14_BYTE = SIZE_13_BYTE+SIZE_1_BYTE
    SIZE_15_BYTE = SIZE_14_BYTE+SIZE_1_BYTE
    SIZE_16_BYTE = SIZE_15_BYTE+SIZE_1_BYTE
    SIZE_17_BYTE = SIZE_16_BYTE+SIZE_1_BYTE
    SIZE_18_BYTE = SIZE_17_BYTE+SIZE_1_BYTE
    SIZE_19_BYTE = SIZE_18_BYTE+SIZE_1_BYTE
    SIZE_20_BYTE = SIZE_19_BYTE+SIZE_1_BYTE
    
    LSB_12_BITS = 0x0FFF
    LSB_5_BITS = 0x0001F
    
    BIT_4 = 4
    BIT_5 = 5
    BIT_6 = 6
    BIT_7 = 7
    BIT_8 = 8

    FLAG_VALUE_0 = '0'
    FLAG_VALUE_1 = '1'

    STATUS_VALUE_00 ='00'
    STATUS_VALUE_01 ='01'
    STATUS_VALUE_02 ='02'

    MOVEMENT_FLAG_VALUE_0 = '0'
    MOVEMENT_FLAG_VALUE_1 = '1'

    PIN_STATE_VALUE_0x00 = 0x00
    PIN_STATE_VALUE_0x01 = 0x01

    STATE_VALUE_0x00 = 0x00
    STATE_VALUE_0x01 = 0x01
    STATE_VALUE_0x02 = 0x02
    STATE_VALUE_0x03 = 0x03
    STATE_VALUE_0x04 = 0x04
    STATE_VALUE_0x05 = 0x05
    STATE_VALUE_0x06 = 0x06
    STATE_VALUE_0x07 = 0x07
    STATE_VALUE_0x08 = 0x08

    PAYLOAD_SIZE_SIZE = 4
    SERIAL_NUMBER_SIZE = 8

    FRAME_GENERATED_0x00 = 0x00
    FRAME_GENERATED_0x01 = 0x01
    FRAME_GENERATED_0x02 = 0x02
    FRAME_GENERATED_0x03 = 0x03

    FRAME_TYPE_0x02 = 0x2
    FRAME_TYPE_0x03 = 0x3
    FRAME_TYPE_0x04 = 0x4
    FRAME_TYPE_0x05 = 0x5
    FRAME_TYPE_0x06 = 0x6
    FRAME_TYPE_0x08 = 0x8
    FRAME_TYPE_0x09 = 0x9
    FRAME_TYPE_0x10 = 0x10
    FRAME_TYPE_0x11 = 0x11
    FRAME_TYPE_0x12 = 0x12
    FRAME_TYPE_0x13 = 0x13
    FRAME_TYPE_0x14 = 0x14
    FRAME_TYPE_0x15 = 0x15
    FRAME_TYPE_0x16 = 0x16
    FRAME_TYPE_0x17 = 0x17
    FRAME_TYPE_0x18 = 0x18
    FRAME_TYPE_0x19 = 0x19
    FRAME_TYPE_0x0A = 0x0A
    FRAME_TYPE_0x0B = 0x0B
    FRAME_TYPE_0x0C = 0x0C
    FRAME_TYPE_0x0D = 0x0D
    FRAME_TYPE_0x0E = 0x0E
    FRAME_TYPE_0x0F = 0x0F
    
    # PACKET HEADER
    POWER_INFORMATION = message[:SIZE_1_BYTE]
    message = message[SIZE_1_BYTE:]
    PROTOCOL_INFORMATION = message[:SIZE_1_BYTE]
    message = message[SIZE_1_BYTE:]
    # SIZE = 2 BYTE

    POWER_INFORMATION_int = int(POWER_INFORMATION,base=BASE_16) 
    POWER_INFORMATION_int_bin = bin(POWER_INFORMATION_int) 
    TYPE_OF_POWER = str(POWER_INFORMATION_int_bin[-1:])

    TYPE_OF_POWER_VALUE_0 = 0
    TYPE_OF_POWER_VALUE_1 = 1

    BATTARY_CHARGE = int(POWER_INFORMATION_int_bin[0:9],2)

    PROTOCOL_INFORMATION_int = int(PROTOCOL_INFORMATION,base=BASE_16) 
    PROTOCOL_INFORMATION_bin = bin(PROTOCOL_INFORMATION_int)
    SERIAL_NUMBER_PRESENCE_BIT = str(PROTOCOL_INFORMATION_bin[-1:])
    INDICATES_VERSION_OF_W_PROTOCOL = str(PROTOCOL_INFORMATION_bin[-4:-1])
    PAYLOAD_SIZE_PRESENCE_BIT = str(PROTOCOL_INFORMATION_bin[-5:-4])
    RFU = str(PROTOCOL_INFORMATION_bin[-8:-5])

    PAYLOAD_SIZE_PRESENCE_BIT_VALUE_0 = '0'
    PAYLOAD_SIZE_PRESENCE_BIT_VALUE_1 = '1'
    SERIAL_NUMBER_PRESENCE_BIT_VALUE_0 = '0'
    SERIAL_NUMBER_PRESENCE_BIT_VALUE_1 = '1'
    ########DIFINE########
    
    # PACKET HEADER PARSING
    if DEBUG_MODE == '1':
        print('%s – Packet header power information (HEX) –> Type of power: %s, Battary charge: %d %% (Dec) ' % (POWER_INFORMATION,TYPE_OF_POWER,BATTARY_CHARGE))
        MyfileWrite('\n%s – Packet header power information (HEX) –> Type of power: %s, Battary charge: %d %% (Dec) ' % (POWER_INFORMATION,TYPE_OF_POWER,BATTARY_CHARGE))
        print('%s - Protocol information –> Serial number presence bit: %s, Indicates version of W-protocol: %s, Payload size presence bit: %s, RFU: %s'%\
        (PROTOCOL_INFORMATION,SERIAL_NUMBER_PRESENCE_BIT,INDICATES_VERSION_OF_W_PROTOCOL,PAYLOAD_SIZE_PRESENCE_BIT,RFU))
        MyfileWrite('\n%s - Protocol information –> Serial number presence bit: %s, Indicates version of W-protocol: %s, Payload size presence bit: %s, RFU: %s'%\
        (PROTOCOL_INFORMATION,SERIAL_NUMBER_PRESENCE_BIT,INDICATES_VERSION_OF_W_PROTOCOL,PAYLOAD_SIZE_PRESENCE_BIT,RFU))
    else:
        if TYPE_OF_POWER == TYPE_OF_POWER_VALUE_0:
                print('Battery power, Battary charge: %d %%' % (BATTARY_CHARGE))
        elif TYPE_OF_POWER == TYPE_OF_POWER_VALUE_1:
                print('External power, Battary charge: %d %%' % (BATTARY_CHARGE))
        MyfileWrite('\n%s – Packet header power information (HEX) –> Type of power: %s, Battary charge: %d %% (Dec) ' % (POWER_INFORMATION,TYPE_OF_POWER,BATTARY_CHARGE))
        MyfileWrite('\n%s - Protocol information –> Serial number presence bit: %s, Indicates version of W-protocol: %s, Payload size presence bit: %s, RFU: %s'%\
        (PROTOCOL_INFORMATION,SERIAL_NUMBER_PRESENCE_BIT,INDICATES_VERSION_OF_W_PROTOCOL,PAYLOAD_SIZE_PRESENCE_BIT,RFU))
    # SERIAL NUMBER AND PAYLOAD SIZE    
    if SERIAL_NUMBER_PRESENCE_BIT == SERIAL_NUMBER_PRESENCE_BIT_VALUE_0 and PAYLOAD_SIZE_PRESENCE_BIT == PAYLOAD_SIZE_PRESENCE_BIT_VALUE_0:
            if DEBUG_MODE == '1':
                print('Serial number field is not present; Payload size field is not present;')
                MyfileWrite('\nSerial number field is not present; Payload size field is not present;')
            else:
                MyfileWrite('\nSerisal number field is not present; Payload size field is not present;')
    elif SERIAL_NUMBER_PRESENCE_BIT == SERIAL_NUMBER_PRESENCE_BIT_VALUE_1 and PAYLOAD_SIZE_PRESENCE_BIT == PAYLOAD_SIZE_PRESENCE_BIT_VALUE_0:
        SERIAL_NUMBER = message[:SIZE_4_BYTE]
        SERIAL_NUMBER = SERIAL_NUMBER[-SIZE_1_BYTE:]+SERIAL_NUMBER[-SIZE_2_BYTE:-SIZE_1_BYTE]+SERIAL_NUMBER[-SIZE_3_BYTE:-SIZE_2_BYTE]+SERIAL_NUMBER[-SIZE_4_BYTE:-SIZE_3_BYTE]
        message = message[SERIAL_NUMBER_SIZE:]
        SERIAL_NUMBER_int = int(SERIAL_NUMBER,base=BASE_16) 
        localSerial = SERIAL_NUMBER_int
        file = open('logs/'+str(localSerial)+current_date_string_logs+'_logs.txt','a')
        file.write("\n\n%s (UTC) message received: %s"%(current_date_string,message))
        (PROTOCOL_INFORMATION,SERIAL_NUMBER_PRESENCE_BIT,INDICATES_VERSION_OF_W_PROTOCOL,PAYLOAD_SIZE_PRESENCE_BIT,RFU)
        file.close()
        if DEBUG_MODE == '1':
                print('Serial number: %d; Payload size field is not present;'%(SERIAL_NUMBER_int))
                MyfileWrite('\nSerial number: %d; Payload size field is not present;'%(SERIAL_NUMBER_int))
        else:
                print('Serial number: %d;'%(SERIAL_NUMBER_int))
                MyfileWrite('\nSerial number: %d; Payload size field is not present;'%(SERIAL_NUMBER_int))
    elif SERIAL_NUMBER_PRESENCE_BIT == SERIAL_NUMBER_PRESENCE_BIT_VALUE_1 and PAYLOAD_SIZE_PRESENCE_BIT == PAYLOAD_SIZE_PRESENCE_BIT_VALUE_1:
        SERIAL_NUMBER = message[:SIZE_4_BYTE]
        message = message[SERIAL_NUMBER_SIZE:]
        SERIAL_NUMBER = SERIAL_NUMBER[-SIZE_1_BYTE:]+SERIAL_NUMBER[-SIZE_2_BYTE:-SIZE_1_BYTE]+SERIAL_NUMBER[-SIZE_3_BYTE:-SIZE_2_BYTE]+SERIAL_NUMBER[-SIZE_4_BYTE:-SIZE_3_BYTE]
        SERIAL_NUMBER_int = int(SERIAL_NUMBER,base=BASE_16) 
        PAYLOAD_SIZE = message[:SIZE_2_BYTE]
        message = message[PAYLOAD_SIZE_SIZE:]
        PAYLOAD_SIZE_int = int(PAYLOAD_SIZE[-SIZE_1_BYTE:]+PAYLOAD_SIZE[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
        PAYLOAD_SIZE_int_bin = bin(PAYLOAD_SIZE_int)
        localSerial = SERIAL_NUMBER_int
        file = open('logs/'+str(localSerial)+current_date_string_logs+'_logs.txt','a')
        file.write("\n\n%s (UTC) message received: %s"%(current_date_string,message))
        (PROTOCOL_INFORMATION,SERIAL_NUMBER_PRESENCE_BIT,INDICATES_VERSION_OF_W_PROTOCOL,PAYLOAD_SIZE_PRESENCE_BIT,RFU)
        file.close()
        if DEBUG_MODE == '1':
                print('Serial number: %d; Payload size: %s;'%(SERIAL_NUMBER_int,PAYLOAD_SIZE_int_bin))
                MyfileWrite('\nSerial number: %d; Payload size: %s;'%(SERIAL_NUMBER_int,PAYLOAD_SIZE_int_bin))
        else:
                print('Serial number: %d; Payload size: %s;'%(SERIAL_NUMBER_int,PAYLOAD_SIZE_int_bin))
                MyfileWrite('\nSerial number: %d; Payload size: %s;'%(SERIAL_NUMBER_int,PAYLOAD_SIZE_int_bin))
    elif SERIAL_NUMBER_PRESENCE_BIT == SERIAL_NUMBER_PRESENCE_BIT_VALUE_0 and PAYLOAD_SIZE_PRESENCE_BIT == PAYLOAD_SIZE_PRESENCE_BIT_VALUE_1:
        PAYLOAD_SIZE = message[:SIZE_2_BYTE]
        message = message[PAYLOAD_SIZE_SIZE:]
        PAYLOAD_SIZE_int = int(PAYLOAD_SIZE[-SIZE_1_BYTE:]+PAYLOAD_SIZE[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
        PAYLOAD_SIZE_int_bin = bin(PAYLOAD_SIZE_int)
        if DEBUG_MODE == '1': 
                print('Serial number field is not present; Payload size: %s;'%(PAYLOAD_SIZE_int_bin))
                MyfileWrite('\nSerial number field is not present; Payload size: %s;'%(PAYLOAD_SIZE_int_bin))
        else:
                print('Payload size: %s;'%(PAYLOAD_SIZE_int_bin))
                MyfileWrite('\nSerial number field is not present; Payload size: %s;'%(PAYLOAD_SIZE_int_bin))
    # FRAME_TYPE RULESs
    while len(message) > 0:
        frame_data = message[SIZE_1_BYTE:SIZE_2_BYTE]+message[:SIZE_1_BYTE]
        if 1:
            if int(frame_data,base = BASE_16)  &LSB_12_BITS   == FRAME_TYPE_0x02:
                    #0x0200 frame type
                    b2 = message[:SIZE_2_BYTE]
                    b2_big_end = int(b2[-SIZE_1_BYTE:]+b2[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16)
                    message = message[SIZE_2_BYTE:]

                    b3 = message[:SIZE_1_BYTE]
                    int_value_b3 = int(b3,base=BASE_16)
                    message = message[SIZE_1_BYTE:]

                    b4 = message[:SIZE_1_BYTE]
                    int_value_b4 = int(b4,base=BASE_16)
                    message = message[SIZE_1_BYTE:]

                    b5 = message[0:SIZE_1_BYTE]
                    int_value_b5 = int(b5,base=BASE_16)
                    bin_value_b5 = bin(int_value_b5)
                    message = message[SIZE_1_BYTE:]

                    if DEBUG_MODE == '1': 
                        print('\n2   bytes: 0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(b2_big_end&LSB_12_BITS,b2_big_end>>TWELVE_DEC)) 
                        MyfileWrite('\n\n2 bytes: 0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(b2_big_end&LSB_12_BITS,b2_big_end>>TWELVE_DEC))
                        print('1 byte : Downlink uid: 0x%0.2X'%int_value_b3)
                        MyfileWrite('\n1 byte : Downlink uid: 0x%0.2X'%int_value_b3)
                        print('1 byte : Command code: 0x%0.2X'%int_value_b4)
                        MyfileWrite('\n1 byte : Command code: 0x%0.2X'%int_value_b4)
                        print('1 byte : Command execution result: 0x%0.2X'%int_value_b5,'\n\
                        PS :  0x00 – execution success; 0x01 – 0xFF – execution error code')
                        MyfileWrite('\n1 byte : Command execution result: 0x%0.2X'%int_value_b5)
                    else:
                        print('\nCommand confirmation frame') 
                        print('Downlink uid: 0x%0.2X'%int_value_b3)
                        print('Command code: 0x%0.2X'%int_value_b4)
                        print('Command execution result: %0.2X'%int_value_b5)

                        MyfileWrite('\n\n2 bytes: 0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(b2_big_end&LSB_12_BITS,b2_big_end>>TWELVE_DEC))
                        MyfileWrite('\n1 byte : Downlink uid: 0x%0.2X'%int_value_b3)
                        MyfileWrite('\n1 byte : Command code: 0x%0.2X'%int_value_b4)
                        MyfileWrite('\n1 byte : Command execution result: 0x%0.2X'%int_value_b5)
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x03:
                    #0x0300 frame type
                    b2 = message[:SIZE_2_BYTE]
                    b2_big_end = int(b2[-SIZE_1_BYTE:]+b2[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16)
                    message = message[SIZE_2_BYTE:]

                    b3 = message[:SIZE_4_BYTE]
                    b3_big_end = b3[-SIZE_1_BYTE:]+b3[-SIZE_2_BYTE:-SIZE_1_BYTE]+b3[-SIZE_3_BYTE:-SIZE_2_BYTE]+b3[-SIZE_4_BYTE:-SIZE_3_BYTE]
                    int_value_b3_big_eng = int(b3_big_end,base=BASE_16)
                    message = message[SIZE_4_BYTE:]

                    b4 = message[:SIZE_4_BYTE]
                    b4_big_end = b4[-SIZE_1_BYTE:]+b4[-SIZE_2_BYTE:-SIZE_1_BYTE]+b4[-SIZE_3_BYTE:-SIZE_2_BYTE]+b4[-SIZE_4_BYTE:-SIZE_3_BYTE]
                    int_value_b4_big_eng = int(b4_big_end,base=BASE_16)
                    message = message[SIZE_4_BYTE:]

                    b5 = message[:SIZE_4_BYTE]
                    b5_big_end = b5[-SIZE_1_BYTE:]+b5[-SIZE_2_BYTE:-SIZE_1_BYTE]+b5[-SIZE_3_BYTE:-SIZE_2_BYTE]+b5[-SIZE_4_BYTE:-SIZE_3_BYTE]
                    int_value_b5_big_eng = int(b5_big_end,base=BASE_16)
                    message = message[SIZE_4_BYTE:]

                    b6 = message[:SIZE_2_BYTE]
                    b6_big_end = b6[-SIZE_1_BYTE:]+b6[-SIZE_2_BYTE:-SIZE_1_BYTE]
                    int_value_b6_big_eng = int(b6_big_end,base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    b7 = message[:SIZE_2_BYTE]
                    b7_big_end = b7[-SIZE_1_BYTE:]+b7[-SIZE_2_BYTE:-SIZE_1_BYTE]
                    int_value_b7_big_eng = int(b7_big_end,base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    b8 = message[:SIZE_1_BYTE]
                    b8_big_end = b8
                    int_value_b8_big_eng = int(b8_big_end,base=BASE_16)
                    message = message[SIZE_1_BYTE:]

                    b9 = message[:SIZE_1_BYTE]
                    b9_big_end = b9
                    int_value_b9_big_eng = int(b9_big_end,base=BASE_16)
                    bin_value_b9 = bin(int_value_b9_big_eng)
                    message = message[SIZE_1_BYTE:]

                    if DEBUG_MODE == '1': 
                        print('\n2 bytes:   0x%0.2X: Type of frame,'%(b2_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(b2_big_end>>12),\
                        '    PS:  0x00 – Frame generated on regular base\n\
                                0x01 – Frame generated because of device mode change\n\
                                0x03 – Frame generated in result of platform request')
                        MyfileWrite('\n\n2 bytes: 0x%0.2X: Type of frame, 4 MSB = 0x%0.2X\n\
                                PS:  0x00 – Frame generated on regular base\n\
                                0x01 – Frame generated because of device mode change\n\
                                0x03 – Frame generated in result of platform request'%(b2_big_end&LSB_12_BITS,b2_big_end>>12))  
                        print('4 bytes: %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (b3,(datetime.timestamp(int_value_b3_big_eng))))
                        MyfileWrite('\n4 bytes: %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (b3,(datetime.timestamp(int_value_b3_big_eng))))
                        print('4 bytes: Latitude: %s' % (int_value_b4_big_eng/100000))
                        MyfileWrite('\n4 bytes: Latitude:  %s' % (int_value_b4_big_eng/100000))
                        print('4 bytes: Longitude: %s' % (int_value_b5_big_eng/100000))
                        MyfileWrite('\n4 bytes: Longitude:  %s' % (int_value_b5_big_eng/100000))
                        print('2 bytes: Height: %s' % (int_value_b6_big_eng))
                        MyfileWrite('\n2 bytes: Height:  %s' % (int_value_b6_big_eng))
                        print('2 bytes: Speed: %s ' % (int_value_b7_big_eng))
                        MyfileWrite('\n2 bytes: Speed: %s' % (int_value_b7_big_eng))
                        print('1 byte : HDOP: %s ' % (int_value_b8_big_eng/10))
                        MyfileWrite('\n1 byte: HDOP: %s' % (int_value_b8_big_eng/10))
                        print('1 byte : Satellites: %d -> %s (Binary)' % (int_value_b9_big_eng&LSB_5_BITS,bin_value_b9),'\n     PS:  Inside geofence 1 flag\n\
                                0 – device outside geofence 1, 1 – device inside geofence\n\
                                Inside geofence 2 flag\n\
                                0 – device outside geofence 2, 1 – device inside geofence 2\n\
                                Movement flag (based on accelerometer data)\n\
                                0 – if device is not in movement, 1 – if device in movement')
                        MyfileWrite('\n1 byte : Satellites: %d -> %s (Binary)\n     PS:  Inside geofence 1 flag\n\
                                0 – device outside geofence 1, 1 – device inside geofence\n\
                                Inside geofence 2 flag\n\
                                0 – device outside geofence 2, 1 – device inside geofence 2\n\
                                Movement flag (based on accelerometer data)\n\
                                0 – if device is not in movement, 1 – if device in movement'% (int_value_b9_big_eng&LSB_5_BITS,bin_value_b9))
                    else:
                        print('\nGNSS geolocation frame')

                        if b2_big_end>>TWELVE_DEC == FRAME_GENERATED_0x00:
                                print('Frame generated on regular base')
                                MyfileWrite('\n\nFrame generated on regular base')
                        elif b2_big_end>>TWELVE_DEC == FRAME_GENERATED_0x01:
                                print('Frame generated because of device mode change')
                                MyfileWrite('\n\nFrame generated because of device mode change')
                        elif b2_big_end>>TWELVE_DEC == FRAME_GENERATED_0x03:
                                print('Frame generated in result of platform request')
                                MyfileWrite('\n\nFrame generated in result of platform request')
  
                        print('Time: %s (UTC)' % (datetime.utcfromtimestamp(int_value_b3_big_eng)))
                        print('Latitude: %s' % (int_value_b4_big_eng/100000))
                        print('Longitude: %s' % (int_value_b5_big_eng/100000))
                        print('Height: %s' % (int_value_b6_big_eng))
                        print('Speed: %s' % (int_value_b7_big_eng))
                        print('HDOP: %s' % (int_value_b8_big_eng/10))
                        print('Satellites: %d' % (int_value_b9_big_eng&LSB_5_BITS))

                        MyfileWrite('\n2 bytes: 0x%0.2X: Type of frame, 4 MSB = 0x%0.2X\n\
                                PS:  0x00 – Frame generated on regular base\n\
                                0x01 – Frame generated because of device mode change\n\
                                0x03 – Frame generated in result of platform request'%(b2_big_end&LSB_12_BITS,b2_big_end>>12))  
                        MyfileWrite('\n4 bytes: %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (b3,(datetime.utcfromtimestamp(int_value_b3_big_eng))))
                        MyfileWrite('\n4 bytes: Latitude:  %s' % (int_value_b4_big_eng/100000))
                        MyfileWrite('\n4 bytes: Longitude:  %s' % (int_value_b5_big_eng/100000))
                        MyfileWrite('\n2 bytes: Height:  %s' % (int_value_b6_big_eng))
                        MyfileWrite('\n2 bytes: Speed: %s' % (int_value_b7_big_eng))
                        MyfileWrite('\n1 byte: HDOP: %s' % (int_value_b8_big_eng/10))
                        MyfileWrite('\n1 byte : Satellites: %d -> %s (Binary)\n     PS:  Inside geofence 1 flag\n\
                                0 – device outside geofence 1, 1 – device inside geofence\n\
                                Inside geofence 2 flag\n\
                                0 – device outside geofence 2, 1 – device inside geofence 2\n\
                                Movement flag (based on accelerometer data)\n\
                                0 – if device is not in movement, 1 – if device in movement'% (int_value_b9_big_eng&LSB_5_BITS,bin_value_b9))
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x04:
                #0x0400 frame type
                b2 = message[:SIZE_2_BYTE]
                b2_big_end = int(b2[-SIZE_1_BYTE:]+b2[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16)
                message = message[SIZE_2_BYTE:]

                b3 = message[:SIZE_4_BYTE]
                b3_big_end = b3[-SIZE_1_BYTE:]+b3[-SIZE_2_BYTE:-SIZE_1_BYTE]+b3[-SIZE_3_BYTE:-SIZE_2_BYTE]+b3[-SIZE_4_BYTE:-SIZE_3_BYTE]
                int_value_b3_big_eng = int(b3_big_end,base=BASE_16)
                message = message[SIZE_4_BYTE:]

                b4 = message[:SIZE_6_BYTE]
                b4_big_end = b4[-SIZE_1_BYTE:]+b4[-SIZE_2_BYTE:-SIZE_1_BYTE]+b4[-SIZE_3_BYTE:-SIZE_2_BYTE]+b4[-SIZE_4_BYTE:-SIZE_3_BYTE]+b4[-SIZE_5_BYTE:-SIZE_4_BYTE]+b4[-SIZE_6_BYTE:-SIZE_5_BYTE]
                message = message[SIZE_6_BYTE:]

                b5 = message[:SIZE_1_BYTE]
                int_value_b5_big_eng = int(b5,base = BASE_16)
                bin_value_b5 = bin(int_value_b5_big_eng)
                b5_bin_aint = Bits(bin_value_b5)
                message = message[SIZE_1_BYTE:]

                b6 = message[:SIZE_6_BYTE]
                b6_big_end = b6[-SIZE_1_BYTE:]+b6[-SIZE_2_BYTE:-SIZE_1_BYTE]+b6[-SIZE_3_BYTE:-SIZE_2_BYTE]+b6[-SIZE_4_BYTE:-SIZE_3_BYTE]+b6[-SIZE_5_BYTE:-SIZE_4_BYTE]+b6[-SIZE_6_BYTE:-SIZE_5_BYTE]
                message = message[SIZE_6_BYTE:]

                b7 = message[:SIZE_1_BYTE]
                int_value_b7_big_eng = int(b7,base = BASE_16)
                bin_value_b7 = bin(int_value_b7_big_eng)
                b7_bin_aint = Bits(bin_value_b7)
                message = message[SIZE_1_BYTE:]

                b8 = message[:SIZE_6_BYTE]
                b8_big_end = b8[-SIZE_1_BYTE:]+b8[-SIZE_2_BYTE:-SIZE_1_BYTE]+b8[-SIZE_3_BYTE:-SIZE_2_BYTE]+b8[-SIZE_4_BYTE:-SIZE_3_BYTE]+b8[-SIZE_5_BYTE:-SIZE_4_BYTE]+b8[-SIZE_6_BYTE:-SIZE_5_BYTE]
                message = message[SIZE_6_BYTE:]

                b9 = message[:SIZE_1_BYTE]
                int_value_b9_big_eng = int(b9,base=BASE_16)
                bin_value_b9 = bin(int_value_b9_big_eng)
                b9_bin_aint = Bits(bin_value_b9)
                message = message[SIZE_1_BYTE:]

                b10 = message[:SIZE_1_BYTE]
                int_value_b10 = int(b10,base=BASE_16)
                bin_value_b10 = bin(int_value_b10)
                message = message[SIZE_1_BYTE:]

                if DEBUG_MODE == '1': 
                        print('\n2 bytes:   0x%0.2X: Type of frame,'%(b2_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(b2_big_end>>12),\
                                '                                   0x00 – Frame generated on regular base\n\
                                        0x01 – Frame generated because of device mode change\n\
                                        0x03 – Frame generated in result of platform request')
                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X\n\
                                        0x00 – Frame generated on regular base\n\
                                        0x01 – Frame generated because of device mode change\n\
                                        0x03 – Frame generated in result of platform request'%(b2_big_end&LSB_12_BITS,b2_big_end>>12))
                        print('4 bytes:  %s - Frame generation timestamp (Hex) -> %s Time (UTC)' % (b3,(datetime.utcfromtimestamp(int_value_b3_big_eng))))
                        MyfileWrite('\n4 bytes:  %s - Frame generation timestamp (Hex) -> %s Time (UTC)' % (b3,(datetime.utcfromtimestamp(int_value_b3_big_eng))))
                        print('6 bytes:  BSSID1: %s'%b4)
                        MyfileWrite('\n6 bytes:  BSSID1: %s'%b4)
                        print('1 byte :  RSSI1: %d'%(int_value_b5_big_eng))
                        MyfileWrite('\n1 byte :  RSSI1: %s'%b5_bin_aint.int)
                        print('6 bytes:  BSSID2: %s'%b6)
                        MyfileWrite('\n6 bytes:  BSSID2: %s'%b6)
                        print('1 byte :  RSSI2: %s'%b7_bin_aint.int)
                        MyfileWrite('\n1 byte :  RSSI2: %s'%b7_bin_aint.int)
                        print('6 bytes:  BSSID3: %s'%b8)
                        MyfileWrite('\n6 bytes:  BSSID3: %s'%b8)
                        print('1 byte :  RSSI3: %s'%b9_bin_aint.int)
                        MyfileWrite('\n1 byte :  RSSI3: %s'%b9_bin_aint.int)
                        print('1 byte :  Additional Flags: %s\n     PS:   Movement flag (based on accelerometer data)\n\
                                        0 – if device is not in movement; 1 – if device in movement\n\
                                        Home flag of third wi-fi network\n\
                                        0 – it’s not a home network; 1 – it’s a home network\n\
                                        Home flag of second wi-fi network\n\
                                        0 – it’s not a home network; 1 – it’s a home network\n\
                                        Home flag of first wi-fi network\n\
                                        0 – it’s not a home network; 1 – it’s a home network'%bin_value_b10[SIZE_1_BYTE:SIZE_3_BYTE])
                        MyfileWrite('\n1 byte :  Additional Flags: %s\n     PS:   Movement flag (based on accelerometer data)\n\
                                        0 – if device is not in movement; 1 – if device in movement\n\
                                        Home flag of third wi-fi network\n\
                                        0 – it’s not a home network; 1 – it’s a home network\n\
                                        Home flag of second wi-fi network\n\
                                        0 – it’s not a home network; 1 – it’s a home network\n\
                                        Home flag of first wi-fi network\n\
                                        0 – it’s not a home network; 1 – it’s a home network'%bin_value_b10[SIZE_1_BYTE:SIZE_3_BYTE])
                else:
                        print('\nWi-Fi geolocation frame')

                        if b2_big_end>>TWELVE_DEC == FRAME_GENERATED_0x00:
                                print('Frame generated on regular base')
                                MyfileWrite('\n\nFrame generated on regular base')
                        elif b2_big_end>>TWELVE_DEC == FRAME_GENERATED_0x01:
                                print('Frame generated because of device mode change')
                                MyfileWrite('\n\nFrame generated because of device mode change')
                        elif b2_big_end>>TWELVE_DEC == FRAME_GENERATED_0x03:
                                print('Frame generated in result of platform request')
                                MyfileWrite('\n\nFrame generated in result of platform request')

                        print('Time: %s (UTC)' % ((datetime.utcfromtimestamp(int_value_b3_big_eng))))
                        print('BSSID1: %s'%b4)
                        print('RSSI1: %d'%(b5_bin_aint.int))
                        print('BSSID2: %s'%b6)
                        print('RSSI2: %s'%b7_bin_aint.int)
                        print('BSSID3: %s'%b8)
                        print('RSSI3: %s'%b9_bin_aint.int)

                        if bin_value_b10[-BIT_4:-BIT_5] == FLAG_VALUE_0:
                                print('Movement flag: device is not in movement')
                        elif bin_value_b10[-BIT_4:-BIT_5] == FLAG_VALUE_1:
                                print('Movement flag: device in movement')
                        
                        if bin_value_b10[-BIT_5:-BIT_6] == FLAG_VALUE_0:
                                print('Home flag of third wi-fi network: not a home network')
                        elif bin_value_b10[-BIT_5:-BIT_6] == FLAG_VALUE_1:
                                print('Home flag of third wi-fi network: a home network')

                        if bin_value_b10[-BIT_6:-BIT_7] == FLAG_VALUE_0:
                                print('Home flag of second wi-fi network: not a home network')
                        elif bin_value_b10[-BIT_6:-BIT_7] == FLAG_VALUE_1:
                                print('Home flag of second wi-fi network: a home network')

                        if bin_value_b10[-BIT_7:-BIT_8] == FLAG_VALUE_0:
                                print('Home flag of first wi-fi network: not a home network')
                        elif bin_value_b10[-BIT_7:-BIT_8] == FLAG_VALUE_1:
                                print('Home flag of first wi-fi network: a home network')

                        MyfileWrite('\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X\n\
                                        0x00 – Frame generated on regular base\n\
                                        0x01 – Frame generated because of device mode change\n\
                                        0x03 – Frame generated in result of platform request'%(b2_big_end&LSB_12_BITS,b2_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s - Frame generation timestamp (Hex) -> %s Time (UTC)' % (b3,(datetime.utcfromtimestamp(int_value_b3_big_eng))))
                        MyfileWrite('\n6 bytes:  BSSID1: %s'%b4)
                        MyfileWrite('\n1 byte :  RSSI1: %s'%b5_bin_aint.int)
                        MyfileWrite('\n6 bytes:  BSSID2: %s'%b6)
                        MyfileWrite('\n1 byte :  RSSI2: %s'%b7_bin_aint.int)
                        MyfileWrite('\n6 bytes:  BSSID3: %s'%b8)
                        MyfileWrite('\n1 byte :  RSSI3: %s'%b9_bin_aint.int)
                        MyfileWrite('\n1 byte :  Additional Flags: %s\n     PS:   Movement flag (based on accelerometer data)\n\
                                        0 – if device is not in movement; 1 – if device in movement\n\
                                        Home flag of third wi-fi network\n\
                                        0 – it’s not a home network; 1 – it’s a home network\n\
                                        Home flag of second wi-fi network\n\
                                        0 – it’s not a home network; 1 – it’s a home network\n\
                                        Home flag of first wi-fi network\n\
                                        0 – it’s not a home network; 1 – it’s a home network'%bin_value_b10[SIZE_1_BYTE:SIZE_3_BYTE])
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x05:
                    #0x0500 frame type
                    b2 = message[:SIZE_2_BYTE]
                    b2_big_end = int(b2[-SIZE_1_BYTE:]+b2[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16)
                    message = message[SIZE_2_BYTE:]

                    b3 = message[:SIZE_4_BYTE]
                    b3_big_end = b3[-SIZE_1_BYTE:]+b3[-SIZE_2_BYTE:-SIZE_1_BYTE]+b3[-SIZE_3_BYTE:-SIZE_2_BYTE]+b3[-SIZE_4_BYTE:-SIZE_3_BYTE]
                    int_value_b3_big_eng = int(b3_big_end,base=BASE_16)
                    message = message[SIZE_4_BYTE:]

                    b4 = message[:SIZE_1_BYTE]
                    b4_big_end = b4
                    int_value_b4_big_eng = int(b4_big_end,base=BASE_16)
                    message = message[SIZE_1_BYTE:]

                    b5 = message[:SIZE_1_BYTE]
                    b5_big_end = b5
                    int_value_b5_big_eng = int(b5_big_end,base=BASE_16)
                    message = message[SIZE_1_BYTE:]

                    if DEBUG_MODE == '1':
                        print('\n2 bytes:  0x%0.2X: Type of frame,'%(b2_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(b2_big_end>>12),\
                        ' '*3,'PS:  0x00 – Frame generated on regular base\n',\
                        ' '*8,'0x01 – Frame generated because of shock detection\n',\
                        ' '*8,'0x02 – Stop movement\n',\
                        ' '*8,'0x03 – Start movement')
                        print('4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (b3,(datetime.utcfromtimestamp(int_value_b3_big_eng))))
                        print('1 byte :  %s: Duration of measurement period in minutes'%int_value_b4_big_eng)
                        print('1 byte :  %s: Averaged index of motion activity in measurement interval'%int_value_b5_big_eng)

                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(b2_big_end&LSB_12_BITS,b2_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (b3,(datetime.utcfromtimestamp(int_value_b3_big_eng))))
                        MyfileWrite('\n1 byte :  %s: Duration of measurement period in minutes'%int_value_b4_big_eng)
                        MyfileWrite('\n1 byte :  %s: Averaged index of motion activity in measurement interval'%int_value_b5_big_eng)
                    else:
                        print('\nMotion activity frame')

                        if b2_big_end>>TWELVE_DEC == FRAME_GENERATED_0x00:
                                print('Frame generated on regular base')
                                MyfileWrite('\n\nFrame generated on regular base')
                        elif b2_big_end>>TWELVE_DEC == FRAME_GENERATED_0x01:
                                print('Frame generated because of shock detection')
                                MyfileWrite('\n\nFrame generated because of shock detection')
                        elif b2_big_end>>TWELVE_DEC == FRAME_GENERATED_0x02:
                                print('Stop movement')
                                MyfileWrite('\n\nStop movement')
                        elif b2_big_end>>TWELVE_DEC == FRAME_GENERATED_0x03:
                                print('Start movement')
                                MyfileWrite('\n\nStart movement')

                        print('Time: %s (UTC)' % (datetime.utcfromtimestamp(int_value_b3_big_eng)))
                        print('Measurement period duration: %s'%int_value_b4_big_eng)
                        print('Motion activity index: %s'%int_value_b5_big_eng)

                        MyfileWrite('\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(b2_big_end&LSB_12_BITS,b2_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (b3,(datetime.utcfromtimestamp(int_value_b3_big_eng))))
                        MyfileWrite('\n1 byte :  %s: Duration of measurement period in minutes'%int_value_b4_big_eng)
                        MyfileWrite('\n1 byte :  %s: Averaged index of motion activity in measurement interval'%int_value_b5_big_eng)
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x06:
                #0x0600 frame type
                b2 = message[:SIZE_2_BYTE]
                b2_big_end = int(b2[-SIZE_1_BYTE:]+b2[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16)
                message = message[SIZE_2_BYTE:]

                b3 = message[:SIZE_4_BYTE]
                b3_big_end = b3[-SIZE_1_BYTE:]+b3[-SIZE_2_BYTE:-SIZE_1_BYTE]+b3[-SIZE_3_BYTE:-SIZE_2_BYTE]+b3[-SIZE_4_BYTE:-SIZE_3_BYTE]
                int_value_b3_big_eng = int(b3_big_end,base=BASE_16)
                message = message[SIZE_4_BYTE:]

                if DEBUG_MODE == '1':
                        print('\n2 bytes: 0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(b2_big_end&LSB_12_BITS,b2_big_end>>12))
                        print('4 bytes: %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (b3,(datetime.utcfromtimestamp(int_value_b3_big_eng))))

                        MyfileWrite('\n\n2 bytes: 0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(b2_big_end&LSB_12_BITS,b2_big_end>>12))
                        MyfileWrite('\n4 bytes: %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (b3,(datetime.utcfromtimestamp(int_value_b3_big_eng))))
                else:
                        print('\nShock detection frame')

                        if b2_big_end>>TWELVE_DEC == FRAME_GENERATED_0x01:
                                print('Shock detected')
                                MyfileWrite('\n\nShock detected')

                        print('Time: %s (UTC)'% (datetime.utcfromtimestamp(int_value_b3_big_eng)))

                        MyfileWrite('\n2 bytes: 0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(b2_big_end&LSB_12_BITS,b2_big_end>>12))
                        MyfileWrite('\n4 bytes: %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (b3,(datetime.utcfromtimestamp(int_value_b3_big_eng))))
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x08:
                    #0x08 type of frame
                    Frame_header = message[:SIZE_2_BYTE]
                    Frame_header_big_end = int(Frame_header[-SIZE_1_BYTE:]+Frame_header[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16) 
                    message = message[SIZE_2_BYTE:]

                    Frame_generation_timestamp = message[:SIZE_4_BYTE]
                    Frame_generation_timestamp_big_end = Frame_generation_timestamp[-SIZE_1_BYTE:]+Frame_generation_timestamp[-SIZE_2_BYTE:-SIZE_1_BYTE]+Frame_generation_timestamp[-SIZE_3_BYTE:-SIZE_2_BYTE]+Frame_generation_timestamp[-SIZE_4_BYTE:-SIZE_3_BYTE] 
                    Frame_generation_timestamp_big_eng_int = int(Frame_generation_timestamp_big_end,base=BASE_16) 
                    message = message[SIZE_4_BYTE:]
                    #
                    Name = message[:SIZE_8_BYTE] 
                    Name_hex = bytes.fromhex(Name)
                    Name_ascii = Name_hex.decode("ASCII")
                    message = message[SIZE_8_BYTE:]

                    Slave_address = message[:SIZE_1_BYTE] 
                    Slave_address_int = int(Slave_address)
                    message = message[SIZE_1_BYTE:]

                    Register_address = message[:SIZE_2_BYTE] 
                    Register_address_int = int(Register_address[-SIZE_1_BYTE:]+Register_address[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16)
                    message = message[SIZE_2_BYTE:]
                    #
                    Function = message[:SIZE_1_BYTE]
                    Funcrion_int = int(Function)
                    message = message[SIZE_1_BYTE:]

                    Register_counter = message[:SIZE_1_BYTE]
                    Register_counter_int = int(Register_counter)
                    message = message[SIZE_1_BYTE:]

                    Signed_flag = message[:SIZE_1_BYTE]
                    Signed_flag_int = int(Signed_flag)
                    message = message[SIZE_1_BYTE:]

                    #
                    Register_value = message[:SIZE_8_BYTE]
                    Register_value_int = int(Register_value[-SIZE_1_BYTE:]+Register_value[-SIZE_2_BYTE:-SIZE_1_BYTE]+Register_value[-SIZE_3_BYTE:-SIZE_2_BYTE]+Register_value[-SIZE_4_BYTE:-SIZE_3_BYTE]\
                        +Register_value[-SIZE_5_BYTE:-SIZE_4_BYTE]+Register_value[-SIZE_6_BYTE:-SIZE_5_BYTE]+Register_value[-SIZE_7_BYTE:-SIZE_6_BYTE]+Register_value[-SIZE_8_BYTE:-SIZE_7_BYTE],base = BASE_16)
                    message = message[SIZE_8_BYTE:]

                    if DEBUG_MODE == '1':
                        print('\n2 bytes:  0x%0.2X: Type of frame,'%(Frame_header_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(Frame_header_big_end>>12)\
                        ,' '*3,'PS:  0x00 – Frame generated on regular base; 0x01 – Frame generated because alarm')
                        print('4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))) 
                        print('8 bytes: Name: %s'%Name_ascii)
                        print('1 bytes: Slave address: %d'%Slave_address_int)
                        print('2 bytes: Register address: %d'%Register_address_int)
                        print('1 bytes: Function: %0.2x'%Funcrion_int)
                        print('1 bytes: Register counter: %0.2x'%Register_counter_int)
                        print('1 bytes: Signed flag: %0.2x'%Signed_flag_int)
                        print('8 bytes: Register value: %d'%Register_value_int)

                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))) 
                        MyfileWrite('\n8 bytes: Name: %s'%Name_ascii)
                        MyfileWrite('\n1 bytes: Slave address: %d'%Slave_address_int)
                        MyfileWrite('\n2 bytes: Register address: %d'%Register_address_int)
                        MyfileWrite('\n1 bytes: Function: %0.2x'%Funcrion_int)
                        MyfileWrite('\n1 bytes: Register counter: %0.2x'%Register_counter_int)
                        MyfileWrite('\n1 bytes: Signed flag: %0.2x'%Signed_flag_int)
                        MyfileWrite('\n8 bytes: Register value: %d'%Register_value_int)
                    else:
                        print('\nModbus frame')

                        if Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x00:
                                print('Frame generated on regular base')
                                MyfileWrite('\n\nFrame generated on regular base')
                        elif Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x01:
                                print('Frame generated because alarm')
                                MyfileWrite('\n\nFrame generated because alarm')

                        print('Time: %s'% (datetime.fromtimestamp(Frame_generation_timestamp_big_eng_int)))
                        print('Name: %s'%Name_ascii)
                        print('Slave address: %d'%Slave_address_int)
                        print('Register address: %d'%Register_address_int)
                        print('Function: %0.2x'%Funcrion_int)
                        print('Register counter: %0.2x'%Register_counter_int)
                        print('Signed flag: %0.2x'%Signed_flag_int)
                        print('Register value: %d'%Register_value_int)

                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))) 
                        MyfileWrite('\n8 bytes: Name: %s'%Name_ascii)
                        MyfileWrite('\n1 bytes: Slave address: %d'%Slave_address_int)
                        MyfileWrite('\n2 bytes: Register address: %d'%Register_address_int)
                        MyfileWrite('\n1 bytes: Function: %0.2x'%Funcrion_int)
                        MyfileWrite('\n1 bytes: Register counter: %0.2x'%Register_counter_int)
                        MyfileWrite('\n1 bytes: Signed flag: %0.2x'%Signed_flag_int)
                        MyfileWrite('\n8 bytes: Register value: %d'%Register_value_int)
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x09:
                    #0x0900 frame type
                    Frame_header = message[:SIZE_2_BYTE]
                    Frame_header_big_end = int(Frame_header[-SIZE_1_BYTE:]+Frame_header[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16) 
                    message = message[SIZE_2_BYTE:]

                    Frame_generation_timestamp = message[:SIZE_4_BYTE]
                    Frame_generation_timestamp_big_end = Frame_generation_timestamp[-SIZE_1_BYTE:]+Frame_generation_timestamp[-SIZE_2_BYTE:-SIZE_1_BYTE]+Frame_generation_timestamp[-SIZE_3_BYTE:-SIZE_2_BYTE]+Frame_generation_timestamp[-SIZE_4_BYTE:-SIZE_3_BYTE] 
                    Frame_generation_timestamp_big_eng_int = int(Frame_generation_timestamp_big_end,base=BASE_16)
                    message = message[SIZE_4_BYTE:] 
                    #
                    Major1 = message[:SIZE_2_BYTE] 
                    Major1_int = int(Major1[-SIZE_1_BYTE:]+Major1[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16)
                    message = message[SIZE_2_BYTE:] 

                    Minor1 = message[:SIZE_2_BYTE] 
                    Minor1_int = int(Minor1[--SIZE_1_BYTE:]+Minor1[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16)
                    message = message[SIZE_2_BYTE:]

                    RSSI1 = message[:SIZE_1_BYTE] 
                    RSSI1_int_big_end = int(RSSI1, base = BASE_16)
                    RSSI1_int_big_end_bin = bin(RSSI1_int_big_end)
                    RSSI1_int_big_end_bin_aint = Bits(RSSI1_int_big_end_bin)
                    message = message[SIZE_1_BYTE:]
                    #
                    Major2 = message[:SIZE_2_BYTE] 
                    Major2_int = int(Major2[-SIZE_1_BYTE:]+Major2[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16)
                    message = message[SIZE_2_BYTE:] 

                    Minor2 = message[:SIZE_2_BYTE] 
                    Minor2_int = int(Minor2[-SIZE_1_BYTE:]+Minor2[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16)
                    message = message[SIZE_2_BYTE:]

                    RSSI2 = message[:SIZE_1_BYTE] 
                    RSSI2_int_big_end = int(RSSI2,base=BASE_16)
                    RSSI2_int_big_end_bin = bin(RSSI2_int_big_end)
                    RSSI2_int_big_end_bin_aint = Bits(RSSI2_int_big_end_bin)
                    message = message[SIZE_1_BYTE:]
                    #
                    Major3 = message[:SIZE_2_BYTE] 
                    Major3_int = int(Major3[-SIZE_1_BYTE:]+Major3[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16)
                    message = message[SIZE_2_BYTE:] 

                    Minor3 = message[:SIZE_2_BYTE] 
                    Minor3_int = int(Minor3[-SIZE_1_BYTE:]+Minor3[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16)
                    message = message[SIZE_2_BYTE:]

                    RSSI3 = message[:SIZE_1_BYTE] 
                    RSSI3_int_big_end = int(RSSI3, base = BASE_16)
                    RSSI3_int_big_end_bin = bin(RSSI3_int_big_end)
                    RSSI3_int_big_end_bin_aint = Bits(RSSI3_int_big_end_bin)
                    message = message[SIZE_1_BYTE:]
                    #
                    Additional_flags = message[:SIZE_1_BYTE]
                    Additional_flags_int = int(Additional_flags,base=BASE_16)
                    Additional_flags_int_bin = bin(Additional_flags_int)
                    message = message[SIZE_1_BYTE:]

                    if DEBUG_MODE == '1':
                        print('\n2 bytes:  0x%0.2X: Type of frame,'%(Frame_header_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(Frame_header_big_end>>12)\
                        ,' '*3,'PS:  0x00 – Frame generated on regular base;')
                        print('4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))) 
                        print('2 bytes:  Major1: %d'%Major1_int)
                        print('2 bytes:  Minor1: %d'%Minor1_int)
                        print('1 byte :   RSSI1: %d'%RSSI1_int_big_end_bin_aint.int)
                        print('2 bytes:  Major2: %d'%Major2_int)
                        print('2 bytes:  Minor2: %d'%Minor2_int)
                        print('1 byte :   RSSI2: %d'%RSSI2_int_big_end_bin_aint.int)
                        print('2 bytes:  Major3: %d'%Major3_int)
                        print('2 bytes:  Minor3: %d'%Minor3_int)
                        print('1 byte :   RSSI3: %d'%RSSI3_int_big_end_bin_aint.int)
                        print('1 byte :  Additional Flags (1 MSB bit): %s\n'%Additional_flags_int_bin[SIZE_1_BYTE:SIZE_1DOT5_BYTE],' '*2,'PS:   Movement flag (based on accelerometer data\n\
                                0 – if device is not in movement; 1 – if device in movement')
                                
                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))) 
                        MyfileWrite('\n2 bytes:  Major1: %d'%Major1_int)
                        MyfileWrite('\n2 bytes:  Minor1: %d'%Minor1_int)
                        MyfileWrite('\n1 byte :   RSSI1: %d'%RSSI1_int_big_end_bin_aint.int)
                        MyfileWrite('\n2 bytes:  Major2: %d'%Major2_int)
                        MyfileWrite('\n2 bytes:  Minor2: %d'%Minor2_int)
                        MyfileWrite('\n1 byte :   RSSI2: %d'%RSSI2_int_big_end_bin_aint.int)
                        MyfileWrite('\n2 bytes:  Major3: %d'%Major3_int)
                        MyfileWrite('\n2 bytes:  Minor3: %d'%Minor3_int)
                        MyfileWrite('\n1 byte :   RSSI3: %d'%RSSI3_int_big_end_bin_aint.int)
                        MyfileWrite('\n1 byte :  Additional Flags (1 MSB bit): %s'%Additional_flags_int_bin[SIZE_1_BYTE:SIZE_1DOT5_BYTE])
                    else:
                        print('\nBluetooth iBeacon geolocation frame')

                        if Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x00:
                                print('Frame generated on regular base')
                                MyfileWrite('\n\nFrame generated on regular base')

                        print('Time: %s (UTC)'% (datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))) 
                        print('Major1: %d'%Major1_int)
                        print('Minor1: %d'%Minor1_int)
                        print('RSSI1: %d'%RSSI1_int_big_end_bin_aint.int)
                        print('Major2: %d'%Major2_int)
                        print('Minor2: %d'%Minor2_int)
                        print('RSSI2: %d'%RSSI2_int_big_end_bin_aint.int)
                        print('Major3: %d'%Major3_int)
                        print('Minor3: %d'%Minor3_int)
                        print('RSSI3: %d'%RSSI3_int_big_end_bin_aint.int)

                        if Additional_flags_int_bin[SIZE_1_BYTE:SIZE_1DOT5_BYTE] == FLAG_VALUE_0:
                                print('Additional Flags: device is not in movement')
                        elif Additional_flags_int_bin[SIZE_1_BYTE:SIZE_1DOT5_BYTE] == FLAG_VALUE_1:
                                print('Additional Flags: device in movement')

                        MyfileWrite('\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))) 
                        MyfileWrite('\n2 bytes:  Major1: %d'%Major1_int)
                        MyfileWrite('\n2 bytes:  Minor1: %d'%Minor1_int)
                        MyfileWrite('\n1 byte :   RSSI1: %d'%RSSI1_int_big_end_bin_aint.int)
                        MyfileWrite('\n2 bytes:  Major2: %d'%Major2_int)
                        MyfileWrite('\n2 bytes:  Minor2: %d'%Minor2_int)
                        MyfileWrite('\n1 byte :   RSSI2: %d'%RSSI2_int_big_end_bin_aint.int)
                        MyfileWrite('\n2 bytes:  Major3: %d'%Major3_int)
                        MyfileWrite('\n2 bytes:  Minor3: %d'%Minor3_int)
                        MyfileWrite('\n1 byte :   RSSI3: %d'%RSSI3_int_big_end_bin_aint.int)
                        MyfileWrite('\n1 byte :  Additional Flags (1 MSB bit): %s'%Additional_flags_int_bin[SIZE_1_BYTE:SIZE_1DOT5_BYTE])
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x10:
                    #0x010 frame type
                    Frame_header = message[:SIZE_2_BYTE]
                    Frame_header_big_end = int(Frame_header[-SIZE_1_BYTE:]+Frame_header[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16) 
                    message = message[SIZE_2_BYTE:]

                    Frame_generation_timestamp = message[:SIZE_4_BYTE]
                    Frame_generation_timestamp_big_end = Frame_generation_timestamp[-SIZE_1_BYTE:]+Frame_generation_timestamp[-SIZE_2_BYTE:-SIZE_1_BYTE]+Frame_generation_timestamp[-SIZE_3_BYTE:-SIZE_2_BYTE]+Frame_generation_timestamp[-SIZE_4_BYTE:-SIZE_3_BYTE] 
                    Frame_generation_timestamp_big_eng_int = int(Frame_generation_timestamp_big_end,base=BASE_16)
                    message = message[SIZE_4_BYTE:] 
                    #
                    Measurement_row_number = message[:SIZE_1_BYTE]
                    Measurement_row_number_int = int(Measurement_row_number,base=BASE_16)
                    message = message[SIZE_1_BYTE:]

                    Command_number_in_row = message[:SIZE_1_BYTE]
                    Command_number_in_row_int = int(Command_number_in_row,base=BASE_16)
                    message = message[SIZE_1_BYTE:]

                    Size_answer = message[:SIZE_1_BYTE]
                    Size_answer_int = int(Size_answer,base=BASE_16)
                    message = message[SIZE_1_BYTE:]

                    Answer = bin(Size_answer_int)[SIZE_1_BYTE:]
                    message = message[len(Answer):]
                    #
                    if DEBUG_MODE == '1':
                        print('\n2 bytes:  0x%0.2X: Type of frame,'%(Frame_header_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(Frame_header_big_end>>12)\
                        ,' '*3,'PS:  0x00 – Frame generated on regular base;')
                        print('4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        print('1 byte :  %d: Measurement row number'%Measurement_row_number_int)
                        print('1 byte :  %d: Command number in row'%Command_number_in_row_int)
                        print('1 byte :  %d: Size answer'%Size_answer_int)
                        print('n bytes:  %s: Answer'%Answer)

                    else:
                        print('\nRS485 frame')

                        if Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x00:
                                print('Frame generated on regular base')
                                MyfileWrite('\n\nFrame generated on regular base')

                        print('Time: %s (UTC)'% (datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))
                        #
                        print('Measurement row number: %d'%Measurement_row_number_int)
                        print('Command number in row: %d'%Command_number_in_row_int)
                        print('Size answer: %d'%Size_answer_int)
                        print('Answer: %s'%Answer)

                        MyfileWrite('\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        MyfileWrite('\n1 byte :  %d: Measurement row number'%Measurement_row_number_int)
                        MyfileWrite('\n1 byte :  %d: Command number in row'%Command_number_in_row_int)
                        MyfileWrite('\n1 byte :  %d: Size answer'%Size_answer_int)
                        MyfileWrite('\nn bytes:  %s: Answer'%Answer)
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x11:
                    #0x11 frame type (SOS)
                    b2 = message[:SIZE_2_BYTE]
                    b2_big_end = int(b2[-SIZE_1_BYTE:]+b2[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16)
                    message = message[SIZE_2_BYTE:]

                    b3 = message[:SIZE_4_BYTE]
                    b3_big_end = b3[-SIZE_1_BYTE:]+b3[-SIZE_2_BYTE:-SIZE_1_BYTE]+b3[-SIZE_3_BYTE:-SIZE_2_BYTE]+b3[-SIZE_4_BYTE:-SIZE_3_BYTE]
                    int_value_b3_big_eng = int(b3_big_end,base=BASE_16)
                    message = message[SIZE_4_BYTE:]

                    if DEBUG_MODE == '1':
                        print('\n2 bytes:  0x%0.2X: Type of frame,'%(b2_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X'%(b2_big_end>>12),'\n     PS:  0x01 – SOS1 event detected, 0x02 – SOS2 event detected')
                        print('4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (b3,(datetime.utcfromtimestamp(int_value_b3_big_eng))))

                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X\n     PS:  0x01 – SOS1 event detected, 0x02 – SOS2 event detected'%(b2_big_end&LSB_12_BITS,b2_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (b3,(datetime.utcfromtimestamp(int_value_b3_big_eng))))
                    else:
                        print('\nSOS frame')

                        if b2_big_end>>TWELVE_DEC == FRAME_GENERATED_0x01:
                                print('SOS1 event detected')
                                MyfileWrite('\n\nSOS1 event detected')
                        elif b2_big_end>>TWELVE_DEC == FRAME_GENERATED_0x02:
                                print('SOS2 event detected')
                                MyfileWrite('\n\nSOS2 event detected')

                        print('Time: %s (UTC)'% (datetime.utcfromtimestamp(int_value_b3_big_eng)))

                        MyfileWrite('\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X\n     PS:  0x01 – SOS1 event detected, 0x02 – SOS2 event detected'%(b2_big_end&LSB_12_BITS,b2_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (b3,(datetime.utcfromtimestamp(int_value_b3_big_eng))))
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x12:
                    #0x012 frame type
                    Frame_header = message[:SIZE_2_BYTE]
                    Frame_header_big_end = int(Frame_header[-SIZE_1_BYTE:]+Frame_header[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16) 
                    message = message[SIZE_2_BYTE:]

                    Frame_generation_timestamp = message[:SIZE_4_BYTE]
                    Frame_generation_timestamp_big_end = Frame_generation_timestamp[-SIZE_1_BYTE:]+Frame_generation_timestamp[-SIZE_2_BYTE:-SIZE_1_BYTE]+Frame_generation_timestamp[-SIZE_3_BYTE:-SIZE_2_BYTE]+Frame_generation_timestamp[-SIZE_4_BYTE:-SIZE_3_BYTE] 
                    Frame_generation_timestamp_big_eng_int = int(Frame_generation_timestamp_big_end,base=BASE_16)
                    message = message[SIZE_4_BYTE:]

                    if DEBUG_MODE == '1': 
                        print('\n2 bytes:  0x%0.2X: Type of frame,'%(Frame_header_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(Frame_header_big_end>>12)\
                        ,' '*3,'PS:  0x01 – Turn event detected;')
                        print('4 bytes:  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))

                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                    else:
                        print('\nTurn detection frame')

                        print('Time: %s (UTC)'% (datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))

                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x13:
                    #0x013 frame type
                    Frame_header = message[:SIZE_2_BYTE]
                    Frame_header_big_end = int(Frame_header[-SIZE_1_BYTE:]+Frame_header[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16) 
                    message = message[SIZE_2_BYTE:]

                    Frame_generation_timestamp = message[:SIZE_4_BYTE]
                    Frame_generation_timestamp_big_end = Frame_generation_timestamp[-SIZE_1_BYTE:]+Frame_generation_timestamp[-SIZE_2_BYTE:-SIZE_1_BYTE]+Frame_generation_timestamp[-SIZE_3_BYTE:-SIZE_2_BYTE]+Frame_generation_timestamp[-SIZE_4_BYTE:-SIZE_3_BYTE] 
                    Frame_generation_timestamp_big_eng_int = int(Frame_generation_timestamp_big_end,base=BASE_16)
                    message = message[SIZE_4_BYTE:] 
                    #
                    Movement_flag = message[:SIZE_1_BYTE]
                    Movement_flag_int = int(Movement_flag,base=BASE_16)
                    message = message[SIZE_1_BYTE:]
                    #
                    if DEBUG_MODE == '1':
                        print('\n2 bytes:  0x%0.2X: Type of frame,'%(Frame_header_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(Frame_header_big_end>>12)\
                        ,' '*3,'PS:  0x00 – Always zero;')
                        print('4 bytes:  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        print('1 byte :  %d: Movement flag'%Movement_flag_int)

                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        MyfileWrite('\n1 byte :  %d: Movement flag'%Movement_flag_int)
                    else:
                        print('\nMovement detection frame')
                        print('Time: %s (UTC)'% (datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))
                        #
                        if Movement_flag_int == MOVEMENT_FLAG_VALUE_0:
                                print('Movement flag: device not in movement')
                        elif Movement_flag_int == MOVEMENT_FLAG_VALUE_1:
                                print('Movement flag: device in movement')

                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        MyfileWrite('\n1 byte :  %d: Movement flag'%Movement_flag_int)
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x14:
                    #0x014 frame type
                    Frame_header = message[:SIZE_2_BYTE]
                    Frame_header_big_end = int(Frame_header[-SIZE_1_BYTE:]+Frame_header[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16) 
                    message = message[SIZE_2_BYTE:]

                    Frame_generation_timestamp = message[:SIZE_4_BYTE]
                    Frame_generation_timestamp_big_end = Frame_generation_timestamp[-SIZE_1_BYTE:]+Frame_generation_timestamp[-SIZE_2_BYTE:-SIZE_1_BYTE]+Frame_generation_timestamp[-SIZE_3_BYTE:-SIZE_2_BYTE]+Frame_generation_timestamp[-SIZE_4_BYTE:-SIZE_3_BYTE] 
                    Frame_generation_timestamp_big_eng_int = int(Frame_generation_timestamp_big_end,base=BASE_16)
                    message = message[SIZE_4_BYTE:] 
                    #
                    ROLL = message[:SIZE_2_BYTE] 
                    ROLL_int = int(ROLL[-SIZE_1_BYTE:]+ROLL[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    PITH = message[:SIZE_2_BYTE] 
                    PITH_int = int(PITH[-SIZE_1_BYTE:]+PITH[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    YAW = message[:SIZE_2_BYTE] 
                    YAW_int = int(YAW[-SIZE_1_BYTE:]+YAW[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]
                    #
                    if DEBUG_MODE == '1':
                        print('\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        print('4 bytes:  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        print('2 bytes:  %d: IMU roll value'%ROLL_int)
                        print('2 bytes:  %d: IMU pith value'%PITH_int)
                        print('2 bytes:  %d: IMU yaw value'%YAW_int)

                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        MyfileWrite('\n2 bytes:  %d: IMU roll value'%ROLL_int)
                        MyfileWrite('\n2 bytes:  %d: IMU pith value'%PITH_int)
                        MyfileWrite('\n2 bytes:  %d: IMU yaw value'%YAW_int)
                    else:
                        print('\nIMU frame')
                        print('Time: %s (UTC)'% (datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))
                        #
                        print('ROLL: %d'%ROLL_int)
                        print('PITH: %d'%PITH_int)
                        print('YAW: %d'%YAW_int)

                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        MyfileWrite('\n2 bytes:  %d: IMU roll value'%ROLL_int)
                        MyfileWrite('\n2 bytes:  %d: IMU pith value'%PITH_int)
                        MyfileWrite('\n2 bytes:  %d: IMU yaw value'%YAW_int)
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x15:
                    #0x015 frame type
                    Frame_header = message[:SIZE_2_BYTE]
                    Frame_header_big_end = int(Frame_header[-SIZE_1_BYTE:]+Frame_header[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16) 
                    message = message[SIZE_2_BYTE:]

                    Frame_generation_timestamp = message[:SIZE_4_BYTE]
                    Frame_generation_timestamp_big_end = Frame_generation_timestamp[-SIZE_1_BYTE:]+Frame_generation_timestamp[-SIZE_2_BYTE:-SIZE_1_BYTE]+Frame_generation_timestamp[-SIZE_3_BYTE:-SIZE_2_BYTE]+Frame_generation_timestamp[-SIZE_4_BYTE:-SIZE_3_BYTE] 
                    Frame_generation_timestamp_big_eng_int = int(Frame_generation_timestamp_big_end,base=BASE_16)
                    message = message[SIZE_4_BYTE:] 
                    #
                    Channel_number = message[:SIZE_1_BYTE]
                    Channel_number_int = int(Channel_number,base=BASE_16)

                    State = message[:SIZE_1_BYTE]
                    State_int = int(State,base=BASE_16)

                    Current_resistance = message[:SIZE_2_BYTE]
                    Current_resistance_int = int(Current_resistance[-SIZE_1_BYTE:]+Current_resistance[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    Min_resistance = message[:SIZE_4_BYTE]
                    Min_resistance_int = int(Min_resistance[-SIZE_1_BYTE:]+Min_resistance[-SIZE_2_BYTE:-SIZE_1_BYTE]+Min_resistance[-SIZE_3_BYTE:-SIZE_2_BYTE]+Min_resistance[-SIZE_4_BYTE:-SIZE_3_BYTE],base=BASE_16)
                    message = message[SIZE_4_BYTE:]

                    Max_resistance = message[:SIZE_4_BYTE]
                    Max_resistance_int = int(Max_resistance[-SIZE_1_BYTE:]+Max_resistance[-SIZE_2_BYTE:-SIZE_1_BYTE]+Max_resistance[-SIZE_3_BYTE:-SIZE_2_BYTE]+Max_resistance[-SIZE_4_BYTE:-SIZE_3_BYTE],base=BASE_16)
                    message = message[SIZE_4_BYTE:]

                    Middle_resistance = message[:SIZE_4_BYTE]
                    Middle_resistance_int = int(Middle_resistance[-SIZE_1_BYTE:]+Middle_resistance[-SIZE_2_BYTE:-SIZE_1_BYTE]+Middle_resistance[-SIZE_3_BYTE:-SIZE_2_BYTE]+Middle_resistance[-SIZE_4_BYTE:-SIZE_3_BYTE],base=BASE_16)
                    message = message[SIZE_4_BYTE:]

                    Current_conduct_resistance = message[:SIZE_4_BYTE]
                    Current_conduct_resistance_int = int(Current_conduct_resistance[-SIZE_1_BYTE:]+Current_conduct_resistance[-SIZE_2_BYTE:-SIZE_1_BYTE]+Current_conduct_resistance[-SIZE_3_BYTE:-SIZE_2_BYTE]+Current_conduct_resistance[-SIZE_4_BYTE:-SIZE_3_BYTE],base=BASE_16)
                    message = message[SIZE_4_BYTE:]
                    #
                    if DEBUG_MODE == '1':
                        print('\n2 bytes:  0x%0.2X: Type of frame,'%(Frame_header_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(Frame_header_big_end>>12)\
                        ,' '*3,'PS:  0x00 – Always zero;')
                        print('4 bytes:  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        print('1 byte :  %d: Channel number'%Channel_number_int)
                        print('1 byte :  0x%0.2x: State'%State_int)
                        print('2 bytes:  %d: Current resistance'%Current_resistance_int)
                        print('4 bytes:  0x%0.2x: Min resistance'%Min_resistance_int)
                        print('4 bytes:  0x%0.2x: Max resistance'%Max_resistance_int)
                        print('4 bytes:  0x%0.2x: Middle resistance'%Middle_resistance_int)
                        print('4 bytes:  0x%0.2x: Current conduct resistance'%Current_conduct_resistance_int)

                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        MyfileWrite('\n1 byte :  %d: Channel number'%Channel_number_int)
                        MyfileWrite('\n1 byte :  0x%0.2x: State'%State_int)
                        MyfileWrite('\n2 bytes:  %d: Current resistance'%Current_resistance_int)
                        MyfileWrite('\n4 bytes:  0x%0.2x: Min resistance'%Min_resistance_int)
                        MyfileWrite('\n4 bytes:  0x%0.2x: Max resistance'%Max_resistance_int)
                        MyfileWrite('\n4 bytes:  0x%0.2x: Middle resistance'%Middle_resistance_int)
                        MyfileWrite('\n4 bytes:  0x%0.2x: Current conduct resistance'%Current_conduct_resistance_int)
                    else:
                        print('\nODK frame')

                        if Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x00:
                                print('Frame generated on regular base')
                                MyfileWrite('\n\nFrame generated on regular base')
                        elif Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x01:
                                print('Frame generated because alarm')
                                MyfileWrite('\n\nFrame generated because alarm')

                        print('Time: %s (UTC)' %(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))
                        #
                        print('Channel number: %d'%Channel_number_int)
                        print('State: 0x%0.2x'%State_int)
                        print('Current resistance: %d'%Current_resistance_int)
                        print('Min resistance: 0x%0.2x'%Min_resistance_int)
                        print('Max resistance: 0x%0.2x'%Max_resistance_int)
                        print('Middle resistance: 0x%0.2x'%Middle_resistance_int)
                        print('Current conduct resistance: 0x%0.2x'%Current_conduct_resistance_int)

                        MyfileWrite('\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        MyfileWrite('\n1 byte :  %d: Channel number'%Channel_number_int)

                        if State_int == STATE_VALUE_0x00:
                                print('1 byte : State: Normal1')
                                MyfileWrite('\n1 byte : State: Normal1')
                        elif State_int == STATE_VALUE_0x01:
                                print('1 byte : State: Normal2')
                                MyfileWrite('\n1 byte : State: Normal2')
                        elif State_int == STATE_VALUE_0x02:
                                print('1 byte : State: Normal3')
                                MyfileWrite('\n1 byte : State: Normal3')
                        elif State_int == STATE_VALUE_0x03:
                                print('1 byte : State: Normal4')
                                MyfileWrite('\n1 byte : State: Normal4')
                        elif State_int == STATE_VALUE_0x04:
                                print('1 byte : State: Normal5')
                                MyfileWrite('\n1 byte : State: Normal5')
                        elif State_int == STATE_VALUE_0x05:
                                print('1 byte : State: Wet')
                                MyfileWrite('\n1 byte : State: Wet')
                        elif State_int == STATE_VALUE_0x06:
                                print('1 byte : State: Break')
                                MyfileWrite('\n1 byte : State: Break')
                        elif State_int == STATE_VALUE_0x07:
                                print('1 byte : State: Wet Break')
                                MyfileWrite('\n1 byte : State: Wet Break')
                        elif State_int == STATE_VALUE_0x08:
                                print('1 byte : State: Unknown')
                                MyfileWrite('\n1 byte : State: Unknown')

                        MyfileWrite('\n2 bytes:  %d: Current resistance'%Current_resistance_int)
                        MyfileWrite('\n4 bytes:  0x%0.2x: Min resistance'%Min_resistance_int)
                        MyfileWrite('\n4 bytes:  0x%0.2x: Max resistance'%Max_resistance_int)
                        MyfileWrite('\n4 bytes:  0x%0.2x: Middle resistance'%Middle_resistance_int)
                        MyfileWrite('\n4 bytes:  0x%0.2x: Current conduct resistance'%Current_conduct_resistance_int)
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x16:
                    #0x016 frame type
                    print('\n   !MBUS!   ')
                    MyfileWrite('\n\n   !MBUS!   ')
                    print("Error parsing: %s" %message)
                    MyfileWrite("\n\nError parsing: %s" %message)
                    break
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x17:
                    #0x017 frame type
                    Frame_header = message[:SIZE_2_BYTE]
                    Frame_header_big_end = int(Frame_header[-SIZE_1_BYTE:]+Frame_header[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16) 
                    message = message[SIZE_2_BYTE:]

                    Frame_generation_timestamp = message[:SIZE_4_BYTE]
                    Frame_generation_timestamp_big_end = Frame_generation_timestamp[-SIZE_1_BYTE:]+Frame_generation_timestamp[-SIZE_2_BYTE:-SIZE_1_BYTE]+Frame_generation_timestamp[-SIZE_3_BYTE:-SIZE_2_BYTE]+Frame_generation_timestamp[-SIZE_4_BYTE:-SIZE_3_BYTE] 
                    Frame_generation_timestamp_big_eng_int = int(Frame_generation_timestamp_big_end,base=BASE_16)
                    message = message[SIZE_4_BYTE:] 
                    #
                    ICCID = message[:SIZE_20_BYTE]
                    ICCID_BIG_END =  ICCID[-SIZE_1_BYTE:]+ICCID[-SIZE_2_BYTE:-SIZE_1_BYTE]+ICCID[-SIZE_3_BYTE:-SIZE_2_BYTE]+ICCID[-SIZE_4_BYTE:-SIZE_3_BYTE]\
                        +ICCID[-SIZE_5_BYTE:-SIZE_4_BYTE]+ICCID[-SIZE_6_BYTE:-SIZE_5_BYTE]+ICCID[-SIZE_7_BYTE:-SIZE_6_BYTE]+ICCID[-SIZE_8_BYTE:-SIZE_7_BYTE]\
                                +ICCID[-SIZE_9_BYTE:-SIZE_8_BYTE]+ICCID[-SIZE_10_BYTE:-SIZE_9_BYTE]+ICCID[-SIZE_11_BYTE:-SIZE_10_BYTE]+ICCID[-SIZE_12_BYTE:-SIZE_11_BYTE]\
                                        +ICCID[-SIZE_13_BYTE:-SIZE_12_BYTE]+ICCID[-SIZE_14_BYTE:-SIZE_13_BYTE]+ICCID[-SIZE_15_BYTE:-SIZE_14_BYTE]+ICCID[-SIZE_16_BYTE:-SIZE_15_BYTE]\
                                                +ICCID[-SIZE_17_BYTE:-SIZE_16_BYTE]+ICCID[-SIZE_18_BYTE:-SIZE_17_BYTE]+ICCID[-SIZE_19_BYTE:-SIZE_18_BYTE]+ICCID[-SIZE_20_BYTE:-SIZE_19_BYTE]
                    message = message[SIZE_20_BYTE:]

                    RSSI = message[:SIZE_2_BYTE]
                    RSSI_BIG_END = RSSI[-SIZE_1_BYTE:]+RSSI[-SIZE_2_BYTE:-SIZE_1_BYTE]
                    message = message[SIZE_2_BYTE:]

                    IMEI = message[:SIZE_15_BYTE]
                    IMEI_BIG_END = IMEI[-SIZE_1_BYTE:]+IMEI[-SIZE_2_BYTE:-SIZE_1_BYTE]+IMEI[-SIZE_3_BYTE:-SIZE_2_BYTE]+IMEI[-SIZE_4_BYTE:-SIZE_3_BYTE]\
                        +IMEI[-SIZE_5_BYTE:-SIZE_4_BYTE]+IMEI[-SIZE_6_BYTE:-SIZE_5_BYTE]+IMEI[-SIZE_7_BYTE:-SIZE_6_BYTE]+IMEI[-SIZE_8_BYTE:-SIZE_7_BYTE]\
                                +IMEI[-SIZE_9_BYTE:-SIZE_8_BYTE]+IMEI[-SIZE_10_BYTE:-SIZE_9_BYTE]+IMEI[-SIZE_11_BYTE:-SIZE_10_BYTE]+IMEI[-SIZE_12_BYTE:-SIZE_11_BYTE]\
                                        +IMEI[-SIZE_13_BYTE:-SIZE_12_BYTE]+IMEI[-SIZE_14_BYTE:-SIZE_13_BYTE]+IMEI[-SIZE_15_BYTE:-SIZE_14_BYTE]
                    message = message[SIZE_15_BYTE:]

                    if DEBUG_MODE == '1':
                        print('\n2 bytes  :  0x%0.2X: Type of frame,'%(Frame_header_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(Frame_header_big_end>>12)\
                        ,' '*3,'PS  :  0x00 – Always zero;')
                        print('4 bytes  :  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        print('20 bytes :  %s: ICCID'%(int(ICCID_BIG_END,base = BASE_16)))
                        print('2  byte  :  %s: RSSI'%(int(RSSI_BIG_END,base = BASE_16)))
                        print('15 bytes :  %s: IMEI'%(int(IMEI_BIG_END,base = BASE_16)))

                        MyfileWrite('\n\n2 bytes  :  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes  :  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        MyfileWrite('\n20 bytes :  %s: ICCID'%(int(ICCID_BIG_END,base = BASE_16)))
                        MyfileWrite('\n2  byte  :  %s: RSSI'%(int(RSSI_BIG_END,base = BASE_16)))
                        MyfileWrite('\n15 bytes :  %s: IMEI'%(int(IMEI_BIG_END,base = BASE_16)))
                    else:
                        print('\nModem State frame')

                        if Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x00:
                                print('Frame generated on regular base')
                                MyfileWrite('\n\nFrame generated on regular base')

                        print('Time: %s (UTC)'% (datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))
                        #
                        print('ICCID: %s'%(int(ICCID_BIG_END,base = BASE_16)))
                        print('RSSI: %s'%(int(RSSI_BIG_END,base = BASE_16)))
                        print('IMEI: %s'%(int(IMEI_BIG_END,base = BASE_16)))

                        MyfileWrite('\n2 bytes  :  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes  :  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        MyfileWrite('\n20 bytes :  %s: ICCID'%(int(ICCID_BIG_END,base = BASE_16)))
                        MyfileWrite('\n2  byte  :  %s: RSSI'%(int(RSSI_BIG_END,base = BASE_16)))
                        MyfileWrite('\n15 bytes :  %s: IMEI'%(int(IMEI_BIG_END,base = BASE_16)))
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x18:
                    #0x018 frame type
                    Frame_header = message[:SIZE_2_BYTE]
                    Frame_header_big_end = int(Frame_header[-SIZE_1_BYTE:]+Frame_header[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16) 
                    message = message[SIZE_2_BYTE:]

                    Frame_generation_timestamp = message[:SIZE_4_BYTE]
                    Frame_generation_timestamp_big_end = Frame_generation_timestamp[-SIZE_1_BYTE:]+Frame_generation_timestamp[-SIZE_2_BYTE:-SIZE_1_BYTE]+Frame_generation_timestamp[-SIZE_3_BYTE:-SIZE_2_BYTE]+Frame_generation_timestamp[-SIZE_4_BYTE:-SIZE_3_BYTE] 
                    Frame_generation_timestamp_big_eng_int = int(Frame_generation_timestamp_big_end,base=BASE_16) 
                    message = message[SIZE_4_BYTE:]
                    #
                    Humidity = message[:SIZE_2_BYTE]
                    Humidity_int = int(Humidity[-SIZE_1_BYTE:]+Humidity[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16)
                    message = message[SIZE_2_BYTE:]

                    if DEBUG_MODE == '1':
                        #
                        print('\n2 bytes  :  0x%0.2X: Type of frame,'%(Frame_header_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(Frame_header_big_end>>12)\
                        ,' '*3,'PS  :  0x00 – Always zero;')
                        print('4 bytes  :  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        print('2  byte  :  %0.1f: Humidity'%(Humidity_int/10))

                        MyfileWrite('\n\n2 bytes  :  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes  :  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        MyfileWrite('\n2  byte  :  %0.1f: Humidity'%(Humidity_int/10))

                    else:
                        print('\nHumidity frame')
                        
                        if Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x00:
                                print('Frame generated on regular base')
                                MyfileWrite('\n\nFrame generated on regular base')

                        print('Time: %s (UTC)'% (datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))
                        #
                        print('Humidity: %0.1f'%(Humidity_int/10))

                        MyfileWrite('\n2 bytes  :  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes  :  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        MyfileWrite('\n2  byte  :  %0.1f: Humidity'%(Humidity_int/10))
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x19:
                    #0x019 frame type
                    Frame_header = message[:SIZE_2_BYTE]
                    Frame_header_big_end = int(Frame_header[-SIZE_1_BYTE:]+Frame_header[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16) 
                    message = message[SIZE_2_BYTE:]

                    Frame_generation_timestamp = message[:SIZE_4_BYTE]
                    Frame_generation_timestamp_big_end = Frame_generation_timestamp[-SIZE_1_BYTE:]+Frame_generation_timestamp[-SIZE_2_BYTE:-SIZE_1_BYTE]+Frame_generation_timestamp[-SIZE_3_BYTE:-SIZE_2_BYTE]+Frame_generation_timestamp[-SIZE_4_BYTE:-SIZE_3_BYTE] 
                    Frame_generation_timestamp_big_eng_int = int(Frame_generation_timestamp_big_end,base=BASE_16) 
                    message = message[SIZE_4_BYTE:]
                    #
                    Illuminance = message[:SIZE_2_BYTE] 
                    Illuminance_int = int(Illuminance[-SIZE_1_BYTE:]+Illuminance[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16)
                    message = message[SIZE_2_BYTE:]

                    if DEBUG_MODE == '1':
                        #
                        print('\n2 bytes  :  0x%0.2X: Type of frame,'%(Frame_header_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(Frame_header_big_end>>12)\
                        ,' '*3,'PS  :  0x00 – Always zero;')
                        print('4 bytes  :  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        print('2  byte  :  %d: Illuminance in Lux'%(Illuminance_int))

                        MyfileWrite('\n\n2 bytes  :  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes  :  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        MyfileWrite('\n2  byte  :  %d: Illuminance in Lux'%(Illuminance_int))
                    else:
                        print('\nIlluminance frame')

                        if Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x00:
                                print('Frame generated on regular base')
                                MyfileWrite('\n\nFrame generated on regular base')

                        print('Time: %s (UTC)'% (datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))
                        #
                        print('Illuminance: %d'%(Illuminance_int))

                        MyfileWrite('\n2 bytes  :  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes  :  %s: Frame generation timestamp (Hex) –> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        MyfileWrite('\n2  byte  :  %d: Illuminance in Lux'%(Illuminance_int))
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x0A:
                    #0x0A00 frame type
                    Frame_header = message[:SIZE_2_BYTE]
                    Frame_header_big_end = int(Frame_header[-SIZE_1_BYTE:]+Frame_header[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16) 
                    message = message[SIZE_2_BYTE:]

                    Frame_generation_timestamp = message[:SIZE_4_BYTE]
                    Frame_generation_timestamp_big_end = Frame_generation_timestamp[-SIZE_1_BYTE:]+Frame_generation_timestamp[-SIZE_2_BYTE:-SIZE_1_BYTE]+Frame_generation_timestamp[-SIZE_3_BYTE:-SIZE_2_BYTE]+Frame_generation_timestamp[-SIZE_4_BYTE:-SIZE_3_BYTE] 
                    Frame_generation_timestamp_big_eng_int = int(Frame_generation_timestamp_big_end,base=BASE_16) 
                    message = message[SIZE_4_BYTE:]
                    #
                    Current = message[:SIZE_4_BYTE]
                    Current_big_end = Current[-SIZE_1_BYTE:]+Current[-SIZE_2_BYTE:-SIZE_1_BYTE]+Current[-SIZE_3_BYTE:-SIZE_2_BYTE]+Current[-SIZE_4_BYTE:-SIZE_3_BYTE]
                    message = message[SIZE_4_BYTE:]

                    if DEBUG_MODE == '1':
                        print('\n2 bytes:  0x%0.2X: Type of frame,'%(Frame_header_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(Frame_header_big_end>>12)\
                        ,' '*3,'PS:  0x00 – Frame generated on regular base; 0x01 – Frame generated because alarm')
                        print('4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))) 
                        print('4 bytes:  0x%0.2X: Current value in milliamperes'% (Current_big_end))

                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))) 
                        MyfileWrite('\n4 bytes:  0x%0.2X: Current value in milliamperes'% (Current_big_end))
                    else:
                        print('\n4-20 mA frame')

                        if Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x00:
                                print('Frame generated on regular base')
                                MyfileWrite('\n\nFrame generated on regular base')
                        elif Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x01:
                                print('Frame generated because alarm')
                                MyfileWrite('\n\nFrame generated because alarm')

                        print('Time: %s (UTC)'% (datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))) 
                        print('Current: 0x%0.2X'% (Current_big_end))

                        MyfileWrite('\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))) 
                        MyfileWrite('\n4 bytes:  0x%0.2X: Current value in milliamperes'% (Current_big_end))
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x0B:
                    #0x0B00 frame type
                    Frame_header = message[:SIZE_2_BYTE]
                    Frame_header_big_end = int(Frame_header[-SIZE_1_BYTE:]+Frame_header[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16) 
                    message = message[SIZE_2_BYTE:]

                    Frame_generation_timestamp = message[:SIZE_4_BYTE]
                    Frame_generation_timestamp_big_end = Frame_generation_timestamp[-SIZE_1_BYTE:]+Frame_generation_timestamp[-SIZE_2_BYTE:-SIZE_1_BYTE]+Frame_generation_timestamp[-SIZE_3_BYTE:-SIZE_2_BYTE]+Frame_generation_timestamp[-SIZE_4_BYTE:-SIZE_3_BYTE] 
                    Frame_generation_timestamp_big_eng_int = int(Frame_generation_timestamp_big_end,base=BASE_16) 
                    message = message[SIZE_4_BYTE:]
                    #
                    Pin_number = message[:SIZE_1_BYTE] 
                    Pin_number_int = int(Pin_number,base=BASE_16)
                    message = message[SIZE_1_BYTE:]

                    Pin_state = message[:SIZE_0DOT1_BYTE]
                    Pin_state_int = int(Pin_state,base=BASE_16)
                    Pin_state_int_bin = bin(Pin_state_int)
                    message = message[SIZE_0DOT1_BYTE:]

                    if DEBUG_MODE == '1':
                        print('\n2 bytes:  0x%0.2X: Type of frame,'%(Frame_header_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(Frame_header_big_end>>12)\
                        ,' '*3,'PS:  0x00 – Frame generated on regular base; 0x01 – Frame generated because alarm')
                        print('4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        print('1 byte :  0x%0.2X: Pin number'%Pin_number_int)
                        print('1 byte :  0x%0.2X: Pin state'%Pin_state_int_bin[SIZE_0_BYTE:SIZE_0DOT1_BYTE])

                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        MyfileWrite('\n1 byte :  0x%0.2X: Pin number'%Pin_number_int)
                        MyfileWrite('\n1 byte :  0x%0.2X: Pin state'%Pin_state_int_bin[SIZE_0_BYTE:SIZE_0DOT1_BYTE])
                    else:
                        print('\nDigital input frame')

                        if Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x00:
                                print('Frame generated on regular base')
                                MyfileWrite('\n\nFrame generated on regular base')
                        elif Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x01:
                                print('Frame generated because alarm')
                                MyfileWrite('\n\nFrame generated because alarm')

                        print('Time: %s (UTC)'% (datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))
                        print('Pin number: %d'%Pin_number_int)

                        if Pin_state_int_bin[SIZE_0_BYTE:SIZE_0DOT1_BYTE] == PIN_STATE_VALUE_0x00:
                                print('Pin state: Low state')
                        elif Pin_state_int_bin[SIZE_0_BYTE:SIZE_0DOT1_BYTE] == PIN_STATE_VALUE_0x01:
                                print('Pin state: High state')

                        MyfileWrite('\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        MyfileWrite('\n1 byte :  0x%0.2X: Pin number'%Pin_number_int)
                        MyfileWrite('\n1 byte :  0x%0.2X: Pin state'%Pin_state_int_bin[SIZE_0_BYTE:SIZE_0DOT1_BYTE])
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x0C:
                    #0x0C00 frame type
                    Frame_header = message[:SIZE_2_BYTE]
                    Frame_header_big_end = int(Frame_header[-SIZE_1_BYTE:]+Frame_header[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16) 
                    message = message[SIZE_2_BYTE:]

                    Frame_generation_timestamp = message[:SIZE_4_BYTE]
                    Frame_generation_timestamp_big_end = Frame_generation_timestamp[-SIZE_1_BYTE:]+Frame_generation_timestamp[-SIZE_2_BYTE:-SIZE_1_BYTE]+Frame_generation_timestamp[-SIZE_3_BYTE:-SIZE_2_BYTE]+Frame_generation_timestamp[-SIZE_4_BYTE:-SIZE_3_BYTE] 
                    Frame_generation_timestamp_big_eng_int = int(Frame_generation_timestamp_big_end,base=BASE_16) 
                    message = message[SIZE_4_BYTE:]
                    #s
                    Pin_number = message[:SIZE_1_BYTE] 
                    Pin_number_int = int(Pin_number,base=BASE_16)
                    message = message[SIZE_1_BYTE:]

                    Voltage = message[:SIZE_4_BYTE]
                    Voltage_int = int(Voltage[-SIZE_1_BYTE:]+Voltage[-SIZE_2_BYTE:-SIZE_1_BYTE]+Voltage[-SIZE_3_BYTE:-SIZE_2_BYTE]+Voltage[-SIZE_4_BYTE:-SIZE_3_BYTE],base=BASE_16)
                    message = message[SIZE_4_BYTE:]

                    Status = message[:SIZE_1_BYTE]
                    message = message[SIZE_1_BYTE:]
                    #
                    if DEBUG_MODE == '1':
                        print('\n2 bytes:  0x%0.2X - Type of frame,'%(Frame_header_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(Frame_header_big_end>>TWELVE_DEC)\
                        ,' '*3,'PS:  0x00 – Frame generated on regular base; 0x01 – Frame generated because alarm')
                        print('4 bytes:  %s - Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))

                        print('1 byte :  0x%0.2X - Pin number'%Pin_number_int)
                        print('4 bytes:  0x%0.2X - Pin state'%Voltage_int)
                        print('1 byte :  %s - Status'%Status)

                        MyfileWrite('\n\n2 bytes:  0x%0.2X - Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>TWELVE_DEC))
                        MyfileWrite('\n4 bytes:  %s - Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        MyfileWrite('\n1 byte :  0x%0.2X - Pin number'%Pin_number_int)
                        MyfileWrite('\n4 bytes:  %d - Pin state'%Voltage_int)
                        MyfileWrite('\n1 byte :  %s - Status'%Status)
                    else:
                        print('\nAnalog input frame')

                        if Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x00:
                                print('Frame generated on regular base')
                                MyfileWrite('\n\nFrame generated on regular base')
                        elif Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x01:
                                print('Frame generated because alarm')
                                MyfileWrite('\n\nFrame generated because alarm')

                        print('Time: %s (UTC)'%(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))
                        print('Pin number: %d'%Pin_number_int)
                        print('Voltage: %d millivolts'%Voltage_int)

                        if Status == STATUS_VALUE_00:
                                print('Status: status ok')
                        elif Status == STATUS_VALUE_01:
                                print('Status: overvoltage detected')
                        elif Status == STATUS_VALUE_02:
                                print('Status: no sensor detected')

                        MyfileWrite('\n2 bytes:  0x%0.2X - Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>TWELVE_DEC))
                        MyfileWrite('\n4 bytes:  %s - Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        MyfileWrite('\n1 byte :  0x%0.2X - Pin number'%Pin_number_int)
                        MyfileWrite('\n4 bytes:  %d - Pin state'%Voltage_int)
                        MyfileWrite('\n1 byte :  %s - Status'%Status)
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x0D:
                    #0x0D00 frame type
                    Frame_header = message[:SIZE_2_BYTE]
                    Frame_header_big_end = int(Frame_header[-SIZE_1_BYTE:]+Frame_header[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16) 
                    message = message[SIZE_2_BYTE:]

                    Frame_generation_timestamp = message[:SIZE_4_BYTE]
                    Frame_generation_timestamp_big_end = Frame_generation_timestamp[-SIZE_1_BYTE:]+Frame_generation_timestamp[-SIZE_2_BYTE:-SIZE_1_BYTE]+Frame_generation_timestamp[-SIZE_3_BYTE:-SIZE_2_BYTE]+Frame_generation_timestamp[-SIZE_4_BYTE:-SIZE_3_BYTE] 
                    Frame_generation_timestamp_big_eng_int = int(Frame_generation_timestamp_big_end,base=BASE_16) 
                    message = message[SIZE_4_BYTE:]
                    #
                    Pin_number = message[:SIZE_1_BYTE] 
                    Pin_number_int = int(Pin_number,base=BASE_16)
                    message = message[SIZE_1_BYTE:]

                    Counter_value = message[:SIZE_4_BYTE]
                    Counter_value_int = int(Counter_value[-SIZE_1_BYTE:]+Counter_value[-SIZE_2_BYTE:-SIZE_1_BYTE]+Counter_value[-SIZE_3_BYTE:-SIZE_2_BYTE]+Counter_value[-SIZE_4_BYTE:-SIZE_3_BYTE],base=BASE_16)
                    message = message[SIZE_4_BYTE:]

                    if DEBUG_MODE == '1':
                        #
                        print('\n2 bytes:  0x%0.2X: Type of frame,'%(Frame_header_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(Frame_header_big_end>>12)\
                        ,' '*3,'PS:  0x00 – Frame generated on regular base;')
                        print('4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))

                        print('1 byte :  0x%0.2X: Pin number'%Pin_number_int)
                        print('4 bytes:  0x%0.2X: Counter value'%Counter_value_int)

                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        MyfileWrite('\n1 byte :  0x%0.2X: Pin number'%Pin_number_int)
                        MyfileWrite('\n4 bytes:  0x%0.2X: Counter value'%Counter_value_int)
                    else:
                        print('\nPulse counter frame')

                        if Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x00:
                                print('Frame generated on regular base')
                                MyfileWrite('\n\nFrame generated on regular base')

                        print('Time: %s (UTC)'% (datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))
                        print('Pin number: %d'%Pin_number_int)
                        print('Counter value: 0x%0.2X'%Counter_value_int)

                        MyfileWrite('\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        MyfileWrite('\n1 byte :  0x%0.2X: Pin number'%Pin_number_int)
                        MyfileWrite('\n4 bytes:  0x%0.2X: Counter value'%Counter_value_int)
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x0E:
                    #0x0E00 frame type
                    Frame_header = message[:SIZE_2_BYTE]
                    Frame_header_big_end = int(Frame_header[-SIZE_1_BYTE:]+Frame_header[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16) 
                    message = message[SIZE_2_BYTE:]

                    Frame_generation_timestamp = message[:SIZE_4_BYTE]
                    Frame_generation_timestamp_big_end = Frame_generation_timestamp[-SIZE_1_BYTE:]+Frame_generation_timestamp[-SIZE_2_BYTE:-SIZE_1_BYTE]+Frame_generation_timestamp[-SIZE_3_BYTE:-SIZE_2_BYTE]+Frame_generation_timestamp[-SIZE_4_BYTE:-SIZE_3_BYTE] 
                    Frame_generation_timestamp_big_eng_int = int(Frame_generation_timestamp_big_end,base=BASE_16) 
                    message = message[SIZE_4_BYTE:]
                    #
                    MCC1 = message[:SIZE_2_BYTE]
                    MCC1_int = int(MCC1[-SIZE_1_BYTE:]+MCC1[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    MNC1 = message[:SIZE_2_BYTE]
                    MNC1_int = int(MNC1[-SIZE_1_BYTE:]+MNC1[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    LAC1 = message[:SIZE_2_BYTE]
                    LAC1_int = int(LAC1[-SIZE_1_BYTE:]+LAC1[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    CELLID1 = message[:SIZE_2_BYTE]
                    CELLID1_int = int(CELLID1[-SIZE_1_BYTE:]+CELLID1[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    Power1 = message[:SIZE_2_BYTE]
                    Power1_int = int(Power1[-SIZE_1_BYTE:]+Power1[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]
                    #
                    MCC2 = message[:SIZE_2_BYTE]
                    MCC2_int = int(MCC2[-SIZE_1_BYTE:]+MCC2[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    MNC2 = message[:SIZE_2_BYTE]
                    MNC2_int = int(MNC2[-SIZE_1_BYTE:]+MNC2[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    LAC2 = message[:SIZE_2_BYTE]
                    LAC2_int = int(LAC2[-SIZE_1_BYTE:]+LAC2[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    CELLID2 = message[:SIZE_2_BYTE]
                    CELLID2_int = int(CELLID2[-SIZE_1_BYTE:]+CELLID2[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    Power2 = message[:SIZE_2_BYTE]
                    Power2_int = int(Power2[-SIZE_1_BYTE:]+Power2[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]
                    #
                    MCC3 = message[:SIZE_2_BYTE]
                    MCC3_int = int(MCC3[-SIZE_1_BYTE:]+MCC3[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    MNC3 = message[:SIZE_2_BYTE]
                    MNC3_int = int(MNC3[-SIZE_1_BYTE:]+MNC3[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    LAC3 = message[:SIZE_2_BYTE]
                    LAC3_int = int(LAC3[-SIZE_1_BYTE:]+LAC3[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    CELLID3 = message[:SIZE_2_BYTE]
                    CELLID3_int = int(CELLID3[-SIZE_1_BYTE:]+CELLID3[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    Power3 = message[:SIZE_2_BYTE]
                    Power3_int = int(Power3[-SIZE_1_BYTE:]+Power3[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)
                    message = message[SIZE_2_BYTE:]

                    if DEBUG_MODE == '1':
                        #
                        print('\n2 bytes:  0x%0.2X: Type of frame,'%(Frame_header_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(Frame_header_big_end>>12)\
                        ,' '*3,'PS:  0x00 – Frame generated on regular base;')
                        print('4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        print('2 bytes:  %d: MCC1'%MCC1_int)
                        print('2 bytes:  %d: MNC1'%MNC1_int)
                        print('2 bytes:  %d: LAC1'%LAC1_int)
                        print('2 bytes:  %d: CELLID1'%CELLID1_int)
                        print('2 bytes:  %d: Power1'%Power1_int)
                        #
                        print('2 bytes:  %d: MCC2'%MCC2_int)
                        print('2 bytes:  %d: MNC2'%MNC2_int)
                        print('2 bytes:  %d: LAC2'%LAC2_int)
                        print('2 bytes:  %d: CELLID2'%CELLID2_int)
                        print('2 bytes:  %d: Power2'%Power2_int)
                        #
                        print('2 bytes:  %d: MCC3'%MCC3_int)
                        print('2 bytes:  %d: MNC3'%MNC3_int)
                        print('2 bytes:  %d: LAC3'%LAC3_int)
                        print('2 bytes:  %d: CELLID3'%CELLID3_int)
                        print('2 bytes:  %d: Power3'%Power3_int)

                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        MyfileWrite('\n2 bytes:  %d: MCC1'%MCC1_int)
                        MyfileWrite('\n2 bytes:  %d: MNC1'%MNC1_int)
                        MyfileWrite('\n2 bytes:  %d: LAC1'%LAC1_int)
                        MyfileWrite('\n2 bytes:  %d: CELLID1'%CELLID1_int)
                        MyfileWrite('\n2 bytes:  %d: Power1'%Power1_int)
                        #
                        MyfileWrite('\n2 bytes:  %d: MCC2'%MCC2_int)
                        MyfileWrite('\n2 bytes:  %d: MNC2'%MNC2_int)
                        MyfileWrite('\n2 bytes:  %d: LAC2'%LAC2_int)
                        MyfileWrite('\n2 bytes:  %d: CELLID2'%CELLID2_int)
                        MyfileWrite('\n2 bytes:  %d - Power2'%Power2_int)
                        #
                        MyfileWrite('\n2 bytes:  %d: MCC3'%MCC3_int)
                        MyfileWrite('\n2 bytes:  %d: MNC3'%MNC3_int)
                        MyfileWrite('\n2 bytes:  %d: LAC3'%LAC3_int)
                        MyfileWrite('\n2 bytes:  %d: CELLID3'%CELLID3_int)
                        MyfileWrite('\n2 bytes:  %d: Power3'%Power3_int)
                    else:
                        print('\nLBS geolocation frame')

                        if Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x00:
                                print('Frame generated on regular base')
                                MyfileWrite('\n\nFrame generated on regular base')

                        print('Time: %s (UTC)'% (datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))
                        #
                        print('MCC1: %d'%MCC1_int)
                        print('MNC1: %d'%MNC1_int)
                        print('LAC1: %d'%LAC1_int)
                        print('CELLID1: %d'%CELLID1_int)
                        print('Power1: %d'%Power1_int)
                        #
                        print('MCC2: %d'%MCC2_int)
                        print('MNC2: %d'%MNC2_int)
                        print('LAC2: %d'%LAC2_int)
                        print('CELLID2: %d'%CELLID2_int)
                        print('Power2: %d'%Power2_int)
                        #
                        print('MCC3: %d'%MCC3_int)
                        print('MNC3: %d'%MNC3_int)
                        print('LAC3: %d'%LAC3_int)
                        print('CELLID3: %d'%CELLID3_int)
                        print('Power3: %d'%Power3_int)

                        MyfileWrite('\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        MyfileWrite('\n2 bytes:  %d: MCC1'%MCC1_int)
                        MyfileWrite('\n2 bytes:  %d: MNC1'%MNC1_int)
                        MyfileWrite('\n2 bytes:  %d: LAC1'%LAC1_int)
                        MyfileWrite('\n2 bytes:  %d: CELLID1'%CELLID1_int)
                        MyfileWrite('\n2 bytes:  %d: Power1'%Power1_int)
                        #
                        MyfileWrite('\n2 bytes:  %d: MCC2'%MCC2_int)
                        MyfileWrite('\n2 bytes:  %d: MNC2'%MNC2_int)
                        MyfileWrite('\n2 bytes:  %d: LAC2'%LAC2_int)
                        MyfileWrite('\n2 bytes:  %d: CELLID2'%CELLID2_int)
                        MyfileWrite('\n2 bytes:  %d - Power2'%Power2_int)
                        #
                        MyfileWrite('\n2 bytes:  %d: MCC3'%MCC3_int)
                        MyfileWrite('\n2 bytes:  %d: MNC3'%MNC3_int)
                        MyfileWrite('\n2 bytes:  %d: LAC3'%LAC3_int)
                        MyfileWrite('\n2 bytes:  %d: CELLID3'%CELLID3_int)
                        MyfileWrite('\n2 bytes:  %d: Power3'%Power3_int)
            elif int(frame_data,base = BASE_16)&LSB_12_BITS   == FRAME_TYPE_0x0F:
                    #0x0F00 frame type
                    Frame_header = message[:SIZE_2_BYTE]
                    Frame_header_big_end = int(Frame_header[-SIZE_1_BYTE:]+Frame_header[-SIZE_2_BYTE:-SIZE_1_BYTE],base = BASE_16) 
                    message = message[SIZE_2_BYTE:]

                    Frame_generation_timestamp = message[:SIZE_4_BYTE]
                    Frame_generation_timestamp_big_end = Frame_generation_timestamp[-SIZE_1_BYTE:]+Frame_generation_timestamp[-SIZE_2_BYTE:-SIZE_1_BYTE]+Frame_generation_timestamp[-SIZE_3_BYTE:-SIZE_2_BYTE]+Frame_generation_timestamp[-SIZE_4_BYTE:-SIZE_3_BYTE] 
                    Frame_generation_timestamp_big_eng_int = int(Frame_generation_timestamp_big_end,base=BASE_16) 
                    message = message[SIZE_4_BYTE:]
                    #
                    Sensor_number = message[:SIZE_1_BYTE] 
                    Sensor_number_int = int(Sensor_number,base=BASE_16)
                    message = message[SIZE_1_BYTE:]

                    Temperature = message[:SIZE_2_BYTE]
                    Temperature_int = int(Temperature[-SIZE_1_BYTE:]+Temperature[-SIZE_2_BYTE:-SIZE_1_BYTE],base=BASE_16)/TEN_DEC
                    message = message[SIZE_2_BYTE:]

                    if DEBUG_MODE == '1':
                        #
                        print('\n2 bytes:  0x%0.2X: Type of frame,'%(Frame_header_big_end&LSB_12_BITS),'4 MSB = 0x%0.2X\n'%(Frame_header_big_end>>12)\
                        ,' '*3,'PS:  0x00 – Frame generated on regular base; 0x01 – Frame generated because alarm')
                        print('4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        print('1 byte :  %d: Sensor number'%Sensor_number_int)
                        print('2 bytes:  %0.1f: Temperature'%Temperature_int)

                        MyfileWrite('\n\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        MyfileWrite('\n1 byte :  %d: Sensor number'%Sensor_number_int)
                        MyfileWrite('\n2 bytes:  %0.1f: Temperature'%Temperature_int)
                    else:
                        print('\nTemperature frame')

                        if Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x00:
                                print('Frame generated on regular base')
                                MyfileWrite('\n\nFrame generated on regular base')
                        elif Frame_header_big_end>>TWELVE_DEC == FRAME_GENERATED_0x01:
                                print('Frame generated because alarm')
                                MyfileWrite('\n\nFrame generated because alarm')

                        print('Time: %s (UTC)'% (datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int)))
                        #
                        print('Sensor number: %d'%Sensor_number_int)
                        print('Temperature: %0.1f'%Temperature_int)

                        MyfileWrite('\n2 bytes:  0x%0.2X: Type of frame, 4 MSB = 0x%0.2X'%(Frame_header_big_end&LSB_12_BITS,Frame_header_big_end>>12))
                        MyfileWrite('\n4 bytes:  %s: Frame generation timestamp (Hex) -> %s Time (UTC)' % (Frame_generation_timestamp,(datetime.utcfromtimestamp(Frame_generation_timestamp_big_eng_int))))
                        #
                        MyfileWrite('\n1 byte :  %d: Sensor number'%Sensor_number_int)
                        MyfileWrite('\n2 bytes:  %0.1f C: Temperature'%Temperature_int)
            else:
                print("Error parsing: %s" %message)
                MyfileWrite("\n\nError parsing: %s" %message)
                return

while 1:
        message = str(input('\nEnter data for parsing: '))
        pars(message)