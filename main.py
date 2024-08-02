from plot import plot_day


if __name__ == '__main__':
    str_start = "2012-01-02 3:40:5.828388"
    str_end = "2012-01-02 23:20:59.828388"
    dataset = 'hh102'
    inspecting_sensors = ['M005', 'M006', 'M007', 'M008', 'LS005', 'LS006', 'LS007', 'LS008']
    plot_day(dataset, str_start, str_end, inspecting_sensors)