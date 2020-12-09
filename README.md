# wifi-position-grapher
Test program for visualisation of wifi-client position.
Four base stations collect beacons from wifi-client and send to PC, that collects RSSI-signal from wifi-client via UDP-socket.
Program collects this rssi-signals and converts its into the distance and plots them.

Before do this:
```
python3 -m venv venv
```
```
. venv/bin/activate
```
```
pip install -r requirements.txt
```
Then run:
```
python main.py
```

for debug run: rssi.test = True (default, without open UDP)

Run tests:
```
python -m unittest -v
```

![Image alt](https://github.com/dmncmn/wifi-position-grapher/blob/master/pic1.PNG)
![Image alt](https://github.com/dmncmn/wifi-position-grapher/blob/master/pic2.PNG)