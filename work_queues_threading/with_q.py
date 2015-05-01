import os, re, threading, Queue


class PingCheck(threading.Thread):
    received_packages = re.compile(r"(\d) packets received")  # regex for output

    def __init__(self, in_q, out_q):
        threading.Thread.__init__(self)
        self.in_q = in_q
        self.out_q = out_q
        self.daemon = True  # ensure that our threads are destroyed when the main finishes

    def run(self):
        while True:
            ip_address = self.in_q.get()
            print(ip_address)
            ping_out = os.popen("ping -q -c2 " + ip, "r")
            line = ping_out.readline()
            n_received = re.findall(self.received_packages,line)
            result = "IP address {0}: {1} received".format(ip, n_received)
            self.out_q.put(result)
            self.in_q.task_done()

    def do_ping(self, ip_address):
        ping_out = os.popen("ping -q -c2 " + ip_address, "r")
        while True:
            line = ping_out.readline()
            if not line:
                break
            n_recieved = ""
            result = ""
        return result


class PingResult(threading.Thread):
    lock = threading.Lock()

    def __init__(self, out_q):
        threading.Thread.__init__(self)
        self.out_q = out_q
        self.daemon = True

    def run(self):
        while True:
            result = self.out_q.get()
            self.lock.acquire()
            print(result)
            self.lock.release()
            self.out_q.task_done()

if __name__ == "__main__":
    in_queue = Queue.Queue()
    out_queue = Queue.Queue()

    # put all the work items in the in_queue
    for suffix in range(1,255):
        ip = "10.25.1."+str(suffix)
        in_queue.put(ip)

    # spawn processes that will process the work items and put results in the out_queue
    for n in xrange(10):
        check = PingCheck(in_queue, out_queue)
        check.start()

    # spawn processes that will process the output in out_q
    for n in xrange(10):
        get_result = PingResult(out_queue)
        get_result.start()

    out = raw_input()  # exit the program and kill threads
