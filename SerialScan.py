import serial.tools.list_ports
import threading
from datetime import datetime
import getpass
import re
#from Scripts import functions
import time
from sys import platform
<<<<<<< Updated upstream
from Classes import PrintThread
from Classes import InputThread
=======
import os

>>>>>>> Stashed changes

class PhotoMaker(threading.Thread):
    def run(self):
        flag = False
        times = 0
        params = s.split()
        print(params)
        ph_times = 0
        if flag == False:
            mc_id = params[2]
            ph_intervals = int(params[3])
            if params.__len__() == 5:
                ph_times = int(params[4])
            flag = True
        while True:
            if s == 'ex':
                flag = False
                return
            elif 'cmd photo stop' in s:
                flag = True
                return
            else:
                p.write(bytes(('mc make_photo ' + mc_id + '\n\r').encode("UTF-8")))
                time.sleep(ph_intervals)
                if ph_times > times:
                    times +=1
                if times > ph_times and ph_times != 0:
                    print("Photo stopped by times")
                    flag = False
                    return


def command(str):
    if 'photo' in str:
        ph = []
        if 'stop' in str:
            print('Photo Stopped')
        else:
            #print(str.split()[2])
            #PhotoM = PhotoMaker
            #ph.append()
            ph[str.split()[2]] = PhotoMaker().start()
            #print(ph[str.split()[2]])
           # ph = PhotoMaker().start()


def escape_ansi(line):
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)



s = ''

def main():
    global p, s, log
    po = []
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(ports.index(p), " - ", p)
        po.append(p.device)

    print('Starting Up Serial Monitor')
    if po.__len__() == 0:
        print("No ports")
        return
    N_port = input("Choose port\n")
    if N_port == 'ex':
        print("End")
        return
    else:
        N_port = int(N_port)
    try:
        p = serial.Serial(
            port = str(po[N_port]),
            baudrate = 115200
            #parity = serial.PARITY_NONE,
            #stopbits = serial.STOPBITS_ONE,
            #bytesize = serial.EIGHTBITS,
            #xonxoff = False,
            #rtscts = False,
            #dsrdtr = False,
            #timeout =2
            #writeTimeout = 0
                )
    except Exception as A:
        print("error open serial port:", str(A))
        exit()
    if p.is_open:
        print('Opened')
<<<<<<< Updated upstream
        #Linux
        if 'linux' in platform:
            filename = '/home/'+getpass.getuser() + '/PyLogs/'+str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))+'.hub.log'
        #Windows
        if 'win32' in platform:
            filename= 'C:/PyLogs/'+str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))+'.hub.log'
=======
        if not os.path.isdir('./PyLogs'):
            os.makedirs('./PyLogs')
        filename ='./PyLogs/'+str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))+'.hub.log'
>>>>>>> Stashed changes
        log = open(filename, 'w+', encoding = "utf-8")
        pt = PrintThread()
        it = InputThread()
        #pt.start()
        #it.start()
        pt.run(s,p,log)
        it.run(s,p)
        f_stop = False
        while True:
            #print(threading.active_count())
            if s == 'ex':
                if not f_stop:
                    if threading.active_count() > 1:
                        pt.stop()
                        it.stop()
                        f_stop = True
                else:
                    if threading.active_count() == 1:
                        p.close()
                        print("Port close")
                        log.close()
                        print("Log file close")
                        break

    else:
        print('Close')


if __name__ == '__main__':
    main()
