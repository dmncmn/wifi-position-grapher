import pyqtgraph as pg
import numpy as np

from pyqtgraph.Qt import QtCore
from typing import NoReturn

from src.maths import Maths


# noinspection PyMethodMayBeStatic
class Plots:

    def __init__(self):
        self.math = Maths()
        self.x_circle = np.arange(-1, 1, 0.002)
        self.y_circle = np.sqrt(1 - self.x_circle ** 2)

    def plot_base_stations(self, plotter, base_stations: dict) -> NoReturn:
        """
        Plot base station positions and room boundaries
        :param plotter:
        :param base_stations: dict with base stations coordinates
        :return:
        """
        B1x = base_stations['B1x']
        B1y = base_stations['B1y']
        B2x = base_stations['B2x']
        B2y = base_stations['B2y']
        B3x = base_stations['B3x']
        B3y = base_stations['B3y']
        B4x = base_stations['B4x']
        B4y = base_stations['B4y']

        plotter.plot([B1x, B2x],
                     [B1y, B2y],
                     pen=pg.mkPen(color=(94, 94, 94), width=1,
                                  style=QtCore.Qt.DashLine))
        plotter.plot([B2x, B3x],
                     [B2y, B3y],
                     pen=pg.mkPen(color=(94, 94, 94), width=1,
                                  style=QtCore.Qt.DashLine))
        plotter.plot([B3x, B4x],
                     [B3y, B4y],
                     pen=pg.mkPen(color=(94, 94, 94), width=1,
                                  style=QtCore.Qt.DashLine))
        plotter.plot([B4x, B1x],
                     [B4y, B1y],
                     pen=pg.mkPen(color=(94, 94, 94), width=1,
                                  style=QtCore.Qt.DashLine))
        plotter.plot([B1x], [B1y],
                     symbolBrush=(255, 0, 0), symbol='t1')
        plotter.plot([B2x], [B2y],
                     symbolBrush=(255, 0, 0), symbol='t1')
        plotter.plot([B3x], [B3y],
                     symbolBrush=(255, 0, 0), symbol='t1')
        plotter.plot([B4x], [B4y],
                     symbolBrush=(255, 0, 0), symbol='t1')

    def plot_level_circles(self, plotter, base_stations: dict,
                           dist_from_base_stations: list,
                           no_plot_levels: bool) -> NoReturn:
        """
        Plot RSSI level circles for base stations
        :param plotter:
        :param base_stations: dict with base station coordinates
        :param dist_from_base_stations: radius of level circles
        :param no_plot_levels:
        :return:
        """

        if not no_plot_levels:
            plotter.plot(clear=True)
        else:
            plotter.plot(clear=False)
            return

        B1x = base_stations['B1x']
        B1y = base_stations['B1y']
        B2x = base_stations['B2x']
        B2y = base_stations['B2y']
        B3x = base_stations['B3x']
        B3y = base_stations['B3y']
        B4x = base_stations['B4x']
        B4y = base_stations['B4y']

        x_base1 = dist_from_base_stations[0] * self.x_circle + B1x
        y_base11 = dist_from_base_stations[0] * self.y_circle + B1y
        y_base12 = -dist_from_base_stations[0] * self.y_circle + B1y

        x_base2 = dist_from_base_stations[1] * self.x_circle + B2x
        y_base21 = dist_from_base_stations[1] * self.y_circle + B2y
        y_base22 = -dist_from_base_stations[1] * self.y_circle + B2y

        x_base3 = dist_from_base_stations[2] * self.x_circle + B3x
        y_base31 = dist_from_base_stations[2] * self.y_circle + B3y
        y_base32 = -dist_from_base_stations[2] * self.y_circle + B3y

        x_base4 = dist_from_base_stations[3] * self.x_circle + B4x
        y_base41 = dist_from_base_stations[3] * self.y_circle + B4y
        y_base42 = -dist_from_base_stations[3] * self.y_circle + B4y

        plotter.plot(x_base1, y_base11, clear=None,
                     pen=None,
                     fillBrush=pg.mkBrush(242, 190, 85, 60),
                     fillLevel=B1y)
        plotter.plot(x_base1, y_base12, clear=None,
                     pen=None,
                     fillBrush=pg.mkBrush(242, 190, 85, 60),
                     fillLevel=B1y)

        plotter.plot(x_base2, y_base21, clear=None,
                     pen=None,
                     fillBrush=pg.mkBrush(207, 91, 191, 60),
                     fillLevel=B2y)
        plotter.plot(x_base2, y_base22, clear=None,
                     pen=None,
                     fillBrush=pg.mkBrush(207, 91, 191, 60),
                     fillLevel=B2y)

        plotter.plot(x_base3, y_base31, clear=None,
                     pen=None,
                     fillBrush=pg.mkBrush(49, 195, 212, 60),
                     fillLevel=B3y)
        plotter.plot(x_base3, y_base32, clear=None,
                     pen=None,
                     fillBrush=pg.mkBrush(49, 195, 212, 60),
                     fillLevel=B3y)

        plotter.plot(x_base4, y_base41, clear=None,
                     pen=None,
                     fillBrush=pg.mkBrush(212, 49, 49, 60),
                     fillLevel=B4y)
        plotter.plot(x_base4, y_base42, clear=None,
                     pen=None,
                     fillBrush=pg.mkBrush(212, 49, 49, 60),
                     fillLevel=B4y)

    def plot_positions(self, plotter, base_stations: dict,
                       dist_from_base_stations: list,
                       no_plot_levels: bool) -> NoReturn:
        """
        Plot client position
        :param plotter:
        :param base_stations: dict with base station coordinates
        :param dist_from_base_stations: radius of level circles
        :param no_plot_levels:
        :return:
        """

        B1x = base_stations['B1x']
        B1y = base_stations['B1y']
        B2x = base_stations['B2x']
        B2y = base_stations['B2y']
        B3x = base_stations['B3x']
        B3y = base_stations['B3y']
        B4x = base_stations['B4x']
        B4y = base_stations['B4y']

        # Ищем позицию от базовых станций 1, 2, 3
        act1, act2, act3 = 0 * np.empty(2), 0 * np.empty(2), 0 * np.empty(2)

        b12 = self.math.calc_circle_intersection((B1x, B1y,
                                                  dist_from_base_stations[0]),
                                                 (B2x, B2y,
                                                  dist_from_base_stations[1]))
        b13 = self.math.calc_circle_intersection((B1x, B1y,
                                                  dist_from_base_stations[0]),
                                                 (B3x, B3y,
                                                  dist_from_base_stations[2]))
        b23 = self.math.calc_circle_intersection((B2x, B2y,
                                                  dist_from_base_stations[1]),
                                                 (B3x, B3y,
                                                  dist_from_base_stations[2]))

        if b12 is not None:
            check_point = np.sqrt((b12[0][0] - B3x) ** 2 +
                                  (b12[0][1] - B3y) ** 2)
            if check_point <= dist_from_base_stations[2]:
                if not no_plot_levels: plotter.plot([b12[0][0]],
                                                         [b12[0][1]],
                                                         pen='r', symbol='p')
                act1 = b12[0][0], b12[0][1]

        if b13 is not None:
            check_point = np.sqrt((b13[0][0] - B2x) ** 2 +
                                  (b13[0][1] - B2y) ** 2)
            if check_point <= dist_from_base_stations[1]:
                if not no_plot_levels: plotter.plot([b13[0][0]],
                                                         [b13[0][1]],
                                                         pen='r', symbol='p')
                act2 = b13[0][0], b13[0][1]

        if b23 is not None:
            check_point = np.sqrt((b23[0][0] - B1x) ** 2 +
                                  (b23[0][1] - B1y) ** 2)
            if check_point <= dist_from_base_stations[0]:
                if not no_plot_levels: plotter.plot([b23[0][0]],
                                                         [b23[0][1]],
                                                         pen='r', symbol='p')
                act3 = b23[0][0], b23[0][1]

        if b12 is not None:
            check_point = np.sqrt((b12[1][0] - B3x) ** 2 +
                                  (b12[1][1] - B3y) ** 2)
            if check_point <= dist_from_base_stations[2]:
                if not no_plot_levels: plotter.plot([b12[1][0]],
                                                         [b12[1][1]],
                                                         pen='r', symbol='p')
                act1 = b12[1][0], b12[1][1]

        if b13 is not None:
            check_point = np.sqrt((b13[1][0] - B2x) ** 2 +
                                  (b13[1][1] - B2y) ** 2)
            if check_point <= dist_from_base_stations[1]:
                if not no_plot_levels: plotter.plot([b13[1][0]],
                                                         [b13[1][1]],
                                                         pen='r', symbol='p')
                act2 = b13[1][0], b13[1][1]

        if b23 is not None:
            check_point = np.sqrt((b23[1][0] - B1x) ** 2 +
                                  (b23[1][1] - B1y) ** 2)
            if check_point <= dist_from_base_stations[0]:
                if not no_plot_levels: plotter.plot([b23[1][0]],
                                                         [b23[1][1]],
                                                         pen='r', symbol='p')
                act3 = b23[1][0], b23[1][1]

        point_123 = 0 * np.empty(2)
        point_123[0] = (act1[0] + act2[0] + act3[0]) / 3.0
        point_123[1] = (act1[1] + act2[1] + act3[1]) / 3.0
        point_123[0], point_123[1] = self.math. \
            check_and_modify(point_123[0], point_123[1], base_stations)

        plotter.plot([point_123[0]], [point_123[1]], pen='r', symbol='+')

        # Ищем позицию от базовых станций 1, 2, 4

        act1, act2, act3 = 0 * np.empty(2), 0 * np.empty(2), 0 * np.empty(2)

        b12 = self.math.calc_circle_intersection((B1x, B1y,
                                                  dist_from_base_stations[0]),
                                                 (B2x, B2y,
                                                  dist_from_base_stations[1]))
        b14 = self.math.calc_circle_intersection((B1x, B1y,
                                                  dist_from_base_stations[0]),
                                                 (B4x, B4y,
                                                  dist_from_base_stations[3]))
        b24 = self.math.calc_circle_intersection((B2x, B2y,
                                                  dist_from_base_stations[1]),
                                                 (B4x, B4y,
                                                  dist_from_base_stations[3]))

        if b12 is not None:
            check_point = np.sqrt((b12[0][0] - B4x) ** 2 +
                                  (b12[0][1] - B4y) ** 2)
            if check_point <= dist_from_base_stations[3]:
                if not no_plot_levels: plotter.plot([b12[0][0]],
                                                         [b12[0][1]],
                                                         pen='r', symbol='p')
                act1 = b12[0][0], b12[0][1]

        if b14 is not None:
            check_point = np.sqrt((b14[0][0] - B2x) ** 2 +
                                  (b14[0][1] - B2y) ** 2)
            if check_point <= dist_from_base_stations[1]:
                if not no_plot_levels: plotter.plot([b14[0][0]],
                                                         [b14[0][1]],
                                                         pen='r', symbol='p')
                act2 = b14[0][0], b14[0][1]

        if b24 is not None:
            check_point = np.sqrt((b24[0][0] - B1x) ** 2 +
                                  (b24[0][1] - B1y) ** 2)
            if check_point <= dist_from_base_stations[0]:
                if not no_plot_levels: plotter.plot([b24[0][0]],
                                                         [b24[0][1]],
                                                         pen='r', symbol='p')
                act3 = b24[0][0], b24[0][1]

        if b12 is not None:
            check_point = np.sqrt((b12[1][0] - B4x) ** 2 +
                                  (b12[1][1] - B4y) ** 2)
            if check_point <= dist_from_base_stations[3]:
                if not no_plot_levels: plotter.plot([b12[1][0]],
                                                         [b12[1][1]],
                                                         pen='r', symbol='p')
                act1 = b12[1][0], b12[1][1]

        if b14 is not None:
            check_point = np.sqrt((b14[1][0] - B2x) ** 2 +
                                  (b14[1][1] - B2y) ** 2)
            if check_point <= dist_from_base_stations[1]:
                if not no_plot_levels: plotter.plot([b14[1][0]],
                                                         [b14[1][1]],
                                                         pen='r', symbol='p')
                act2 = b14[1][0], b14[1][1]

        if b24 is not None:
            check_point = np.sqrt((b24[1][0] - B1x) ** 2 +
                                  (b24[1][1] - B1y) ** 2)
            if check_point <= dist_from_base_stations[0]:
                if not no_plot_levels: plotter.plot([b24[1][0]],
                                                         [b24[1][1]],
                                                         pen='r', symbol='p')
                act3 = b24[1][0], b24[1][1]

        point_124 = 0 * np.empty(2)
        point_124[0] = (act1[0] + act2[0] + act3[0]) / 3.0
        point_124[1] = (act1[1] + act2[1] + act3[1]) / 3.0

        point_124[0], point_124[1] = self.math. \
            check_and_modify(point_124[0], point_124[1], base_stations)

        plotter.plot([point_124[0]], [point_124[1]], pen='r', symbol='+')

        # Ищем позицию от базовых станций 1, 3, 4

        act1, act2, act3 = 0 * np.empty(2), 0 * np.empty(2), 0 * np.empty(2)

        b13 = self.math.calc_circle_intersection((B1x, B1y,
                                                  dist_from_base_stations[0]),
                                                 (B3x, B3y,
                                                  dist_from_base_stations[2]))
        b14 = self.math.calc_circle_intersection((B1x, B1y,
                                                  dist_from_base_stations[0]),
                                                 (B4x, B4y,
                                                  dist_from_base_stations[3]))
        b34 = self.math.calc_circle_intersection((B3x, B3y,
                                                  dist_from_base_stations[2]),
                                                 (B4x, B4y,
                                                  dist_from_base_stations[3]))

        if b13 is not None:
            check_point = np.sqrt((b13[0][0] - B4x) ** 2 +
                                  (b13[0][1] - B4y) ** 2)
            if check_point <= dist_from_base_stations[3]:
                if not no_plot_levels: plotter.plot([b13[0][0]],
                                                         [b13[0][1]],
                                                         pen='r', symbol='p')
                act1 = b13[0][0], b13[0][1]

        if b14 is not None:
            check_point = np.sqrt((b14[0][0] - B3x) ** 2 +
                                  (b14[0][1] - B3y) ** 2)
            if check_point <= dist_from_base_stations[2]:
                if not no_plot_levels: plotter.plot([b14[0][0]],
                                                         [b14[0][1]],
                                                         pen='r', symbol='p')
                act2 = b14[0][0], b14[0][1]

        if b34 is not None:
            check_point = np.sqrt((b34[0][0] - B1x) ** 2 +
                                  (b34[0][1] - B1y) ** 2)
            if check_point <= dist_from_base_stations[0]:
                if not no_plot_levels: plotter.plot([b34[0][0]],
                                                         [b34[0][1]],
                                                         pen='r', symbol='p')
                act3 = b34[0][0], b34[0][1]

        if b13 is not None:
            check_point = np.sqrt((b13[1][0] - B4x) ** 2 +
                                  (b13[1][1] - B4y) ** 2)
            if check_point <= dist_from_base_stations[3]:
                if not no_plot_levels: plotter.plot([b13[1][0]],
                                                         [b13[1][1]],
                                                         pen='r', symbol='p')
                act1 = b13[1][0], b13[1][1]

        if b14 is not None:
            check_point = np.sqrt((b14[1][0] - B3x) ** 2 +
                                  (b14[1][1] - B3y) ** 2)
            if check_point <= dist_from_base_stations[2]:
                if not no_plot_levels: plotter.plot([b14[1][0]],
                                                         [b14[1][1]],
                                                         pen='r', symbol='p')
                act2 = b14[1][0], b14[1][1]

        if b34 is not None:
            check_point = np.sqrt((b34[1][0] - B1x) ** 2 +
                                  (b34[1][1] - B1y) ** 2)
            if check_point <= dist_from_base_stations[0]:
                if not no_plot_levels: plotter.plot([b34[1][0]],
                                                         [b34[1][1]],
                                                         pen='r', symbol='p')
                act3 = b34[1][0], b34[1][1]

        point_134 = 0 * np.empty(2)
        point_134[0] = (act1[0] + act2[0] + act3[0]) / 3.0
        point_134[1] = (act1[1] + act2[1] + act3[1]) / 3.0

        point_134[0], point_134[1] = self.math. \
            check_and_modify(point_134[0], point_134[1], base_stations)

        plotter.plot([point_134[0]], [point_134[1]], pen='r', symbol='+')

        # Ищем позицию от базовых станций 2, 3, 4

        act1, act2, act3 = 0 * np.empty(2), 0 * np.empty(2), 0 * np.empty(2)
        b23 = self.math.calc_circle_intersection((B2x, B2y,
                                                  dist_from_base_stations[1]),
                                                 (B3x, B3y,
                                                  dist_from_base_stations[2]))
        b24 = self.math.calc_circle_intersection((B2x, B2y,
                                                  dist_from_base_stations[1]),
                                                 (B4x, B4y,
                                                  dist_from_base_stations[3]))
        b34 = self.math.calc_circle_intersection((B3x, B3y,
                                                  dist_from_base_stations[2]),
                                                 (B4x, B4y,
                                                  dist_from_base_stations[3]))

        if b23 is not None:
            check_point = np.sqrt((b23[0][0] - B4x) ** 2 +
                                  (b23[0][1] - B4y) ** 2)
            if check_point <= dist_from_base_stations[3]:
                if not no_plot_levels: plotter.plot([b23[0][0]],
                                                         [b23[0][1]],
                                                         pen='r', symbol='p')
                act1 = b23[0][0], b23[0][1]

        if b24 is not None:
            check_point = np.sqrt((b24[0][0] - B3x) ** 2 +
                                  (b24[0][1] - B3y) ** 2)
            if check_point <= dist_from_base_stations[2]:
                if not no_plot_levels: plotter.plot([b24[0][0]],
                                                         [b24[0][1]],
                                                         pen='r', symbol='p')
                act2 = b24[0][0], b24[0][1]

        if b34 is not None:
            check_point = np.sqrt((b34[0][0] - B2x) ** 2 +
                                  (b34[0][1] - B2y) ** 2)
            if check_point <= dist_from_base_stations[1]:
                if not no_plot_levels: plotter.plot([b34[0][0]],
                                                         [b34[0][1]],
                                                         pen='r', symbol='p')
                act3 = b34[0][0], b34[0][1]

        if b23 is not None:
            check_point = np.sqrt((b23[1][0] - B4x) ** 2 +
                                  (b23[1][1] - B4y) ** 2)
            if check_point <= dist_from_base_stations[3]:
                if not no_plot_levels: plotter.plot([b23[1][0]],
                                                         [b23[1][1]],
                                                         pen='r', symbol='p')
                act1 = b23[1][0], b23[1][1]

        if b24 is not None:
            check_point = np.sqrt((b24[1][0] - B3x) ** 2 +
                                  (b24[1][1] - B3y) ** 2)
            if check_point <= dist_from_base_stations[2]:
                if not no_plot_levels: plotter.plot([b24[1][0]],
                                                         [b24[1][1]],
                                                         pen='r', symbol='p')
                act2 = b24[1][0], b24[1][1]

        if b34 is not None:
            check_point = np.sqrt((b34[1][0] - B2x) ** 2 +
                                  (b34[1][1] - B2y) ** 2)
            if check_point <= dist_from_base_stations[1]:
                if not no_plot_levels: plotter.plot([b34[1][0]],
                                                         [b34[1][1]],
                                                         pen='r', symbol='p')
                act3 = b34[1][0], b34[1][1]

        point_234 = 0 * np.empty(2)
        point_234[0] = (act1[0] + act2[0] + act3[0]) / 3.0
        point_234[1] = (act1[1] + act2[1] + act3[1]) / 3.0

        point_234[0], point_234[1] = self.math. \
            check_and_modify(point_234[0], point_234[1], base_stations)

        plotter.plot([point_234[0]], [point_234[1]], pen='r', symbol='+')

        zero_values = 0
        init_point_x = B1x
        init_point_y = B1y

        if point_123[0] == init_point_x and point_123[1] == init_point_y:
            point_123 = 0 * point_123
            zero_values += 1
        if point_124[0] == init_point_x and point_124[1] == init_point_y:
            point_124 = 0 * point_124
            zero_values += 1
        if point_134[0] == init_point_x and point_134[1] == init_point_y:
            point_134 = 0 * point_134
            zero_values += 1
        if point_234[0] == init_point_x and point_234[1] == init_point_y:
            point_234 = 0 * point_234
            zero_values += 1

        average_point = 0, 0
        if zero_values != 4:
            average_point = (point_123[0] +
                             point_124[0] +
                             point_134[0] +
                             point_234[0]) / (4.0 - zero_values), \
                            (point_123[1] +
                             point_124[1] +
                             point_134[1] +
                             point_234[1]) / (4.0 - zero_values)

        plotter.plot([average_point[0]], [average_point[1]], pen='r',
                     symbol='o', symbolBrush=(255, 0, 0))