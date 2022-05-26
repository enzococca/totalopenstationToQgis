import serial
import datetime
import argparse


file = "serial.log"

def open_serial(port, bps, is_log=False):
    s = serial.Serial(port, bps)

    while s.is_open:
        line = s.readline().decode()
        t = datetime.datetime.now().ctime()
        line = f"{t} : {line}"
        print(line)
        if is_log:
            with open(file, "a") as f:
                f.writelines(line)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("port", help="serial port. like COM1 or /dev/serial ")
    parser.add_argument("-b", dest="bps", type=int,
                        default=9600, help="serial boundrates")
    parser.add_argument("-l", dest="log", action="store_true", help="is logging")
    # parser.add_argument("-i","--interact",action="store_true",help="interactive")
    args = parser.parse_args()


    open_serial(args.port, args.bps, args.log)

if __name__ == "__main__":
    main()

