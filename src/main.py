import sys
from PyQt5 import QtWidgets

from rssi import UdpThread
from grapher import Graph


def main():
    app = QtWidgets.QApplication(sys.argv)
    udp = UdpThread()
    udp.connect()
    udp.start()
    Graph(rssi_listener=udp).show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
