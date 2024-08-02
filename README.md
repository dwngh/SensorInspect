# SensorInspect
## Sử dụng
Tải dataset về thư mục ```data/```. Dataset mặc định của repo là *hh102*.

### File splitter
Chia file data lớn thành nhiều file nhỏ. 
Để trực tiếp chia dataset mặc định (*hh102*), chạy lệnh sau:
```
./seg
``` 

Để phiên dịch lại mã của chương trình chia file (ví dụ để sử dụng với dataset khác, fix bug, cải tiến,...):
```
gcc -o seg quickseg.c 
```

### Plotter

Trong file ```main.py```, chỉnh lại thời gian bắt đầu, thời gian kết thúc và các loại cảm biến sẽ được vẽ. Sau đó chạy file trên.
```python
str_start = "2012-01-02 3:40:5.828388"
str_end = "2012-01-02 23:20:59.828388"
dataset = 'hh102'
inspecting_sensors = ['M005', 'M006', 'M007', 'M008', 'LS005', 'LS006', 'LS007', 'LS008']
plot_day(dataset, str_start, str_end, inspecting_sensors)
```
