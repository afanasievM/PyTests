import threading
import time


class InputThread(threading.Thread):
    def __init__(self):
        super(InputThread, self).__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()
        return 1

    def join(self, *args, **kwargs):
        self.stop()
        super(InputThread, self).join(*args, **kwargs)

    def run(self, s,p):
        #global s
        while not self._stop_event.is_set():
            s = input()
            if "cmd" in s:
                command(s)
            else:
                p.write(bytes((s+'\n\r').encode("UTF-8")))
        print("Input off")


class PrintThread(threading.Thread):
    def __init__(self):
        super(PrintThread, self).__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()
        return 1

    def join(self, *args, **kwargs):
        self.stop()
        super(PrintThread, self).join(*args, **kwargs)

    def run(self, s, p, log):
        while not self._stop_event.is_set():
            x = p.readline().decode("utf-8")
            x = escape_ansi(x).replace('>\r', '>')
            t = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            print(t + " " + x, end = "")
            if log.closed:
                return
            else:
                log.write(t + " " + x)
        print("Print off")

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
