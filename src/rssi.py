import socket
import threading
import numpy as np

from src.maths import Maths

import random


class UdpThread(threading.Thread):

    def __init__(self):
        super().__init__()
        self.event = threading.Event()
        self.update_time = 0.1

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.UDP_IP = '192.168.77.1'
        self.UDP_PORT = 7777
        self.mac_addr = 'ab:cd:ef'

        self.math = Maths()

        self.gain_filter = 0.8
        self.start_udp = False
        self.gain = 0.1
        self.distance = 0 * np.empty(4)
        self.rssi_level = 0 * np.empty(4)
        self.rssi_level_last = 0 * np.empty(4)
        self.bases = {
            'vt-001': 0,
            'vt-002': 1,
            'vt-003': 2,
            'vt-004': 3,
        }

        self.test = True

    def connect(self):
        if not self.test:
            self.sock.bind((self.UDP_IP, self.UDP_PORT))

    def view_demo(self):
        """
        Test values for rssi level circles, visualise determine position
        self.test must be True
        :return:
        """
        edge_1 = 1
        edge_2 = 100
        rssi_1 = - random.randint(edge_1, edge_2) / 300.0
        rssi_2 = - random.randint(edge_1, edge_2) / 300.0
        rssi_3 = - random.randint(edge_1, edge_2) / 300.0
        rssi_4 = - random.randint(edge_1, edge_2) / 300.0
        self.rssi_level = [-10+rssi_1, -10+rssi_2, -10+rssi_3, -10+rssi_4]
        for rssi in [0, 1, 2, 3]:
            watt = self.math. \
                dbm_to_watt(dbm=self.rssi_level[rssi])
            self.distance[rssi] = self.math. \
                friis_formula(watt=watt, gain=self.gain)

    def run(self):
        while not self.event.is_set():
            self.event.wait(self.update_time)
            if self.start_udp:
                self.udp_listener()
            if self.test:
                self.view_demo()

    def udp_listener(self):
        """
        UDP-parser
        Packet structure:
            beacon_[0] - dummy
            beacon_[1] - base station id
            beacon_[2] - time of arrival
            beacon_[3] - RSSi level
            beacon_[4] - MAC
        :return:
        """

        try:
            data, addr = self.sock.recvfrom(1024)
            data2 = str(data).split("V")
        except socket.error:
            return

        for beacon in data2:
            if "vt" not in beacon:
                continue
            beacon_ = str(beacon).split(" ")
            for item, value in self.bases.items():
                if beacon_[1] == item:
                    try:
                        self.rssi_level[0] = \
                            int(str(beacon_[3]).replace("dBm", ""))
                    except ValueError:
                        self.rssi_level[value] = 0
                        continue
                    self.rssi_level_last[value] = \
                        self.gain_filter * self.rssi_level_last[value] + \
                        (1 - self.gain_filter) * self.rssi_level[value]
                    watt = self.math.\
                        dbm_to_watt(dbm=self.rssi_level_last[value])
                    self.distance[value] = self.math.\
                        friis_formula(watt=watt, gain=self.gain)

    def stop(self):
        self.event.set()
