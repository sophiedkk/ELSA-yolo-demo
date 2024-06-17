from ultralytics import YOLO

import settings as s

yolo_model = YOLO(s.MODEL, task="detect")
yolo_model.export(format="ncnn", imgsz=s.IMAGE_HEIGHT)  # creates 'yolov8n_ncnn_model'
