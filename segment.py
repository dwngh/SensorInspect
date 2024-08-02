from datetime import datetime, timedelta
import matplotlib.dates
from copy import deepcopy
import numpy as np

def toindex(y, m , d):
    return (y - 2011) * 36 + (m - 1) * 3 + int(d / 10)

# Geek4geek code :))
def binary_search(arr, low, high, x):
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		return high

class Segment:
    def __init__(self, year, segnum, dataset_name, isStart=False, isEnd=False):
        self.file = open(f"segments/{year}/{dataset_name}_{segnum}.txt", "r")
        self.initState = {}
        self.currentState = None
        self.isStart = isStart
        self.isEnd = isEnd
        self.states = []
        self.timestamps = []
    
    def read(self):
        c = 0
        for line in self.file:
            parts = line.split()
            if parts[0] == 'i':
                self.initState[parts[1]] = int(parts[2])
            else:
                dtstr = parts[0] + " " + parts[1]
                self.timestamps.append(datetime.strptime(dtstr,'%Y-%m-%d %H:%M:%S.%f'))
                if self.currentState is None:
                    self.currentState = deepcopy(self.initState)
                if parts[2] not in self.currentState:
                    for s in self.states:
                        s.append(None)
                self.currentState[parts[2]] = int(parts[3])
                self.states.append(list(self.currentState.values()))
                c += 1
        self.states = np.array(self.states)
        c = 0
        for key, val in self.currentState.items():
            self.currentState[key] = c
            c += 1
    
    def getDtIndex(self, dt):
        r = binary_search(self.timestamps, 0, len(self.timestamps) - 1, dt)
        if r < 0:
             return 0
        if r > self.states.shape[0]:
             return self.states.shape[0] - 1
        return r

    def getTransTimeAndData(self, name, startdt=None, enddt=None):
        data = self.states.T[self.currentState[name]]
        rng = (0, len(data)) if startdt is None else (self.getDtIndex(startdt), self.getDtIndex(enddt) + 1)

        timestamps = []
        tdata = []
        for i in range(rng[0], rng[1] - 1):
            tdata.append(data[i])
            tdata.append(data[i])
            timestamps.append(self.timestamps[i])
            timestamps.append(self.timestamps[i + 1] - timedelta(microseconds=1))
        tdata.append(data[rng[1] - 1])
        timestamps.append(self.timestamps[rng[1] - 1])
        dates = matplotlib.dates.date2num(timestamps)
        return dates, tdata