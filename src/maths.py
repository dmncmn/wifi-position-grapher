import numpy as np


# noinspection PyMethodMayBeStatic
class Maths:

    def friis_formula(self, watt: float, gain: float) -> float:
        wifi_wave_length = 0.12
        return wifi_wave_length * 0.1 * gain / (4 * np.pi * np.sqrt(watt))

    def dbm_to_watt(self, dbm: float) -> float:
        return 0.001 * 10 * pow(10, dbm) / 10.0

    def calc_circle_intersection(self, circle1: tuple, circle2: tuple):
        """
        :param circle1: tuple, contains X, Y coordinates and radius
        :param circle2: tuple, contains X, Y coordinates and radius
        :return: 2 tuple, contains coordinates points of intersection
        """
        x1, y1, r1 = circle1
        x2, y2, r2 = circle2

        dx, dy = x2 - x1, y2 - y1
        d = np.sqrt(dx * dx + dy * dy)

        if d > r1 + r2:
            return None
        if d < abs(r1 - r2):
            return None
        if d == 0:
            return None

        a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
        h = np.sqrt(r1 * r1 - a * a)
        xm = x1 + a * dx / d
        ym = y1 + a * dy / d
        xs1 = xm + h * dy / d
        xs2 = xm - h * dy / d
        ys1 = ym - h * dx / d
        ys2 = ym + h * dx / d

        return (xs1, ys1), (xs2, ys2)

    def check_and_modify(self, xpoint: float, ypoint: float,
                         base_stations: dict):
        """
        :param xpoint:
        :param ypoint:
        :param base_stations: dict with base stations coordinates
        :return:
        """

        x = xpoint
        y = ypoint
        # General line
        x1 = base_stations['B1x']
        y1 = base_stations['B1y']
        x2 = base_stations['B4x']
        y2 = base_stations['B4y']

        # Points refer to top line
        xt1 = base_stations['B3x']
        yt1 = base_stations['B3y']
        xt2 = base_stations['B4x']
        yt2 = base_stations['B4y']

        # Points refer to bottom line
        xb1 = base_stations['B1x']
        yb1 = base_stations['B1y']
        xb2 = base_stations['B2x']
        yb2 = base_stations['B2y']

        D = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)

        # find projecion on top and bottom lines

        if xt1 == xt2 or xb1 == xb2:
            yp_top, yp_bot = 0, 0
        else:
            yp_top = ((yt2 - yt1) / (xt2 - xt1)) * (x - xt1) + yt1
            yp_bot = ((yb2 - yb1) / (xb2 - xb1)) * (x - xb1) + yb1

        if y <= yp_top:
            pass
        if y >= yp_bot:
            pass
        if y > y2:  # if point upper than top line
            y = yp_top
        if y < y1:  # if point bellow than top line
            y = yp_bot

        if D >= 0:  # if point on the right side
            pass
        else:
            x = ((y - y1) / (y2 - y1)) * (x2 - x1) + x1

        xpoint = x
        ypoint = y

        # Check position reference to line 2-3
        x = xpoint
        y = ypoint

        # General line
        x1 = base_stations['B2x']
        y1 = base_stations['B2y']
        x2 = base_stations['B3x']
        y2 = base_stations['B3y']

        D = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)

        # find projection on top and bottom lines
        if xt1 == xt2 or xb1 == xb2:
            yp_top, yp_bot = 0, 0
        else:
            yp_top = ((yt2 - yt1) / (xt2 - xt1)) * (x - xt1) + yt1
            yp_bot = ((yb2 - yb1) / (xb2 - xb1)) * (x - xb1) + yb1

        if y <= yp_top:
            pass
        if y >= yp_bot:
            pass
        if y > y2:  # if point upper than top line
            y = yp_top
        if y < y1:  # if point bellow than top line
            y = yp_bot

        if D <= 0:  # if point on the right side
            pass
        else:
            x = ((y - y1) / (y2 - y1)) * (x2 - x1) + x1

        xpoint = x
        ypoint = y

        return xpoint, ypoint
