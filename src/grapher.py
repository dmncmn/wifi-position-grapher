# -*- coding: utf-8 -*-
from pyqtgraph.Qt import QtCore, QtWidgets
from typing import NoReturn

from src import ui
from src.plots import Plots

timer = QtCore.QTimer()
timer.setInterval(100)

timer_clear = QtCore.QTimer()
timer_clear.setInterval(3000)


class Graph(QtWidgets.QMainWindow, ui.UiMainWindow):

    def __init__(self, rssi_listener):

        super(Graph, self).__init__()

        self.room_dimension_x = 10
        self.room_dimension_y = 10

        self.base_stations = {
            'B1x': 0.0,
            'B1y': 0.0,
            'B2x': 0.0,
            'B2y': 0.0,
            'B3x': 0.0,
            'B3y': 0.0,
            'B4x': 0.0,
            'B4y': 0.0,
        }

        self.rssi = rssi_listener

        self.setup_UI(self)
        self.plots = Plots()
        self.p1 = self.graphics_view.plotItem
        self.init_UI()

        self.rssi.gain = 0.0001

        self.no_plot_levels = False

    def set_gain(self, value: float):
        self.rssi.gain = value / 10000.0
        self.current_gain.setText("Gain: %s" % self.rssi.gain)

    def start(self):
        if self.rssi.start_udp:
            self.rssi.start_udp = False
            self.rssi.test = True
            self.start_button.setText('Stop')
        else:
            self.rssi.start_udp = True
            self.rssi.test = False
            self.start_button.setText('Start')

    def show_position_or_level(self):
        if self.no_plot_levels:
            self.no_plot_levels = False
            self.show_position_or_level_button.setText('Position')
        else:
            self.no_plot_levels = True
            self.p1.plot(clear=True)
            self.show_position_or_level_button.setText('Levels')

    def get_coordinates(self, input_coordinates) -> NoReturn:
        """
        :param input_coordinates: user data for base station coordinates:
        base1: x, y\n
        base2: x, y\n
        base3: x, y\n
        base4: x, y\n
        :return:
        """
        parse_info = input_coordinates.split('\n')
        coord = parse_info[0].split(" ")

        if len(parse_info) != 4:
            return

        try:
            self.B1x, self.B1y = float(coord[1]), float(coord[2])
        except ValueError:
            self.B1x, self.B1y = 0, 0

        coord = parse_info[1].split(" ")
        try:
            self.B2x, self.B2y = float(coord[1]), float(coord[2])
        except ValueError:
            self.B2x, self.B2y = 0, 0

        coord = parse_info[2].split(" ")
        try:
            self.B3x, self.B3y = float(coord[1]), float(coord[2])
        except ValueError:
            self.B3x, self.B3y = 0, 0

        coord = parse_info[3].split(" ")
        try:
            self.B4x, self.B4y = float(coord[1]), float(coord[2])
        except ValueError:
            self.B4x, self.B4y = 0, 0

        self.base_stations = {
            'B1x': self.B1x,
            'B1y': self.B1y,
            'B2x': self.B2x,
            'B2y': self.B2y,
            'B3x': self.B3x,
            'B3y': self.B3y,
            'B4x': self.B4x,
            'B4y': self.B4y,
        }

    def get_mac_addr(self, macinfo: str) -> NoReturn:
        self.rssi.mac_addr = macinfo

    def init_UI(self):

        def update_plot():

            self.plots.\
                plot_level_circles(plotter=self.p1,
                                   base_stations=self.base_stations,
                                   dist_from_base_stations=self.rssi.distance,
                                   no_plot_levels=self.no_plot_levels)

            self.plots.\
                plot_base_stations(plotter=self.p1,
                                   base_stations=self.base_stations)

            self.plots.\
                plot_positions(plotter=self.p1,
                               base_stations=self.base_stations,
                               dist_from_base_stations=self.rssi.distance,
                               no_plot_levels=self.no_plot_levels)

            self.update_rssi_labels(base_station_levels=self.rssi.rssi_level)

        def clear_plot():
            if self.no_plot_levels:
                self.p1.plot(clear=True)

        self.p1.setXRange(0.0, self.room_dimension_x, padding=0)
        self.p1.setYRange(0.0, self.room_dimension_y, padding=0)

        self.p1.showAxis('right')
        self.p1.showAxis('bottom')
        self.p1.showAxis('top')
        self.p1.showGrid(x=True, y=True)
        self.p1.setTitle(u'RSSI WI-FI POSITION GRAPHER')
        self.p1.setLabel('left', 'a (meters)')
        self.p1.setLabel('bottom', 'b (meters)')

        timer.start()
        timer.timeout.connect(update_plot)
        timer_clear.start()
        timer_clear.timeout.connect(clear_plot)

    def exit(self):
        self.rssi.stop()
        raise SystemExit