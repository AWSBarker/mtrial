import requests
from flatdict import FlatDict
import random, string
from datetime import datetime as dt

rsys = random.randrange(125, 155)
rdia = random.randrange(75, 89)
rpulse = random.randrange(55, 100)
rimei = random.randrange(358173054439512, 358173054439517)
rts = dt.now().strftime("%Y-%m-%dT%H:%M:%SZ")
mts = dt.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
cid1 = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
cid2 = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
cid3 = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
cid4 = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
cid5 = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
cid = '-'.join((cid1,cid2,cid3,cid4,cid5)).lower()

aurl = 'http://127.0.0.1:8001/itasc/bp/'
#load = {"correlationId": "c418e0b5-8d6e-4237-accf-e30c40a9b5c1", "IMEI": 358173054439520, "timestamp": "2022-05-18T13:46:01+01:00"}

# json "99999" seems to 'convert' to 99999 with BigInteger
# mariadb takes Boolean as tinyint so False is 0

load = {"metadata":
            {"correlationId": cid,
             "receivedTime": mts,
             "deviceGroups": "",
             "measurementType": "BloodPressure"},
        "device": {"id": "TaiDoc:BP800:001-326171744000070A-47",
                   "serialNumber": "001-326171744000070A-47",
                   "IMEI": rimei,
                   "IMSI": "204046206994346",
                   "manufacturer": "TaiDoc",
                   "model": "BP800",
                   "timezone": "Europe/London"},
        "measurements": {"annotations": {"averageMeasurement": 'false', "irregularHeartBeat": 'false'},
                         "diastolicBloodPressure": {"value": rdia, "unit": "mmHg", "isInRange": 'false'},
                         "meanBloodPressure": {"value": 99, "unit": "mmHg", "isInRange": 'true'},
                         "pulse": {"value": rpulse, "unit": "bpm", "isInRange": 'true'},
                         "systolicBloodPressure": {"value": rsys, "unit": "mmHg", "isInRange": 'false'},
                         "timestamp": rts}
        }
print(rimei)
#load['measurements']['timestamp'] = dt.now().strftime("%Y-%m-%dT%H:%M:%SZ")
flat_dict = FlatDict(load, delimiter='_')

# field separators (normalise) = '_', so measurements_annotations_pulse
response = requests.post(aurl, json= load)
print(response.status_code)

"""
load = {"metadata":
            {"correlationId": "c418e0b5-8d6e-4237-accf-e30c40a9b5b9",
             "receivedTime": "2022-05-18T12:46:25.383136859Z",
             "deviceGroups": "",
             "measurementType": "BloodPressure"},
        "device": {"id": "TaiDoc:BP800:001-326171744000070A-47",
                   "serialNumber": "001-326171744000070A-47",
                   "IMEI": "358173054439511",
                   "IMSI": "204046206994346",
                   "manufacturer": "TaiDoc",
                   "model": "BP800",
                   "timezone": "Europe/London"},
        "measurements": {"annotations": {"averageMeasurement": 'false', "irregularHeartBeat": 'false'},
                         "diastolicBloodPressure": {"value": 76, "unit": "mmHg", "isInRange": 'true'},
                         "meanBloodPressure": {"value": 91, "unit": "mmHg", "isInRange": 'true'},
                         "pulse": {"value": 65, "unit": "bpm", "isInRange": 'true'},
                         "systolicBloodPressure": {"value": 131, "unit": "mmHg", "isInRange": 'true'},
                         "timestamp": "2022-05-18T13:45:00+01:00"}
        }
"""
