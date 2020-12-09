# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from pyqtgraph import PlotWidget


class UiMainWindow:
    """
    UI implementation
    """
    def setup_UI(self, main_window):

        width, height = 1680, 900
        main_window.resize(width, height)
        main_window.setStyleSheet("QMainWindow {background: '#000000';}")
        main_window.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.central_widget = QtWidgets.QWidget(main_window)

        self.graphics_view = PlotWidget(self.central_widget)
        self.graphics_view.setGeometry(QtCore.QRect(10, 10, 1450, 820))

        self.label_base_addr = QtWidgets.QLabel(self.central_widget)
        self.label_base_addr.setGeometry(QtCore.QRect(1500, 40, 121, 16))

        self.coord_text_field = QtWidgets.\
            QTextEdit(self.central_widget)
        self.coord_text_field.\
            setGeometry(QtCore.QRect(1500, 60, 131, 91))
        self.coord_text_field.\
            document().contentsChanged.connect(self.coord_changed)
        self.coord_text_field.setStyleSheet(
            "font-size: 12px; color: #b5b5b5; background-color: #313131; "
            "border: 0px; text-align: right;")
        self.coord_text_field.setText(
            "Base1: 1.0 1.0\nBase2: 9.0 1.0\nBase3: 9.0 9.0\nBase4: 1.0 9.0"
        )

        self.mac_addr_text_field = QtWidgets.\
            QTextEdit(self.central_widget)
        self.mac_addr_text_field.\
            setGeometry(QtCore.QRect(1500, 180, 131, 91))
        self.mac_addr_text_field.\
            document().contentsChanged.connect(self.mac_addr_changed)
        self.mac_addr_text_field.setStyleSheet(
            "font-size: 12px; color: #b5b5b5; background-color: #313131; "
            "border: 0px; text-align: right;")
        self.mac_addr_text_field.setText('ab:cd:ef:01:02:03')

        self.label_mac_addr = QtWidgets.QLabel(self.central_widget)
        self.label_mac_addr.setGeometry(QtCore.QRect(1500, 160, 71, 16))

        self.start_button = QtWidgets.QPushButton(self.central_widget)
        self.start_button.setGeometry(QtCore.QRect(1500, 280, 131, 41))
        self.start_button.clicked.connect(self.start)

        self.label_last_rssi = QtWidgets.QLabel(self.central_widget)
        self.label_last_rssi.setGeometry(QtCore.QRect(1500, 350, 121, 16))

        self.label_rssi_1 = QtWidgets.QLabel(self.central_widget)
        self.label_rssi_1.setGeometry(QtCore.QRect(1500, 370, 161, 16))

        self.label_rssi_2 = QtWidgets.QLabel(self.central_widget)
        self.label_rssi_2.setGeometry(QtCore.QRect(1500, 390, 161, 16))

        self.label_rssi_3 = QtWidgets.QLabel(self.central_widget)
        self.label_rssi_3.setGeometry(QtCore.QRect(1500, 410, 161, 16))

        self.label_rssi_4 = QtWidgets.QLabel(self.central_widget)
        self.label_rssi_4.setGeometry(QtCore.QRect(1500, 430, 161, 16))

        self.current_gain = QtWidgets.QLabel(self.central_widget)
        self.current_gain.setGeometry(QtCore.QRect(1500, 700, 161, 16))

        self.gain_slider = QtWidgets.\
            QSlider(QtCore.Qt.Horizontal, self.central_widget)
        self.gain_slider.setGeometry(QtCore.QRect(1500, 720, 130, 16))
        self.gain_slider.valueChanged[int].connect(self.set_gain)
        self.gain_slider.setMinimum(1)
        self.gain_slider.setMaximum(100)
        self.gain_slider.setTickInterval(5)

        self.show_position_or_level_button = QtWidgets.\
            QPushButton(self.central_widget)
        self.show_position_or_level_button.\
            setGeometry(QtCore.QRect(1500, 750, 131, 41))
        self.show_position_or_level_button.clicked.\
            connect(self.show_position_or_level)

        self.exit_button = QtWidgets.\
            QPushButton(self.central_widget)
        self.exit_button.\
            setGeometry(QtCore.QRect(1500, 810, 131, 41))
        self.exit_button.clicked.\
            connect(self.exit)

        main_window.setCentralWidget(self.central_widget)
        self.status_bar = QtWidgets.QStatusBar(main_window)
        main_window.setStatusBar(self.status_bar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):

        self.label_base_addr.setText("Base stations:")
        self.label_base_addr.setStyleSheet('color: #b5b5b5')
        self.label_mac_addr.setText("Client addr:")
        self.label_mac_addr.setStyleSheet('color: #b5b5b5')
        self.start_button.setText("Stop")
        self.show_position_or_level_button.setText("Position only")
        self.exit_button.setText("Exit")
        self.exit_button.setStyleSheet('background: #d48a31')
        self.label_last_rssi.setText("Last RSSI:")
        self.label_last_rssi.setStyleSheet('color: #b5b5b5')

        self.label_rssi_1.setText("Base 1:")
        self.label_rssi_1.setStyleSheet('color: #b5b5b5')
        self.label_rssi_2.setText("Base 2:")
        self.label_rssi_2.setStyleSheet('color: #b5b5b5')
        self.label_rssi_3.setText("Base 3:")
        self.label_rssi_3.setStyleSheet('color: #b5b5b5')
        self.label_rssi_4.setText("Base 4:")
        self.label_rssi_4.setStyleSheet('color: #b5b5b5')

        self.current_gain.setText("Gain: ")
        self.current_gain.setStyleSheet('color: #b5b5b5')

    def update_rssi_labels(self, base_station_levels: list):
        self.label_rssi_1.setText("Base 1: %sdBm" %
                                  round(base_station_levels[0],2))
        self.label_rssi_2.setText("Base 2: %sdBm" %
                                  round(base_station_levels[1],2))
        self.label_rssi_3.setText("Base 3: %sdBm" %
                                  round(base_station_levels[2],2))
        self.label_rssi_4.setText("Base 4: %sdBm" %
                                  round(base_station_levels[3],2))

    def coord_changed(self):
        self.coord_text_field.toPlainText()
        coord = self.coord_text_field.toPlainText()
        self.get_coordinates(coord)

    def mac_addr_changed(self):
        self.mac_addr_text_field.toPlainText()
        addr = self.mac_addr_text_field.toPlainText()
        self.get_mac_addr(addr)
