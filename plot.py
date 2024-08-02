from datetime import datetime
import matplotlib.pyplot as plt
from segment import Segment


def plot_day(dataset_name, start_str, end_str, inspecting_sensors):

    # plt.style.use('dark_background')
    inspecting_sensors.sort()

    def to_index(y, m , d):
        return (y - 2011) * 36 + (m - 1) * 3 + int(d / 10)

    dt_start = datetime.strptime(start_str,'%Y-%m-%d %H:%M:%S.%f')
    dt_end = datetime.strptime(end_str,'%Y-%m-%d %H:%M:%S.%f')

    seg_start, seg_end = to_index(dt_start.year, dt_start.month, dt_start.day), to_index(dt_end.year, dt_end.month, dt_end.day)
    print((seg_start, seg_end))
    if dt_start.month == 1 and dt_start.day < 10:
        segment = Segment(dt_start.year - 1, seg_start, dataset_name, True)
    else:
        segment = Segment(dt_start.year, seg_start, dataset_name, True)
    segment.read()

    dt_list = []
    data = {}

    for i in inspecting_sensors:
        t, d = segment.getTransTimeAndData(i, dt_start, dt_end)
        dt_list = t
        data[i] = d

    fig, axs = plt.subplots(len(inspecting_sensors), 1, layout='constrained')
    plt.rcParams['axes.titlepad'] = -14

    for i, s in enumerate(inspecting_sensors):
        # axs[i].set_title(s)
        axs[i].plot(dt_list, data[s])
        axs[i].xaxis.axis_date()
        if max(data[s]) > 1:
            axs[i].set_ylim(0, max(data[s]) + 5)
    # plt.savefig(f'camo/neuvo/2012-10-{day}_(4).png')
    # print(day)
    # plt.close()
    plt.show()
