class SerialComm:
    def _init_(self):
        self.port = serial.Serial("/dev/tty/USB0", baudrate = 9600, timeout = 1)

    def read_serial(self):
        res = self.port.read(50)
        if len(res):
            return res
        else:
            return None

    def send_serial(self, text):
        self.port.write(text)

class ShellWrapper:
    def _init_(self):
        self.ps = subprocess.Popen(['bash'], stdout = subprocess.PIPE,
                                   stderr = subprocess.PIPE,
                                   stdin = subprocess.PIPE)

    def execute_command(self, command):
        self.ps.stdin.write(command + "\n")

    def get_output(self):
        timeout = False
        time_limit = .5
        lines = []
        while not timeout:
            poll_result = select.select([self.ps.stdout, self.ps.stderr],
                                        [], [], time_limit)[0]
            if len(poll_result):
                for p in poll_result:
                    lines.append(p.readline())
            else:
                timeout = True
        return lines

def main():
    shell = ShellWrapper()
    ble_comm = SerialComm()
    while True:
        out = ble_comm.read_serial()
        for ble_line in out;
        print(out)
        shell.execute_command(ble_line)
        shell_out = shell.get_output()
        for l in shell_out:
            print(l)
            ble_comm.send_serial(l)s
