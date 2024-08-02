# SensorInspect
## Usage
First download the dataset and extract it to the ```data/``` directory. The default dataset is *hh102*.

### File splitter
Split a large data file into smaller chunks. Its source code is ```quickseg.c```. An executable program ```seg``` was compiled from that source code.

For directly splitting the default dataset (*hh102*), run the executable file by:
```
./seg
``` 

To recompile the source code (e.g. custom modify, change dataset,... ), run:
```
gcc -o seg quickseg.c 
```

### Plotter

In ```main.py```, modify the start time, end time and the sensor list which we want to inspect and run. Note that the original dataset must be splitted before run this script.
```python
str_start = "2012-01-02 3:40:5.828388"
str_end = "2012-01-02 23:20:59.828388"
dataset = 'hh102'
inspecting_sensors = ['M005', 'M006', 'M007', 'M008', 'LS005', 'LS006', 'LS007', 'LS008']
plot_day(dataset, str_start, str_end, inspecting_sensors)
```
